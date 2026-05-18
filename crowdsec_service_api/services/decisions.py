import json
from types import NoneType
from typing import Optional, Union, Annotated

from ..models import *
from ..base_model import Page, Service
from pydantic import BaseModel, Field
from pydantic.fields import FieldInfo
from httpx import Auth
from ..http_client import HttpClient

class Decisions(Service):
    def __init__(self, auth: Auth, base_url: str = "https://admin.api.crowdsec.net/v1") -> None:
        super().__init__(base_url=base_url, auth=auth, user_agent="crowdsec_service_api/1.122.0")
    
    def get_decisions(
        self,
        instance_ids: list[str] = [],
        tag_ids: list[str] = [],
        remediation_types: list[str] = [],
        ips: list[str] = [],
        sort_by: Optional[DecisionsSortBy] = DecisionsSortBy("created_at"),
        sort_order: Optional[DecisionsSortOrder] = DecisionsSortOrder("desc"),
        page: int = 1,
        size: int = 50,
    )-> DecisionsGetResponsePage:
        endpoint_url = "/decisions"
        loc = locals()
        headers = {}
        params = json.loads(
            DecisionsGetDecisionsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = {}
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return DecisionsGetResponsePage(_client=self, **response.json())
    
    def create_decision(
        self,
        request: DecisionCreateRequest,
    )-> DecisionCreateResponse:
        endpoint_url = "/decisions"
        loc = locals()
        headers = {}
        params = {}
        path_params = {}
        
        payload = json.loads(
            request.model_dump_json(
                exclude_none=True
            )
        ) if "request" in loc else None
        response = self.http_client.post(
            url=endpoint_url, path_params=path_params, params=params, headers=headers, json=payload
        )
        
        return DecisionCreateResponse(**response.json())
    