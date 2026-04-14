"""Tests for scripts/update_version.py."""
import importlib
import json
import sys
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).parent


@pytest.fixture
def uv(monkeypatch, tmp_path):
    """Import update_version fresh with cwd = tmp_path so relative `pyproject.toml` resolves there."""
    monkeypatch.chdir(tmp_path)
    monkeypatch.syspath_prepend(str(SCRIPTS_DIR))
    if "update_version" in sys.modules:
        del sys.modules["update_version"]
    module = importlib.import_module("update_version")
    yield module


PYPROJECT_TEMPLATE = """\
[build-system]
requires = ["setuptools>=61.0"]

[project]
name = "crowdsec_service_api"
version = "{version}"
license = {{ text = "MIT" }}
"""


def _seed(tmp_path, version, *, openapi_pretty=False, service_files=None, package="crowdsec_service_api"):
    (tmp_path / "pyproject.toml").write_text(PYPROJECT_TEMPLATE.format(version=version))

    spec = {"openapi": "3.1.0", "info": {"title": "T", "version": version}, "paths": {}}
    openapi_path = tmp_path / "openapi.json"
    if openapi_pretty:
        openapi_path.write_text(json.dumps(spec, indent=2))
    else:
        openapi_path.write_text(json.dumps(spec))

    if service_files:
        svc_dir = tmp_path / package / "services"
        svc_dir.mkdir(parents=True)
        for name in service_files:
            (svc_dir / name).write_text(
                f'class X:\n    def __init__(self):\n        super().__init__(user_agent="{package}/{version}")\n'
            )
    return openapi_path


class TestNormalize:
    def test_strips_v_prefix(self, uv):
        assert uv.normalize("v1.0.0") == "1.0.0"

    def test_converts_dash_to_dot(self, uv):
        assert uv.normalize("v1.0.0-dev15") == "1.0.0.dev15"

    def test_clean_version_unchanged(self, uv):
        assert uv.normalize("1.2.3") == "1.2.3"

    def test_multiple_dashes(self, uv):
        assert uv.normalize("v1.0.0-rc-1") == "1.0.0.rc.1"


class TestReadPyprojectVersion:
    def test_extracts_version(self, uv, tmp_path):
        _seed(tmp_path, "1.2.3")
        assert uv.read_pyproject_version() == "1.2.3"

    def test_exits_when_missing(self, uv, tmp_path):
        (tmp_path / "pyproject.toml").write_text("[project]\nname = 'x'\n")
        with pytest.raises(SystemExit):
            uv.read_pyproject_version()


class TestUpdatePyproject:
    def test_replaces_version(self, uv, tmp_path):
        _seed(tmp_path, "1.0.0")
        uv.update_pyproject("2.0.0")
        assert uv.read_pyproject_version() == "2.0.0"

    def test_replaces_only_project_version(self, uv, tmp_path):
        (tmp_path / "pyproject.toml").write_text(
            '[project]\nversion = "1.0.0"\n\n[tool.other]\nversion = "9.9.9"\n'
        )
        uv.update_pyproject("2.0.0")
        text = (tmp_path / "pyproject.toml").read_text()
        assert 'version = "2.0.0"' in text
        assert 'version = "9.9.9"' in text


class TestUpdateOpenapi:
    def test_preserves_minified(self, uv, tmp_path):
        path = _seed(tmp_path, "1.0.0", openapi_pretty=False)
        uv.update_openapi(path, "2.0.0")
        text = path.read_text()
        assert "\n" not in text
        assert json.loads(text)["info"]["version"] == "2.0.0"

    def test_preserves_pretty(self, uv, tmp_path):
        path = _seed(tmp_path, "1.0.0", openapi_pretty=True)
        uv.update_openapi(path, "2.0.0")
        text = path.read_text()
        assert "\n" in text
        assert json.loads(text)["info"]["version"] == "2.0.0"

    def test_creates_info_if_missing(self, uv, tmp_path):
        path = tmp_path / "openapi.json"
        path.write_text(json.dumps({"openapi": "3.1.0", "paths": {}}))
        uv.update_openapi(path, "2.0.0")
        assert json.loads(path.read_text())["info"]["version"] == "2.0.0"


