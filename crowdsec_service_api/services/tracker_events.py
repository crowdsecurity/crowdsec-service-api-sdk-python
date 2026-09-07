import json
from types import NoneType
from typing import Optional, Union, Annotated

from ..models import *
from ..base_model import Page, Service
from pydantic import BaseModel, Field
from pydantic.fields import FieldInfo
from httpx import Auth
from ..http_client import HttpClient

class TrackerEvents(Service):
    def __init__(self, auth: Auth, base_url: str = "https://admin.api.crowdsec.net/v1") -> None:
        super().__init__(base_url=base_url, auth=auth, user_agent="crowdsec_service_api/v0.18.8")
    
    def get_exploitation_phase_change_events(
        self,
        since: str = "30d",
        sort_order: Optional[GetCVEsSortOrder] = GetCVEsSortOrder("desc"),
        cve_id: Optional[str] = None,
        previous_phase: Optional[CVEExploitationPhase] = None,
        new_phase: Optional[CVEExploitationPhase] = None,
        page: int = 1,
        size: int = 50,
    )-> ExploitationPhaseChangeEventsResponsePage:
        endpoint_url = "/tracker-events/exploitation-phase-change"
        loc = locals()
        headers = {}
        params = json.loads(
            TrackerEventsGetExploitationPhaseChangeEventsQueryParameters(**loc).model_dump_json(
                exclude_none=True
            )
        )
        path_params = {}
        
        response = self.http_client.get(
            url=endpoint_url, path_params=path_params, params=params, headers=headers
        )
        
        return ExploitationPhaseChangeEventsResponsePage(_client=self, **response.json())
    