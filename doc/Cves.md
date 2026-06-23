

# Cves Methods
| Method | Description |
| ------ | ----------- |
| [get_cves](#get_cves) | Get a paginated list of CVEs that CrowdSec is tracking. Pass detailed=true to also include the heavy detail fields (description, crowdsec_analysis, cwes, references, events, tags) for each CVE; they are omitted by default to keep the list light. |
| [get_cve](#get_cve) | Get information about a specific CVE ID |
| [get_cve_protect_rules](#get_cve_protect_rules) | Get protection/detection rules associated with a specific CVE ID |
| [download_cve_ips](#download_cve_ips) | Download the list of IPs exploiting a specific CVE ID in raw format |
| [get_cve_ips_details](#get_cve_ips_details) | Get detailed information about IPs exploiting a specific CVE ID |
| [get_cve_ips_details_stats](#get_cve_ips_details_stats) | Get aggregated statistics about IPs exploiting a specific CVE ID |
| [get_cve_subscribed_integrations](#get_cve_subscribed_integrations) | Get the list of integrations subscribed to a specific CVE ID |
| [subscribe_integration_to_cve](#subscribe_integration_to_cve) | Subscribe an integration to receive threats related to a specific CVE ID |
| [unsubscribe_integration_from_cve](#unsubscribe_integration_from_cve) | Unsubscribe an integration from receiving threats related to a specific CVE ID |
| [get_cve_indicators](#get_cve_indicators) | Get the top indicators (e.g. http_path) observed for a specific CVE ID. Each item is tagged with its ``indicator_type``. The list is pre-ranked by ``sort_by`` (popular = most reported, most_recent = newly discovered variations). Pass ``indicator_type`` one or more times to narrow to specific IOC types. |
| [get_cve_timeline](#get_cve_timeline) | Get timeline data of occurrences for a specific CVE ID |

## **get_cves**
### Get a paginated list of CVEs that CrowdSec is tracking. Pass detailed=true to also include the heavy detail fields (description, crowdsec_analysis, cwes, references, events, tags) for each CVE; they are omitted by default to keep the list light. 
- Endpoint: `/cves`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| query | Optional[str] | Search query for CVEs | False | None |
| sort_by | Optional[GetCVEsSortBy] | Field to sort by | False | GetCVEsSortBy("rule_release_date") |
| sort_order | Optional[GetCVEsSortOrder] | Sort order: ascending or descending | False | GetCVEsSortOrder("desc") |
| exploitation_phase | Optional[CVEExploitationPhase] | Filter by exploitation phase | False | None |
| detailed | bool | Include the heavy detail fields (description, crowdsec_analysis, cwes, references, events, tags) for each CVE in the list. Defaults to false to keep the response lightweight. | False | False |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[GetCVEsResponsePage](./Models.md#getcvesresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Cves,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Cves(auth=auth)
try:
    response = client.get_cves(
        query=None,
        sort_by=rule_release_date,
        sort_order=desc,
        exploitation_phase=None,
        detailed=True,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_cve**
### Get information about a specific CVE ID 
- Endpoint: `/cves/{cve_id}`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| cve_id | str |  | True |  |
### Returns:
[GetCVEResponse](./Models.md#getcveresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | CVE Not Found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Cves,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Cves(auth=auth)
try:
    response = client.get_cve(
        cve_id='cve_id',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_cve_protect_rules**
### Get protection/detection rules associated with a specific CVE ID 
- Endpoint: `/cves/{cve_id}/protect-rules`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| cve_id | str |  | True |  |
### Returns:
[GetCVEProtectRulesResponse](./Models.md#getcveprotectrulesresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | CVE Not Found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Cves,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Cves(auth=auth)
try:
    response = client.get_cve_protect_rules(
        cve_id='cve_id',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **download_cve_ips**
### Download the list of IPs exploiting a specific CVE ID in raw format 
- Endpoint: `/cves/{cve_id}/ips-download`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| cve_id | str |  | True |  |
### Returns:
[str](./Models.md#str)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | CVE Not Found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Cves,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Cves(auth=auth)
try:
    response = client.download_cve_ips(
        cve_id='cve_id',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_cve_ips_details**
### Get detailed information about IPs exploiting a specific CVE ID 
- Endpoint: `/cves/{cve_id}/ips-details`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| cve_id | str |  | True |  |
| since | Optional[str] | Filter IPs seen since this date, format duration (e.g., 7d, 24h), default to 14d | False | "14d" |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[GetCVEIPsResponsePage](./Models.md#getcveipsresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | CVE Not Found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Cves,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Cves(auth=auth)
try:
    response = client.get_cve_ips_details(
        cve_id='cve_id',
        since=14d,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_cve_ips_details_stats**
### Get aggregated statistics about IPs exploiting a specific CVE ID 
- Endpoint: `/cves/{cve_id}/ips-details-stats`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| cve_id | str |  | True |  |
| since | Optional[str] | Filter IPs seen since this date, format duration (e.g., 7d, 24h), default to 14d | False | "14d" |
### Returns:
[IpsDetailsStats](./Models.md#ipsdetailsstats)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | CVE Not Found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Cves,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Cves(auth=auth)
try:
    response = client.get_cve_ips_details_stats(
        cve_id='cve_id',
        since=14d,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_cve_subscribed_integrations**
### Get the list of integrations subscribed to a specific CVE ID 
- Endpoint: `/cves/{cve_id}/integrations`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| cve_id | str |  | True |  |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[GetCVESubscribedIntegrationsResponsePage](./Models.md#getcvesubscribedintegrationsresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | CVE Not Found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Cves,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Cves(auth=auth)
try:
    response = client.get_cve_subscribed_integrations(
        cve_id='cve_id',
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **subscribe_integration_to_cve**
### Subscribe an integration to receive threats related to a specific CVE ID 
- Endpoint: `/cves/{cve_id}/integrations`
- Method: `POST`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [SubscribeCVEIntegrationRequest](./Models.md#subscribecveintegrationrequest) | Request body | Yes | - |
| cve_id | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Integration Not Found |
| 400 | CVE Already Subscribed |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Cves,
    ApiKeyAuth,
    SubscribeCVEIntegrationRequest,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Cves(auth=auth)
request = SubscribeCVEIntegrationRequest(
        name=None,
)
try:
    response = client.subscribe_integration_to_cve(
        request=request,
        cve_id='cve_id',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **unsubscribe_integration_from_cve**
### Unsubscribe an integration from receiving threats related to a specific CVE ID 
- Endpoint: `/cves/{cve_id}/integrations/{integration_name}`
- Method: `DELETE`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| cve_id | str |  | True |  |
| integration_name | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Integration Not Found |
| 400 | CVE Already Unsubscribed |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Cves,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Cves(auth=auth)
try:
    response = client.unsubscribe_integration_from_cve(
        cve_id='cve_id',
        integration_name='integration_name',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_cve_indicators**
### Get the top indicators (e.g. http_path) observed for a specific CVE ID. Each item is tagged with its ``indicator_type``. The list is pre-ranked by ``sort_by`` (popular = most reported, most_recent = newly discovered variations). Pass ``indicator_type`` one or more times to narrow to specific IOC types. 
- Endpoint: `/cves/{cve_id}/indicators`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| cve_id | str |  | True |  |
| sort_by | IndicatorsSortBy | Ranking applied to the returned list. | False |  |
| indicator_type | Optional[list[IndicatorType]] | Restrict to one or more IOC types. | False | None |
### Returns:
[list[IndicatorHttpPath]](./Models.md#list[indicatorhttppath])
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | CVE Not Found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Cves,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Cves(auth=auth)
try:
    response = client.get_cve_indicators(
        cve_id='cve_id',
        sort_by=None,
        indicator_type=None,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_cve_timeline**
### Get timeline data of occurrences for a specific CVE ID 
- Endpoint: `/cves/{cve_id}/timeline`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| cve_id | str |  | True |  |
| since_days | SinceOptions | Time range for the timeline data (in days). Options: 1 (1 day), 7 (1 week), 30 (1 month). Default is 7 days. | False |  |
### Returns:
[list[TimelineItem]](./Models.md#list[timelineitem])
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | CVE Not Found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Cves,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Cves(auth=auth)
try:
    response = client.get_cve_timeline(
        cve_id='cve_id',
        since_days=None,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```

