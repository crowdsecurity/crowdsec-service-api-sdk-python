import json
from types import NoneType
from typing import Optional, Union, Annotated

from ..models import *
from ..base_model import Page, Service
from pydantic import BaseModel, Field
from pydantic.fields import FieldInfo
from httpx import Auth
from ..http_client import HttpClient

class Hub(Service):
    
    def get_index(
        self,
        branch: str,
        tenant: str,
        with_content: bool = False,
    )-> Index:
        endpoint_url = "/hub/index/{tenant}/{branch}/.index.json"
        loc = locals()
        headers = {}
        params = json.loads(
            HubGetIndexQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = json.loads(
            HubGetIndexPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return Index(**response.json())
    
    def get_item_content(
        self,
        item_path: str,
        branch: str,
        tenant: str,
    ):
        endpoint_url = "/hub/index/{tenant}/{branch}/{item_path}"
        loc = locals()
        headers = {}
        params = {}
        path_params = json.loads(
            HubGetItemContentPathParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return None
    