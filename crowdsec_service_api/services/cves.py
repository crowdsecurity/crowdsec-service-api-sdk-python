import json
from types import NoneType
from typing import Optional, Union, Annotated

from ..models import *
from ..base_model import Page, Service
from pydantic import BaseModel, Field
from pydantic.fields import FieldInfo
from httpx import Auth
from ..http_client import HttpClient

class Cves(Service):
    
    def get_cve(
        self,
        cve_id: str,
    )-> GetCVEResponse:
        endpoint_url = "/cves/{cve_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            CvesGetCvePathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return GetCVEResponse(**response.json())
    
    def get_cve_ips(
        self,
        cve_id: str,
        since: Optional[str] = None,
        page: int = 1,
        size: int = 50,
    )-> GetCVEIPsResponsePage:
        endpoint_url = "/cves/{cve_id}/ips"
        loc = locals()
        headers = {}
        params = json.loads(
            CvesGetCveIpsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            CvesGetCveIpsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return GetCVEIPsResponsePage(**response.json())
    
    def subscribe_integration_to_cve(
        self,
        request: SubscribeCVEIntegrationRequest,
        cve_id: str,
    ):
        endpoint_url = "/cves/{cve_id}/integrations"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            CvesSubscribeIntegrationToCvePathParameters(**loc).model_dump_json(
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
        
        return None
    
    def unsubscribe_integration_from_cve(
        self,
        cve_id: str,
        integration_name: str,
    ):
        endpoint_url = "/cves/{cve_id}/integrations/{integration_name}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            CvesUnsubscribeIntegrationFromCvePathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.delete(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    