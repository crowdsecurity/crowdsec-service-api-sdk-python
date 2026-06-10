import json
from types import NoneType
from typing import Optional, Union, Annotated

from ..models import *
from ..base_model import Page, Service
from pydantic import BaseModel, Field
from pydantic.fields import FieldInfo
from httpx import Auth
from ..http_client import HttpClient

class Vendors(Service):
    def __init__(self, auth: Auth, base_url: str = "https://admin.api.crowdsec.net/v1") -> None:
        super().__init__(base_url=base_url, auth=auth, user_agent="crowdsec_service_api/1.127.1")
    
    def get_vendors(
        self,
        query: Optional[str] = None,
        sort_by: Optional[VendorSortBy] = None,
        sort_order: Optional[GetCVEsSortOrder] = GetCVEsSortOrder("desc"),
        page: int = 1,
        size: int = 50,
    )-> LookupListWithStatsResponsePage:
        endpoint_url = "/vendors"
        loc = locals()
        headers = {}
        params = json.loads(
            VendorsGetVendorsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = {}
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return LookupListWithStatsResponsePage(_client=self, **response.json())
    
    def get_vendor_stats(
        self,
        vendor: str,
    )-> VendorStatsResponse:
        endpoint_url = "/vendors/{vendor}/stats"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            VendorsGetVendorStatsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return VendorStatsResponse(**response.json())
    
    def download_vendor_ips(
        self,
        vendor: str,
    )-> str:
        endpoint_url = "/vendors/{vendor}/ips-download"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            VendorsDownloadVendorIpsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return response.text
    
    def get_vendor_ips_details(
        self,
        vendor: str,
        since: Optional[str] = "14d",
        page: int = 1,
        size: int = 50,
    )-> GetVendorIPsResponsePage:
        endpoint_url = "/vendors/{vendor}/ips-details"
        loc = locals()
        headers = {}
        params = json.loads(
            VendorsGetVendorIpsDetailsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            VendorsGetVendorIpsDetailsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return GetVendorIPsResponsePage(_client=self, **response.json())
    
    def get_vendor_ips_details_stats(
        self,
        vendor: str,
        since: Optional[str] = "14d",
    )-> IpsDetailsStats:
        endpoint_url = "/vendors/{vendor}/ips-details-stats"
        loc = locals()
        headers = {}
        params = json.loads(
            VendorsGetVendorIpsDetailsStatsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            VendorsGetVendorIpsDetailsStatsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return IpsDetailsStats(**response.json())
    
    def get_vendor_subscribed_integrations(
        self,
        vendor: str,
        page: int = 1,
        size: int = 50,
    )-> GetVendorSubscribedIntegrationsResponsePage:
        endpoint_url = "/vendors/{vendor}/integrations"
        loc = locals()
        headers = {}
        params = json.loads(
            VendorsGetVendorSubscribedIntegrationsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            VendorsGetVendorSubscribedIntegrationsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return GetVendorSubscribedIntegrationsResponsePage(_client=self, **response.json())
    
    def subscribe_integration_to_vendor(
        self,
        request: SubscribeVendorIntegrationRequest,
        vendor: str,
    ):
        endpoint_url = "/vendors/{vendor}/integrations"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            VendorsSubscribeIntegrationToVendorPathParameters(**loc).model_dump_json(
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
    
    def unsubscribe_integration_from_vendor(
        self,
        vendor: str,
        integration_name: str,
    ):
        endpoint_url = "/vendors/{vendor}/integrations/{integration_name}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            VendorsUnsubscribeIntegrationFromVendorPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.delete(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    
    def get_vendor_impact(
        self,
        vendor: str,
        sort_by: Optional[GetCVEsSortBy] = GetCVEsSortBy("rule_release_date"),
        sort_order: Optional[GetCVEsSortOrder] = GetCVEsSortOrder("desc"),
        page: int = 1,
        size: int = 50,
    )-> LookupImpactResponsePage:
        endpoint_url = "/vendors/{vendor}"
        loc = locals()
        headers = {}
        params = json.loads(
            VendorsGetVendorImpactQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            VendorsGetVendorImpactPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return LookupImpactResponsePage(_client=self, **response.json())
    