from urllib.parse import quote, urlparse

from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import botocore.session

import httpx


class AWSSignV4Auth(httpx.Auth):
    def __init__(self, aws_region="eu-west-1") -> None:
        self.aws_region = aws_region

    def auth_flow(self, request):
        request = self.sign_request(request)
        yield request

    def sign_request(self, request: httpx.Request) -> httpx.Request:
        """Signs an httpx request with AWS Signature Version 4."""

        session = botocore.session.get_session()
        credentials = session.get_credentials()
        aws_request = AWSRequest(
            method=request.method.upper(), url=str(request.url), data=request.content
        )
        region = self.aws_region
        service = "execute-api"

        # Sign the request
        SigV4Auth(credentials, service, region).add_auth(aws_request)

        # Update the httpx request headers with the signed headers
        request.headers.update(dict(aws_request.headers))

        return request


class ApiKeyAuth(httpx.Auth):
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def auth_flow(self, request):
        request.headers["x-api-key"] = self.api_key
        yield request


class HttpClient:
    def __init__(
        self,
        base_url: str,
        auth: httpx.Auth,
        user_agent: str = None,
        aws_region="eu-west-1",
    ) -> None:
        self.aws_region = aws_region
        self.base_url = base_url
        self.auth = auth
        headers = {"Accept-Encoding": "gzip"}
        if user_agent:
            headers["User-Agent"] = user_agent
        self.client = httpx.Client(headers=headers)
        self.timeout = 30

    def _replace_path_params(self, url: str, path_params: dict):
        if path_params:
            for param, value in path_params.items():
                if not value:
                    raise ValueError(
                        f"Parameter {param} is required, cannot be empty or blank."
                    )
                url = url.replace(f"{{{param}}}", quote(str(value)))
        return url

    def _normalize_url(self, url: str):
        self.base_url = self.base_url.rstrip("/")
        parsed_url = urlparse(url)
        if not parsed_url.netloc:
            return f"{self.base_url}{url}"
        return url

    def get(
        self,
        url: str,
        path_params: dict = None,
        params: dict = None,
        headers: dict = None,
    ):
        url = self._replace_path_params(
            url=self._normalize_url(url), path_params=path_params
        )
        response = self.client.get(
            url=url,
            params=params,
            headers=headers,
            auth=self.auth,
            timeout=self.timeout,
        )
        response.raise_for_status()
        return response

    def post(
        self, url: str, path_params: dict, params: dict, headers: dict, json: dict
    ):
        url = self._replace_path_params(
            url=self._normalize_url(url), path_params=path_params
        )
        response = self.client.post(
            url=url,
            params=params,
            headers=headers,
            json=json,
            auth=self.auth,
            timeout=self.timeout,
        )
        response.raise_for_status()
        return response

    def put(self, url: str, path_params: dict, params: dict, headers: dict, json: dict):
        url = self._replace_path_params(
            url=self._normalize_url(url), path_params=path_params
        )
        response = self.client.put(
            url=url,
            params=params,
            headers=headers,
            json=json,
            auth=self.auth,
            timeout=self.timeout,
        )
        response.raise_for_status()
        return response

    def patch(
        self, url: str, path_params: dict, params: dict, headers: dict, json: dict
    ):
        url = self._replace_path_params(
            url=self._normalize_url(url), path_params=path_params
        )
        response = self.client.patch(
            url=url,
            params=params,
            headers=headers,
            json=json,
            auth=self.auth,
            timeout=self.timeout,
        )
        response.raise_for_status()
        return response

    def delete(self, url: str, path_params: dict, params: dict, headers: dict):
        url = self._replace_path_params(
            url=self._normalize_url(url), path_params=path_params
        )
        response = self.client.delete(
            url=url,
            params=params,
            headers=headers,
            auth=self.auth,
            timeout=self.timeout,
        )
        response.raise_for_status()
        return response
