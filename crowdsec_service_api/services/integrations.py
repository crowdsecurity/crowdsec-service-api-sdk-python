import json
from httpx import Auth
from ..models import *
from ..base_model import Page, Service
from ..http_client import HttpClient

class Integrations(Service):
    
    def get_integrations(
        self,
        page: int = 1,
        size: int = 50,
    )-> Page[IntegrationGetResponse]:
        endpoint_url = "/integrations"
        loc = locals()
        headers = {}
        params = json.loads(
            IntegrationsGetIntegrationsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = {}
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return Page[IntegrationGetResponse](**response.json())
    
    def create_integration(
        self,
        request: IntegrationCreateRequest,
    )-> IntegrationCreateResponse:
        endpoint_url = "/integrations"
        loc = locals()
        headers = {}
        params = {}
        path_params = {}
        
        response = self.http_client.post(
            url=endpoint_url, path_params=path_params, params=params, headers=headers, json=json.loads(
                request.model_dump_json(
                    exclude_none=True
                )
            )
        )
        
        return IntegrationCreateResponse(**response.json())
    
    def get_integration(
        self,
        integration_id: str,
    )-> IntegrationGetResponse:
        endpoint_url = "/integrations/{integration_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            IntegrationsGetIntegrationPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return IntegrationGetResponse(**response.json())
    
    def delete_integration(
        self,
        integration_id: str,
    ):
        endpoint_url = "/integrations/{integration_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            IntegrationsDeleteIntegrationPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.delete(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    
    def update_integration(
        self,
        request: IntegrationUpdateRequest,
        integration_id: str,
    )-> IntegrationUpdateResponse:
        endpoint_url = "/integrations/{integration_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            IntegrationsUpdateIntegrationPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.patch(
            url=endpoint_url, path_params=path_params, params=params, headers=headers, json=json.loads(
                request.model_dump_json(
                    exclude_unset=True
                )
            )
        )
        
        return IntegrationUpdateResponse(**response.json())
    
    def get_integration_content(
        self,
        integration_id: str,
        page: int = 1,
        page_size: Optional[int] = None,
    ):
        endpoint_url = "/integrations/{integration_id}/content"
        loc = locals()
        headers = {}
        params = json.loads(
            IntegrationsGetIntegrationContentQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            IntegrationsGetIntegrationContentPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    
    def get_integration_content_stream(
        self,
        integration_id: str,
        startup: bool = False,
    ):
        endpoint_url = "/integrations/{integration_id}/v1/decisions/stream"
        loc = locals()
        headers = {}
        params = json.loads(
            IntegrationsGetIntegrationContentStreamQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            IntegrationsGetIntegrationContentStreamPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    