class TestUpdateServiceFiles:
    def test_replaces_user_agent_in_all_services(self, uv, tmp_path):
        _seed(tmp_path, "1.0.0", service_files=["allowlists.py", "blocklists.py"])
        uv.update_service_files("crowdsec_service_api", "1.0.0", "2.0.0")
        for name in ("allowlists.py", "blocklists.py"):
            text = (tmp_path / "crowdsec_service_api" / "services" / name).read_text()
            assert 'user_agent="crowdsec_service_api/2.0.0"' in text
            assert 'user_agent="crowdsec_service_api/1.0.0"' not in text

    def test_no_services_dir_is_ok(self, uv, tmp_path):
        _seed(tmp_path, "1.0.0")
        uv.update_service_files("crowdsec_service_api", "1.0.0", "2.0.0")

    def test_leaves_unrelated_user_agents_alone(self, uv, tmp_path):
        _seed(tmp_path, "1.0.0", service_files=["a.py"])
        path = tmp_path / "crowdsec_service_api" / "services" / "a.py"
        path.write_text('user_agent="other_pkg/1.0.0"')
        uv.update_service_files("crowdsec_service_api", "1.0.0", "2.0.0")
        assert path.read_text() == 'user_agent="other_pkg/1.0.0"'


class TestMain:
    def _args(self, monkeypatch, *args):
        monkeypatch.setattr(sys, "argv", ["update_version.py", *args])

    def test_happy_path_updates_everything(self, uv, tmp_path, monkeypatch, capsys):
        _seed(tmp_path, "1.0.0", openapi_pretty=True, service_files=["a.py"])
        self._args(monkeypatch, "v2.0.0", "crowdsec_service_api", "openapi.json")
        uv.main()
        assert uv.read_pyproject_version() == "2.0.0"
        spec = json.loads((tmp_path / "openapi.json").read_text())
        assert spec["info"]["version"] == "2.0.0"
        text = (tmp_path / "crowdsec_service_api" / "services" / "a.py").read_text()
        assert 'user_agent="crowdsec_service_api/2.0.0"' in text

    def test_normalizes_dev_tag(self, uv, tmp_path, monkeypatch):
        _seed(tmp_path, "1.0.0", service_files=["a.py"])
        self._args(monkeypatch, "v1.0.0-dev15", "crowdsec_service_api", "openapi.json")
        uv.main()
        assert uv.read_pyproject_version() == "1.0.0.dev15"
        text = (tmp_path / "crowdsec_service_api" / "services" / "a.py").read_text()
        assert 'user_agent="crowdsec_service_api/1.0.0.dev15"' in text

    def test_idempotent_when_version_matches(self, uv, tmp_path, monkeypatch, capsys):
        _seed(tmp_path, "1.0.0", openapi_pretty=True, service_files=["a.py"])
        svc = tmp_path / "crowdsec_service_api" / "services" / "a.py"
        before_pyproject = (tmp_path / "pyproject.toml").read_text()
        before_openapi = (tmp_path / "openapi.json").read_text()
        before_service = svc.read_text()

        self._args(monkeypatch, "v1.0.0", "crowdsec_service_api", "openapi.json")
        uv.main()

        assert (tmp_path / "pyproject.toml").read_text() == before_pyproject
        assert (tmp_path / "openapi.json").read_text() == before_openapi
        assert svc.read_text() == before_service
        assert "already matches" in capsys.readouterr().out

    def test_wrong_arg_count_exits(self, uv, tmp_path, monkeypatch):
        _seed(tmp_path, "1.0.0")
        self._args(monkeypatch, "v1.0.0")
        with pytest.raises(SystemExit):
            uv.main()

    def test_no_services_dir(self, uv, tmp_path, monkeypatch):
        _seed(tmp_path, "1.0.0")
        self._args(monkeypatch, "v2.0.0", "crowdsec_service_api", "openapi.json")
        uv.main()
        assert uv.read_pyproject_version() == "2.0.0"
