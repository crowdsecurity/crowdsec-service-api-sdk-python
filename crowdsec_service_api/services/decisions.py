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
        super().__init__(base_url=base_url, auth=auth, user_agent="crowdsec_service_api/1.133.1")
    
    def get_decisions(
        self,
        page: int = 1,
        size: int = 50,
        instance_ids: list[str] = [],
        tag_ids: list[str] = [],
        remediation_types: list[str] = [],
        ips: list[str] = [],
        alert_ids: list[str] = [],
        decision_ids: list[str] = [],
        created_at_from: Optional[str] = None,
        sort_by: Optional[DecisionsSortBy] = DecisionsSortBy("created_at"),
        sort_order: Optional[DecisionsSortOrder] = DecisionsSortOrder("desc"),
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
    
    def delete_decision(
        self,
        decision_id: str,
    ):
        endpoint_url = "/decisions/{decision_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            DecisionsDeleteDecisionPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.delete(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    
    def get_aggregated_decisions(
        self,
        page: int = 1,
        size: int = 50,
        instance_ids: list[str] = [],
        tag_ids: list[str] = [],
        remediation_types: list[str] = [],
        ips: list[str] = [],
        alert_ids: list[str] = [],
        decision_ids: list[str] = [],
        created_at_from: Optional[str] = None,
        sort_by: Optional[AggregatedDecisionsSortBy] = AggregatedDecisionsSortBy("first_created_at"),
        sort_order: Optional[DecisionsSortOrder] = DecisionsSortOrder("desc"),
    )-> AggregatedDecisionsGetResponsePage:
        endpoint_url = "/decisions/aggregated"
        loc = locals()
        headers = {}
        params = json.loads(
            DecisionsGetAggregatedDecisionsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = {}
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return AggregatedDecisionsGetResponsePage(_client=self, **response.json())
    
    def delete_aggregated_decisions(
        self,
        aggregated_id: str,
    ):
        endpoint_url = "/decisions/aggregated/{aggregated_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            DecisionsDeleteAggregatedDecisionsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.delete(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    
    def delete_aggregated_decision_item(
        self,
        aggregated_id: str,
        decision_id: str,
    ):
        endpoint_url = "/decisions/aggregated/{aggregated_id}/items/{decision_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            DecisionsDeleteAggregatedDecisionItemPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.delete(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    