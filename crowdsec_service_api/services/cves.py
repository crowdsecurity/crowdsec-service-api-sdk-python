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
    def __init__(self, auth: Auth, base_url: str = "https://admin.api.crowdsec.net/v1") -> None:
        super().__init__(base_url=base_url, auth=auth, user_agent="crowdsec_service_api/1.130.0")
    
    def get_cves(
        self,
        query: Optional[str] = None,
        sort_by: Optional[GetCVEsSortBy] = GetCVEsSortBy("rule_release_date"),
        sort_order: Optional[GetCVEsSortOrder] = GetCVEsSortOrder("desc"),
        exploitation_phase: Optional[CVEExploitationPhase] = None,
        detailed: bool = False,
        page: int = 1,
        size: int = 50,
    )-> GetCVEsResponsePage:
        endpoint_url = "/cves"
        loc = locals()
        headers = {}
        params = json.loads(
            CvesGetCvesQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = {}
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return GetCVEsResponsePage(_client=self, **response.json())
    
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
    
    def get_cve_protect_rules(
        self,
        cve_id: str,
    )-> GetCVEProtectRulesResponse:
        endpoint_url = "/cves/{cve_id}/protect-rules"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            CvesGetCveProtectRulesPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return GetCVEProtectRulesResponse(**response.json())
    
    def download_cve_ips(
        self,
        cve_id: str,
    )-> str:
        endpoint_url = "/cves/{cve_id}/ips-download"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            CvesDownloadCveIpsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return response.text
    
    def get_cve_ips_details(
        self,
        cve_id: str,
        since: Optional[str] = "14d",
        page: int = 1,
        size: int = 50,
    )-> GetCVEIPsResponsePage:
        endpoint_url = "/cves/{cve_id}/ips-details"
        loc = locals()
        headers = {}
        params = json.loads(
            CvesGetCveIpsDetailsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            CvesGetCveIpsDetailsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return GetCVEIPsResponsePage(_client=self, **response.json())
    
    def get_cve_ips_details_stats(
        self,
        cve_id: str,
        since: Optional[str] = "14d",
    )-> IpsDetailsStats:
        endpoint_url = "/cves/{cve_id}/ips-details-stats"
        loc = locals()
        headers = {}
        params = json.loads(
            CvesGetCveIpsDetailsStatsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            CvesGetCveIpsDetailsStatsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return IpsDetailsStats(**response.json())
    
    def get_cve_subscribed_integrations(
        self,
        cve_id: str,
        page: int = 1,
        size: int = 50,
    )-> GetCVESubscribedIntegrationsResponsePage:
        endpoint_url = "/cves/{cve_id}/integrations"
        loc = locals()
        headers = {}
        params = json.loads(
            CvesGetCveSubscribedIntegrationsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            CvesGetCveSubscribedIntegrationsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return GetCVESubscribedIntegrationsResponsePage(_client=self, **response.json())
    
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
    
    def get_cve_indicators(
        self,
        cve_id: str,
        sort_by: IndicatorsSortBy,
        indicator_type: Optional[list[IndicatorType]] = None,
    )-> list[IndicatorHttpPath]:
        endpoint_url = "/cves/{cve_id}/indicators"
        loc = locals()
        headers = {}
        params = json.loads(
            CvesGetCveIndicatorsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            CvesGetCveIndicatorsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return [IndicatorHttpPath(**item) for item in response.json()]
    
    def get_cve_timeline(
        self,
        cve_id: str,
        since_days: SinceOptions,
    )-> list[TimelineItem]:
        endpoint_url = "/cves/{cve_id}/timeline"
        loc = locals()
        headers = {}
        params = json.loads(
            CvesGetCveTimelineQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            CvesGetCveTimelinePathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return [TimelineItem(**item) for item in response.json()]
    