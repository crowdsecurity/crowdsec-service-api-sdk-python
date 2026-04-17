

# TrackerTags Methods
| Method | Description |
| ------ | ----------- |
| [get_tags](#get_tags) | Get a paginated list of tags |
| [get_tag_impact](#get_tag_impact) | Get CVE and fingerprint rules affecting a tag |
| [get_tracker_tags](#get_tracker_tags) | Get a paginated list of tracker tags |
| [get_tracker_tag_impact](#get_tracker_tag_impact) | Get CVE and fingerprint rules affecting a tracker tag |

## **get_tags**
### Get a paginated list of tags 
- Endpoint: `/tags`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| query | Optional[str] | Search query for tags | False | None |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[LookupListWithStatsResponsePage](./Models.md#lookuplistwithstatsresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    TrackerTags,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = TrackerTags(auth=auth)
try:
    response = client.get_tags(
        query=None,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_tag_impact**
### Get CVE and fingerprint rules affecting a tag 
- Endpoint: `/tags/{tag}`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| tag | str |  | True |  |
| sort_by | Optional[GetCVEsSortBy] | Field to sort by | False | GetCVEsSortBy("rule_release_date") |
| sort_order | Optional[GetCVEsSortOrder] | Sort order: ascending or descending | False | GetCVEsSortOrder("desc") |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[LookupImpactResponsePage](./Models.md#lookupimpactresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    TrackerTags,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = TrackerTags(auth=auth)
try:
    response = client.get_tag_impact(
        tag='tag',
        sort_by=rule_release_date,
        sort_order=desc,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_tracker_tags**
### Get a paginated list of tracker tags 
- Endpoint: `/tracker-tags`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| query | Optional[str] | Search query for tags | False | None |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[LookupListWithStatsResponsePage](./Models.md#lookuplistwithstatsresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    TrackerTags,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = TrackerTags(auth=auth)
try:
    response = client.get_tracker_tags(
        query=None,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_tracker_tag_impact**
### Get CVE and fingerprint rules affecting a tracker tag 
- Endpoint: `/tracker-tags/{tag}`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| tag | str |  | True |  |
| sort_by | Optional[GetCVEsSortBy] | Field to sort by | False | GetCVEsSortBy("rule_release_date") |
| sort_order | Optional[GetCVEsSortOrder] | Sort order: ascending or descending | False | GetCVEsSortOrder("desc") |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[LookupImpactResponsePage](./Models.md#lookupimpactresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    TrackerTags,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = TrackerTags(auth=auth)
try:
    response = client.get_tracker_tag_impact(
        tag='tag',
        sort_by=rule_release_date,
        sort_order=desc,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```

