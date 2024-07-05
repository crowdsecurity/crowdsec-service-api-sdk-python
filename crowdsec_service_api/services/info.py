import json
from httpx import Auth
from ..models import *
from ..base_model import Page, Service
from ..http_client import HttpClient

class Info(Service):
    
    def get_info(
        self,
    )-> InfoResponse:
        endpoint_url = "/info"
        loc = locals()
        headers = {}
        params = {}
        path_params = {}
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return InfoResponse(**response.json())
    