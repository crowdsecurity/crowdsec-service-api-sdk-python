import json
from types import NoneType
from typing import Optional, Union, Annotated

from ..models import *
from ..base_model import Page, Service
from pydantic import BaseModel, Field
from pydantic.fields import FieldInfo
from httpx import Auth
from ..http_client import HttpClient

class Fingerprints(Service):
    def __init__(self, auth: Auth, base_url: str = "https://admin.api.crowdsec.net/v1") -> None:
        super().__init__(base_url=base_url, auth=auth, user_agent="crowdsec_service_api/1.132.2")
    
    def get_fingerprint_rules(
        self,
        query: Optional[str] = None,
        sort_by: Optional[GetCVEsSortBy] = GetCVEsSortBy("rule_release_date"),
        sort_order: Optional[GetCVEsSortOrder] = GetCVEsSortOrder("desc"),
        detailed: bool = False,
        page: int = 1,
        size: int = 50,
    )-> GetFingerprintRulesResponsePage:
        endpoint_url = "/fingerprints"
        loc = locals()
        headers = {}
        params = json.loads(
            FingerprintsGetFingerprintRulesQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = {}
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return GetFingerprintRulesResponsePage(_client=self, **response.json())
    
    def download_fingerprint_ips(
        self,
        fingerprint: str,
    )-> str:
        endpoint_url = "/fingerprints/{fingerprint}/ips-download"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            FingerprintsDownloadFingerprintIpsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return response.text
    
    def get_fingerprint_ips_details(
        self,
        fingerprint: str,
        since: Optional[str] = "14d",
        page: int = 1,
        size: int = 50,
    )-> GetFingerprintIPsResponsePage:
        endpoint_url = "/fingerprints/{fingerprint}/ips-details"
        loc = locals()
        headers = {}
        params = json.loads(
            FingerprintsGetFingerprintIpsDetailsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            FingerprintsGetFingerprintIpsDetailsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return GetFingerprintIPsResponsePage(_client=self, **response.json())
    
    def get_fingerprint_ips_details_stats(
        self,
        fingerprint: str,
        since: Optional[str] = "14d",
    )-> IpsDetailsStats:
        endpoint_url = "/fingerprints/{fingerprint}/ips-details-stats"
        loc = locals()
        headers = {}
        params = json.loads(
            FingerprintsGetFingerprintIpsDetailsStatsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            FingerprintsGetFingerprintIpsDetailsStatsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return IpsDetailsStats(**response.json())
    
    def get_fingerprint_subscribed_integrations(
        self,
        fingerprint: str,
        page: int = 1,
        size: int = 50,
    )-> GetFingerprintSubscribedIntegrationsResponsePage:
        endpoint_url = "/fingerprints/{fingerprint}/integrations"
        loc = locals()
        headers = {}
        params = json.loads(
            FingerprintsGetFingerprintSubscribedIntegrationsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            FingerprintsGetFingerprintSubscribedIntegrationsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return GetFingerprintSubscribedIntegrationsResponsePage(_client=self, **response.json())
    
    def subscribe_integration_to_fingerprint(
        self,
        request: SubscribeFingerprintIntegrationRequest,
        fingerprint: str,
    ):
        endpoint_url = "/fingerprints/{fingerprint}/integrations"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            FingerprintsSubscribeIntegrationToFingerprintPathParameters(**loc).model_dump_json(
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
    
    def unsubscribe_integration_from_fingerprint(
        self,
        fingerprint: str,
        integration_name: str,
    ):
        endpoint_url = "/fingerprints/{fingerprint}/integrations/{integration_name}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            FingerprintsUnsubscribeIntegrationFromFingerprintPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.delete(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    
    def get_fingerprint_timeline(
        self,
        fingerprint: str,
        since_days: SinceOptions,
        interval: Optional[IntervalOptions] = None,
    )-> list[FingerprintTimelineItem]:
        endpoint_url = "/fingerprints/{fingerprint}/timeline"
        loc = locals()
        headers = {}
        params = json.loads(
            FingerprintsGetFingerprintTimelineQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            FingerprintsGetFingerprintTimelinePathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return [FingerprintTimelineItem(**item) for item in response.json()]
    
    def get_fingerprint_indicators(
        self,
        fingerprint: str,
        sort_by: IndicatorsSortBy,
        indicator_type: Optional[list[IndicatorType]] = None,
    )-> list[IndicatorHttpPath]:
        endpoint_url = "/fingerprints/{fingerprint}/indicators"
        loc = locals()
        headers = {}
        params = json.loads(
            FingerprintsGetFingerprintIndicatorsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            FingerprintsGetFingerprintIndicatorsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return [IndicatorHttpPath(**item) for item in response.json()]
    
    def get_fingerprint_rule(
        self,
        fingerprint: str,
    )-> FingerprintRuleResponse:
        endpoint_url = "/fingerprints/{fingerprint}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            FingerprintsGetFingerprintRulePathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return FingerprintRuleResponse(**response.json())
    