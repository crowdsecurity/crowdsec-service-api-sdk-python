

# Fingerprints Methods
| Method | Description |
| ------ | ----------- |
| [get_fingerprint_rules](#get_fingerprint_rules) | Get a paginated list of fingerprint rules |
| [download_fingerprint_ips](#download_fingerprint_ips) | Download the list of IPs exploiting a specific fingerprint rule in raw format |
| [get_fingerprint_ips_details](#get_fingerprint_ips_details) | Get detailed information about IPs exploiting a specific fingerprint rule |
| [get_fingerprint_ips_details_stats](#get_fingerprint_ips_details_stats) | Get aggregated statistics about IPs exploiting a specific fingerprint rule |
| [get_fingerprint_subscribed_integrations](#get_fingerprint_subscribed_integrations) | Get the list of integrations subscribed to a specific fingerprint rule |
| [subscribe_integration_to_fingerprint](#subscribe_integration_to_fingerprint) | Subscribe an integration to receive threats related to a specific fingerprint rule |
| [unsubscribe_integration_from_fingerprint](#unsubscribe_integration_from_fingerprint) | Unsubscribe an integration from receiving threats related to a specific fingerprint rule |
| [get_fingerprint_timeline](#get_fingerprint_timeline) | Get timeline data of occurrences for a specific fingerprint rule |
| [get_fingerprint_rule](#get_fingerprint_rule) | Get information about a specific fingerprint rule |

## **get_fingerprint_rules**
### Get a paginated list of fingerprint rules 
- Endpoint: `/fingerprints`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| query | Optional[str] | Search query for fingerprint rules | False | None |
| sort_by | Optional[GetCVEsSortBy] | Field to sort by | False | GetCVEsSortBy("rule_release_date") |
| sort_order | Optional[GetCVEsSortOrder] | Sort order: ascending or descending | False | GetCVEsSortOrder("desc") |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[GetFingerprintRulesResponsePage](./Models.md#getfingerprintrulesresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Fingerprints,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Fingerprints(auth=auth)
try:
    response = client.get_fingerprint_rules(
        query=None,
        sort_by=rule_release_date,
        sort_order=desc,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **download_fingerprint_ips**
### Download the list of IPs exploiting a specific fingerprint rule in raw format 
- Endpoint: `/fingerprints/{fingerprint}/ips-download`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| fingerprint | str |  | True |  |
### Returns:
[str](./Models.md#str)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Fingerprints,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Fingerprints(auth=auth)
try:
    response = client.download_fingerprint_ips(
        fingerprint='fingerprint',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_fingerprint_ips_details**
### Get detailed information about IPs exploiting a specific fingerprint rule 
- Endpoint: `/fingerprints/{fingerprint}/ips-details`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| fingerprint | str |  | True |  |
| since | Optional[str] | Filter IPs seen since this date, format duration (e.g., 7d, 24h), default to 14d | False | "14d" |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[GetFingerprintIPsResponsePage](./Models.md#getfingerprintipsresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Fingerprints,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Fingerprints(auth=auth)
try:
    response = client.get_fingerprint_ips_details(
        fingerprint='fingerprint',
        since=14d,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_fingerprint_ips_details_stats**
### Get aggregated statistics about IPs exploiting a specific fingerprint rule 
- Endpoint: `/fingerprints/{fingerprint}/ips-details-stats`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| fingerprint | str |  | True |  |
| since | Optional[str] | Filter IPs seen since this date, format duration (e.g., 7d, 24h), default to 14d | False | "14d" |
### Returns:
[IpsDetailsStats](./Models.md#ipsdetailsstats)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Fingerprints,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Fingerprints(auth=auth)
try:
    response = client.get_fingerprint_ips_details_stats(
        fingerprint='fingerprint',
        since=14d,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_fingerprint_subscribed_integrations**
### Get the list of integrations subscribed to a specific fingerprint rule 
- Endpoint: `/fingerprints/{fingerprint}/integrations`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| fingerprint | str |  | True |  |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[GetFingerprintSubscribedIntegrationsResponsePage](./Models.md#getfingerprintsubscribedintegrationsresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Fingerprints,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Fingerprints(auth=auth)
try:
    response = client.get_fingerprint_subscribed_integrations(
        fingerprint='fingerprint',
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **subscribe_integration_to_fingerprint**
### Subscribe an integration to receive threats related to a specific fingerprint rule 
- Endpoint: `/fingerprints/{fingerprint}/integrations`
- Method: `POST`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [SubscribeFingerprintIntegrationRequest](./Models.md#subscribefingerprintintegrationrequest) | Request body | Yes | - |
| fingerprint | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Fingerprints,
    ApiKeyAuth,
    SubscribeFingerprintIntegrationRequest,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Fingerprints(auth=auth)
request = SubscribeFingerprintIntegrationRequest(
        name=None,
)
try:
    response = client.subscribe_integration_to_fingerprint(
        request=request,
        fingerprint='fingerprint',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **unsubscribe_integration_from_fingerprint**
### Unsubscribe an integration from receiving threats related to a specific fingerprint rule 
- Endpoint: `/fingerprints/{fingerprint}/integrations/{integration_name}`
- Method: `DELETE`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| fingerprint | str |  | True |  |
| integration_name | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Fingerprints,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Fingerprints(auth=auth)
try:
    response = client.unsubscribe_integration_from_fingerprint(
        fingerprint='fingerprint',
        integration_name='integration_name',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_fingerprint_timeline**
### Get timeline data of occurrences for a specific fingerprint rule 
- Endpoint: `/fingerprints/{fingerprint}/timeline`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| fingerprint | str |  | True |  |
| since_days | SinceOptions | Time range for the timeline data (in days). Options: 1 (1 day), 7 (1 week), 30 (1 month). Default is 7 days. | False |  |
| interval | Optional[IntervalOptions] | Interval for aggregating timeline data. Options: 'hour', 'day', 'week'. Default is adapted based on 'since' parameter. | False | None |
### Returns:
[list[FingerprintTimelineItem]](./Models.md#list[fingerprinttimelineitem])
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Fingerprints,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Fingerprints(auth=auth)
try:
    response = client.get_fingerprint_timeline(
        fingerprint='fingerprint',
        since_days=None,
        interval=None,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_fingerprint_rule**
### Get information about a specific fingerprint rule 
- Endpoint: `/fingerprints/{fingerprint}`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| fingerprint | str |  | True |  |
### Returns:
[FingerprintRuleResponse](./Models.md#fingerprintruleresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Fingerprints,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Fingerprints(auth=auth)
try:
    response = client.get_fingerprint_rule(
        fingerprint='fingerprint',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```

