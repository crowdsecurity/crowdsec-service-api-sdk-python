import json
from types import NoneType
from typing import Optional, Union, Annotated

from ..models import *
from ..base_model import Page, Service
from pydantic import BaseModel, Field
from pydantic.fields import FieldInfo
from httpx import Auth
from ..http_client import HttpClient

class Allowlists(Service):
    
    def list_allowlists(
        self,
        page: int = 1,
        size: int = 50,
    )-> Page[AllowlistGetResponse]:
        endpoint_url = "/allowlists"
        loc = locals()
        headers = {}
        params = json.loads(
            AllowlistsListAllowlistsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = {}
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return Page[AllowlistGetResponse](_client=self, **response.json())
    
    def create_allowlist(
        self,
        request: AllowlistCreateRequest,
    )-> AllowlistCreateResponse:
        endpoint_url = "/allowlists"
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
        
        return AllowlistCreateResponse(**response.json())
    
    def get_allowlist(
        self,
        allowlist_id: str,
    )-> AllowlistGetResponse:
        endpoint_url = "/allowlists/{allowlist_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            AllowlistsGetAllowlistPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return AllowlistGetResponse(**response.json())
    
    def delete_allowlist(
        self,
        allowlist_id: str,
        force: bool = False,
    ):
        endpoint_url = "/allowlists/{allowlist_id}"
        loc = locals()
        headers = {}
        params = json.loads(
            AllowlistsDeleteAllowlistQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            AllowlistsDeleteAllowlistPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.delete(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    
    def update_allowlist(
        self,
        request: AllowlistUpdateRequest,
        allowlist_id: str,
    )-> AllowlistUpdateResponse:
        endpoint_url = "/allowlists/{allowlist_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            AllowlistsUpdateAllowlistPathParameters(**loc).model_dump_json(
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
        
        return AllowlistUpdateResponse(**response.json())
    
    def get_allowlist_items(
        self,
        allowlist_id: str,
        page: int = 1,
        size: int = 50,
    )-> Page[AllowlistGetItemsResponse]:
        endpoint_url = "/allowlists/{allowlist_id}/items"
        loc = locals()
        headers = {}
        params = json.loads(
            AllowlistsGetAllowlistItemsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            AllowlistsGetAllowlistItemsPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return Page[AllowlistGetItemsResponse](_client=self, **response.json())
    
    def create_allowlist_items(
        self,
        request: AllowlistItemsCreateRequest,
        allowlist_id: str,
    ):
        endpoint_url = "/allowlists/{allowlist_id}/items"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            AllowlistsCreateAllowlistItemsPathParameters(**loc).model_dump_json(
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
    
    def get_allowlist_item(
        self,
        allowlist_id: str,
        item_id: str,
    )-> AllowlistGetItemsResponse:
        endpoint_url = "/allowlists/{allowlist_id}/items/{item_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            AllowlistsGetAllowlistItemPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return AllowlistGetItemsResponse(**response.json())
    
    def delete_allowlist_item(
        self,
        allowlist_id: str,
        item_id: str,
    ):
        endpoint_url = "/allowlists/{allowlist_id}/items/{item_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            AllowlistsDeleteAllowlistItemPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.delete(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    
    def update_allowlist_item(
        self,
        request: AllowlistItemUpdateRequest,
        allowlist_id: str,
        item_id: str,
    )-> AllowlistItemUpdateResponse:
        endpoint_url = "/allowlists/{allowlist_id}/items/{item_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            AllowlistsUpdateAllowlistItemPathParameters(**loc).model_dump_json(
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
        
        return AllowlistItemUpdateResponse(**response.json())
    
    def get_allowlist_subscribers(
        self,
        allowlist_id: str,
        page: int = 1,
        size: int = 50,
    )-> Page[AllowlistSubscriberEntity]:
        endpoint_url = "/allowlists/{allowlist_id}/subscribers"
        loc = locals()
        headers = {}
        params = json.loads(
            AllowlistsGetAllowlistSubscribersQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            AllowlistsGetAllowlistSubscribersPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return Page[AllowlistSubscriberEntity](_client=self, **response.json())
    
    def subscribe_allowlist(
        self,
        request: AllowlistSubscriptionRequest,
        allowlist_id: str,
    )-> AllowlistSubscriptionResponse:
        endpoint_url = "/allowlists/{allowlist_id}/subscribers"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            AllowlistsSubscribeAllowlistPathParameters(**loc).model_dump_json(
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
        
        return AllowlistSubscriptionResponse(**response.json())
    
    def unsubscribe_allowlist(
        self,
        allowlist_id: str,
        entity_id: str,
    ):
        endpoint_url = "/allowlists/{allowlist_id}/subscribers/{entity_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            AllowlistsUnsubscribeAllowlistPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.delete(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    