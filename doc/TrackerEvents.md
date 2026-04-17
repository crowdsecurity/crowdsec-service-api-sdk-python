

# TrackerEvents Methods
| Method | Description |
| ------ | ----------- |
| [get_exploitation_phase_change_events](#get_exploitation_phase_change_events) | Get a paginated list of exploitation phase change events across tracked CVEs |

## **get_exploitation_phase_change_events**
### Get a paginated list of exploitation phase change events across tracked CVEs 
- Endpoint: `/tracker-events/exploitation-phase-change`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| since | str | Duration string (e.g. '30d', '24h') to filter events | False | "30d" |
| sort_order | Optional[GetCVEsSortOrder] | Sort order: ascending or descending | False | GetCVEsSortOrder("desc") |
| cve_id | Optional[str] | Filter by CVE identifier (exact match) | False | None |
| previous_phase | Optional[CVEExploitationPhase] | Filter by previous exploitation phase name | False | None |
| new_phase | Optional[CVEExploitationPhase] | Filter by new exploitation phase name | False | None |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[ExploitationPhaseChangeEventsResponsePage](./Models.md#exploitationphasechangeeventsresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    TrackerEvents,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = TrackerEvents(auth=auth)
try:
    response = client.get_exploitation_phase_change_events(
        since=30d,
        sort_order=desc,
        cve_id=None,
        previous_phase=None,
        new_phase=None,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```

