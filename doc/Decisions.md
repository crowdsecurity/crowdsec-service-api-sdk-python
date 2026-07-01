

# Decisions Methods
| Method | Description |
| ------ | ----------- |
| [get_decisions](#get_decisions) | Get decisions |
| [create_decision](#create_decision) | Create a new decision. |
| [delete_decision](#delete_decision) | Delete a decision by its UUID. |
| [get_aggregated_decisions](#get_aggregated_decisions) | None |
| [delete_aggregated_decisions](#delete_aggregated_decisions) | Delete one decision by ID |
| [delete_aggregated_decision_item](#delete_aggregated_decision_item) | Delete one decision by ID |

## **get_decisions**
### Get decisions 
- Endpoint: `/decisions`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
| instance_ids | list[str] | Filter decisions by instance IDs | False | [] |
| tag_ids | list[str] | Filter decisions by tag IDs | False | [] |
| remediation_types | list[str] | Filter decisions by remediation types | False | [] |
| ips | list[str] | Filter decisions by IPs (only for IP decisions) | False | [] |
| alert_ids | list[str] | Filter decisions by associated alert IDs | False | [] |
| decision_ids | list[str] | Filter decisions by decision IDs | False | [] |
| created_at_from | Optional[str] | Filter decisions created after this date (inclusive) | False | None |
| sort_by | Optional[DecisionsSortBy] | Field to sort by (e.g., created_at, duration) | False | DecisionsSortBy("created_at") |
| sort_order | Optional[DecisionsSortOrder] | Sort order: 'asc' for ascending, 'desc' for descending | False | DecisionsSortOrder("desc") |
### Returns:
[DecisionsGetResponsePage](./Models.md#decisionsgetresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Not found |
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
        page=1,
        size=50,
        instance_ids=['sample-item'],
        tag_ids=['sample-item'],
        remediation_types=['sample-item'],
        ips=['sample-item'],
        alert_ids=['sample-item'],
        decision_ids=['sample-item'],
        created_at_from=None,
        sort_by=created_at,
        sort_order=desc,
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
| 409 | Already exists |
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
| 422 | Unprocessable entity |
| 404 | Not found |
| 500 | Internal server error |
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


## **get_aggregated_decisions**
### None 
- Endpoint: `/decisions/aggregated`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
| instance_ids | list[str] | Filter decisions by instance IDs | False | [] |
| tag_ids | list[str] | Filter decisions by tag IDs | False | [] |
| remediation_types | list[str] | Filter decisions by remediation types | False | [] |
| ips | list[str] | Filter decisions by IPs (only for IP decisions) | False | [] |
| alert_ids | list[str] | Filter decisions by associated alert IDs | False | [] |
| decision_ids | list[str] | Filter decisions by decision IDs | False | [] |
| created_at_from | Optional[str] | Filter decisions created after this date (inclusive) | False | None |
| sort_by | Optional[AggregatedDecisionsSortBy] | Field to sort by (e.g., created_at, duration) | False | AggregatedDecisionsSortBy("first_created_at") |
| sort_order | Optional[DecisionsSortOrder] | Sort order: 'asc' for ascending, 'desc' for descending | False | DecisionsSortOrder("desc") |
### Returns:
[AggregatedDecisionsGetResponsePage](./Models.md#aggregateddecisionsgetresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Not found |
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
    response = client.get_aggregated_decisions(
        page=1,
        size=50,
        instance_ids=['sample-item'],
        tag_ids=['sample-item'],
        remediation_types=['sample-item'],
        ips=['sample-item'],
        alert_ids=['sample-item'],
        decision_ids=['sample-item'],
        created_at_from=None,
        sort_by=first_created_at,
        sort_order=desc,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **delete_aggregated_decisions**
### Delete one decision by ID 
- Endpoint: `/decisions/aggregated/{aggregated_id}`
- Method: `DELETE`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| aggregated_id | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Unprocessable entity |
| 404 | Not found |
| 500 | Internal server error |
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
    response = client.delete_aggregated_decisions(
        aggregated_id='aggregated_id',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **delete_aggregated_decision_item**
### Delete one decision by ID 
- Endpoint: `/decisions/aggregated/{aggregated_id}/items/{decision_id}`
- Method: `DELETE`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| aggregated_id | str |  | True |  |
| decision_id | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Unprocessable entity |
| 404 | Not found |
| 500 | Internal server error |
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
    response = client.delete_aggregated_decision_item(
        aggregated_id='aggregated_id',
        decision_id='decision_id',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```

