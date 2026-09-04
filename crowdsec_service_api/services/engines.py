import json
from types import NoneType
from typing import Optional, Union, Annotated

from ..models import *
from ..base_model import Page, Service
from pydantic import BaseModel, Field
from pydantic.fields import FieldInfo
from httpx import Auth
from ..http_client import HttpClient

class Engines(Service):
    def __init__(self, auth: Auth, base_url: str = "https://admin.api.crowdsec.net/v1") -> None:
        super().__init__(base_url=base_url, auth=auth, user_agent="crowdsec_service_api/1.137.0")
    
    def get_engines(
        self,
        tag: Optional[list[str]] = None,
        page: int = 1,
        size: int = 50,
    )-> EngineGetResponsePage:
        endpoint_url = "/engines"
        loc = locals()
        headers = {}
        params = json.loads(
            EnginesGetEnginesQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = {}
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return EngineGetResponsePage(_client=self, **response.json())
    