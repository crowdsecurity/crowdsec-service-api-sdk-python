import json
from types import NoneType
from typing import Optional, Union, Annotated

from ..models import *
from ..base_model import Page, Service
from pydantic import BaseModel, Field
from pydantic.fields import FieldInfo
from httpx import Auth
from ..http_client import HttpClient

class Metrics(Service):
    
    def get_metrics_remediation(
        self,
        start_date: str,
        end_date: str,
        engine_ids: list[str] = [],
        tags: list[str] = [],
    )-> GetRemediationMetricsResponse:
        endpoint_url = "/metrics/remediation"
        loc = locals()
        headers = {}
        params = json.loads(
            MetricsGetMetricsRemediationQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = {}
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return GetRemediationMetricsResponse(**response.json())
    