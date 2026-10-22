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
        super().__init__(base_url=base_url, auth=auth, user_agent="crowdsec_service_api/1.143.0")
    
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
    
    def get_engine(
        self,
        engine_id: str,
    )-> EngineGetResponse:
        endpoint_url = "/engines/{engine_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            EnginesGetEnginePathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return EngineGetResponse(**response.json())
    
    def associate_tags_with_engine(
        self,
        request: EngineAssociateTagsRequest,
        engine_id: str,
    )-> EngineAssociateTagsResponse:
        endpoint_url = "/engines/{engine_id}/tags"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            EnginesAssociateTagsWithEnginePathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        payload = json.loads(
            request.model_dump_json(
                exclude_none=True
            )
        ) if "request" in loc else None
        response = self.http_client.post(
            url=endpoint_url, path_params=path_params, params=params, headers=headers, json=payload
        )
        
        return EngineAssociateTagsResponse(**response.json())
    
    def disassociate_tags_with_engine(
        self,
        engine_id: str,
        tag_name: str,
    ):
        endpoint_url = "/engines/{engine_id}/tags/{tag_name}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            EnginesDisassociateTagsWithEnginePathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.delete(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    
    def get_engine_log_processors(
        self,
        engine_id: str,
        page: int = 1,
        size: int = 50,
    )-> LogProcessorsGetResponsePage:
        endpoint_url = "/engines/{engine_id}/log_processors"
        loc = locals()
        headers = {}
        params = json.loads(
            EnginesGetEngineLogProcessorsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            EnginesGetEngineLogProcessorsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return LogProcessorsGetResponsePage(_client=self, **response.json())
    
    def get_engine_remediation_components(
        self,
        engine_id: str,
        page: int = 1,
        size: int = 50,
    )-> RemediationComponentsGetResponsePage:
        endpoint_url = "/engines/{engine_id}/remediation_components"
        loc = locals()
        headers = {}
        params = json.loads(
            EnginesGetEngineRemediationComponentsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            EnginesGetEngineRemediationComponentsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return RemediationComponentsGetResponsePage(_client=self, **response.json())
    