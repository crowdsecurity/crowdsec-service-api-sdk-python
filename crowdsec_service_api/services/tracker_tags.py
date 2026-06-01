import json
from types import NoneType
from typing import Optional, Union, Annotated

from ..models import *
from ..base_model import Page, Service
from pydantic import BaseModel, Field
from pydantic.fields import FieldInfo
from httpx import Auth
from ..http_client import HttpClient

class TrackerTags(Service):
    def __init__(self, auth: Auth, base_url: str = "https://admin.api.crowdsec.net/v1") -> None:
        super().__init__(base_url=base_url, auth=auth, user_agent="crowdsec_service_api/v0.15.34")
    
    def get_tags(
        self,
        query: Optional[str] = None,
        page: int = 1,
        size: int = 50,
    )-> LookupListWithStatsResponsePage:
        endpoint_url = "/tags"
        loc = locals()
        headers = {}
        params = json.loads(
            TrackerTagsGetTagsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = {}
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return LookupListWithStatsResponsePage(_client=self, **response.json())
    
    def get_tag_impact(
        self,
        tag: str,
        sort_by: Optional[GetCVEsSortBy] = GetCVEsSortBy("rule_release_date"),
        sort_order: Optional[GetCVEsSortOrder] = GetCVEsSortOrder("desc"),
        page: int = 1,
        size: int = 50,
    )-> LookupImpactResponsePage:
        endpoint_url = "/tags/{tag}"
        loc = locals()
        headers = {}
        params = json.loads(
            TrackerTagsGetTagImpactQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            TrackerTagsGetTagImpactPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return LookupImpactResponsePage(_client=self, **response.json())
    
    def get_tracker_tags(
        self,
        query: Optional[str] = None,
        page: int = 1,
        size: int = 50,
    )-> LookupListWithStatsResponsePage:
        endpoint_url = "/tracker-tags"
        loc = locals()
        headers = {}
        params = json.loads(
            TrackerTagsGetTrackerTagsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = {}
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return LookupListWithStatsResponsePage(_client=self, **response.json())
    
    def get_tracker_tag_impact(
        self,
        tag: str,
        sort_by: Optional[GetCVEsSortBy] = GetCVEsSortBy("rule_release_date"),
        sort_order: Optional[GetCVEsSortOrder] = GetCVEsSortOrder("desc"),
        page: int = 1,
        size: int = 50,
    )-> LookupImpactResponsePage:
        endpoint_url = "/tracker-tags/{tag}"
        loc = locals()
        headers = {}
        params = json.loads(
            TrackerTagsGetTrackerTagImpactQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            TrackerTagsGetTrackerTagImpactPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return LookupImpactResponsePage(_client=self, **response.json())
    