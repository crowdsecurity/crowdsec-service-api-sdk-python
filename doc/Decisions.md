

# Decisions Methods
| Method | Description |
| ------ | ----------- |
| [get_decisions](#get_decisions) | Get decisions |
| [create_decision](#create_decision) | Create a new decision. |
| [delete_decision](#delete_decision) | Delete a decision by its UUID. |

## **get_decisions**
### Get decisions 
- Endpoint: `/decisions`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| instance_ids | list[str] | Filter decisions by instance IDs | False | [] |
| tag_ids | list[str] | Filter decisions by tag IDs | False | [] |
| remediation_types | list[str] | Filter decisions by remediation types | False | [] |
| ips | list[str] | Filter decisions by IPs (only for IP decisions) | False | [] |
| sort_by | Optional[DecisionsSortBy] | Field to sort by (e.g., created_at, duration) | False | DecisionsSortBy("created_at") |
| sort_order | Optional[DecisionsSortOrder] | Sort order: 'asc' for ascending, 'desc' for descending | False | DecisionsSortOrder("desc") |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[DecisionsGetResponsePage](./Models.md#decisionsgetresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Not found |
| 500 | Internal server error |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Decisions,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Decisions(auth=auth)
try:
    response = client.get_decisions(
        instance_ids=['sample-item'],
        tag_ids=['sample-item'],
        remediation_types=['sample-item'],
        ips=['sample-item'],
        sort_by=created_at,
        sort_order=desc,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **create_decision**
### Create a new decision. 
- Endpoint: `/decisions`
- Method: `POST`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [DecisionCreateRequest](./Models.md#decisioncreaterequest) | Request body | Yes | - |
### Returns:
[DecisionCreateResponse](./Models.md#decisioncreateresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 409 | Conflict: Decision value is in allowlists; cannot create decision. |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Decisions,
    ApiKeyAuth,
    DecisionCreateRequest,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Decisions(auth=auth)
request = DecisionCreateRequest(
        created_at=None,
        uuid=None,
        id=None,
        duration=None,
        origin=None,
        scenario=None,
        scope=None,
        type=None,
        value=None,
        country=None,
        as_name=None,
        as_num=None,
        city=None,
        latitude=None,
        longitude=None,
        target=None,
)
try:
    response = client.create_decision(
        request=request,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **delete_decision**
### Delete a decision by its UUID. 
- Endpoint: `/decisions/{decision_id}`
- Method: `DELETE`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| decision_id | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Decisions,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Decisions(auth=auth)
try:
    response = client.delete_decision(
        decision_id='decision_id',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```

