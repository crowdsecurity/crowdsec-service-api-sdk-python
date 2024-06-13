import json
from httpx import Auth
from ..models import *
from ..base_model import Page, Service
from ..http_client import HttpClient

class Blocklists(Service):
    
    def get_blocklists(
        self,
        page: int = 1,
        page_size: int = 100,
        subscribed_only: bool = False,
        exclude_subscribed: bool = False,
        include_filter: list[BlocklistIncludeFilters] = ['private', 'shared'],
        size: int = 50,
    )-> Page[BlocklistResponse]:
        endpoint_url = "/blocklists"
        loc = locals()
        headers = {}
        params = json.loads(
            BlocklistsGetBlocklistsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = {}
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return Page[BlocklistResponse](**response.json())
    
    def create_blocklist(
        self,
        request: BlocklistCreateRequest,
    )-> BlocklistCreateResponse:
        endpoint_url = "/blocklists"
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
        
        return BlocklistCreateResponse(**response.json())
    
    def get_blocklist(
        self,
        blocklist_id: str,
    )-> BlocklistGetResponse:
        endpoint_url = "/blocklists/{blocklist_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            BlocklistsGetBlocklistPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return BlocklistGetResponse(**response.json())
    
    def delete_blocklist(
        self,
        blocklist_id: str,
        force: bool = False,
    ):
        endpoint_url = "/blocklists/{blocklist_id}"
        loc = locals()
        headers = {}
        params = json.loads(
            BlocklistsDeleteBlocklistQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            BlocklistsDeleteBlocklistPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.delete(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    
    def update_blocklist(
        self,
        request: BlocklistUpdateRequest,
        blocklist_id: str,
    )-> BlocklistResponse:
        endpoint_url = "/blocklists/{blocklist_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            BlocklistsUpdateBlocklistPathParameters(**loc).model_dump_json(
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
        
        return BlocklistResponse(**response.json())
    
    def add_ips_to_blocklist(
        self,
        request: BlocklistAddIPsRequest,
        blocklist_id: str,
    ):
        endpoint_url = "/blocklists/{blocklist_id}/ips"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            BlocklistsAddIpsToBlocklistPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.post(
            url=endpoint_url, path_params=path_params, params=params, headers=headers, json=json.loads(
                request.model_dump_json(
                    exclude_none=True
                )
            )
        )
        
        return None
    
    def delete_ips_from_blocklist(
        self,
        request: BlocklistDeleteIPsRequest,
        blocklist_id: str,
    ):
        endpoint_url = "/blocklists/{blocklist_id}/ips/delete"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            BlocklistsDeleteIpsFromBlocklistPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.post(
            url=endpoint_url, path_params=path_params, params=params, headers=headers, json=json.loads(
                request.model_dump_json(
                    exclude_none=True
                )
            )
        )
        
        return None
    
    def download_blocklist_content(
        self,
        blocklist_id: str,
        if_modified_since: Optional[str] = None,
        if_none_match: Optional[str] = None,
    )-> str:
        endpoint_url = "/blocklists/{blocklist_id}/download"
        loc = locals()
        headers = json.loads(
            BlocklistsDownloadBlocklistContentHeadersParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        params = {}
        path_params = json.loads(
            BlocklistsDownloadBlocklistContentPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return response.text
    
    def get_blocklist_subscribers(
        self,
        blocklist_id: str,
    )-> BlocklistSubscribersResponse:
        endpoint_url = "/blocklists/{blocklist_id}/subscribers"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            BlocklistsGetBlocklistSubscribersPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return BlocklistSubscribersResponse(**response.json())
    
    def subscribe_blocklist(
        self,
        request: BlocklistSubscriptionRequest,
        blocklist_id: str,
    )-> BlocklistSubscriptionResponse:
        endpoint_url = "/blocklists/{blocklist_id}/subscribers"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            BlocklistsSubscribeBlocklistPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.post(
            url=endpoint_url, path_params=path_params, params=params, headers=headers, json=json.loads(
                request.model_dump_json(
                    exclude_none=True
                )
            )
        )
        
        return BlocklistSubscriptionResponse(**response.json())
    
    def unsubscribe_blocklist(
        self,
        blocklist_id: str,
        entity_id: str,
    ):
        endpoint_url = "/blocklists/{blocklist_id}/subscribers/{entity_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            BlocklistsUnsubscribeBlocklistPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.delete(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    
    def share_blocklist(
        self,
        request: BlocklistShareRequest,
        blocklist_id: str,
    ):
        endpoint_url = "/blocklists/{blocklist_id}/shares"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            BlocklistsShareBlocklistPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.post(
            url=endpoint_url, path_params=path_params, params=params, headers=headers, json=json.loads(
                request.model_dump_json(
                    exclude_none=True
                )
            )
        )
        
        return None
    
    def unshare_blocklist(
        self,
        blocklist_id: str,
        unshare_organization_id: str,
    ):
        endpoint_url = "/blocklists/{blocklist_id}/shares/{unshare_organization_id}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            BlocklistsUnshareBlocklistPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.delete(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    