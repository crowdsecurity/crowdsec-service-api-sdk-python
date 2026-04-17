

# Vendors Methods
| Method | Description |
| ------ | ----------- |
| [get_vendors](#get_vendors) | Get a paginated list of vendors |
| [get_vendor_stats](#get_vendor_stats) | Get statistics for a vendor including CVE/fingerprint counts, IP counts, and top affected products |
| [download_vendor_ips](#download_vendor_ips) | Download the list of IPs exploiting a specific vendor in raw format |
| [get_vendor_ips_details](#get_vendor_ips_details) | Get detailed information about IPs exploiting a specific vendor |
| [get_vendor_ips_details_stats](#get_vendor_ips_details_stats) | Get aggregated statistics about IPs exploiting a specific vendor |
| [get_vendor_subscribed_integrations](#get_vendor_subscribed_integrations) | Get the list of integrations subscribed to a specific vendor |
| [subscribe_integration_to_vendor](#subscribe_integration_to_vendor) | Subscribe an integration to receive threats related to a specific vendor |
| [unsubscribe_integration_from_vendor](#unsubscribe_integration_from_vendor) | Unsubscribe an integration from receiving threats related to a specific vendor |
| [get_vendor_impact](#get_vendor_impact) | Get CVE and fingerprint rules affecting a vendor |

## **get_vendors**
### Get a paginated list of vendors 
- Endpoint: `/vendors`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| query | Optional[str] | Search query for vendors | False | None |
| sort_by | Optional[VendorSortBy] | Sort by: value, nb_cves, nb_ips, latest_rule_release | False | None |
| sort_order | Optional[GetCVEsSortOrder] | Sort order: asc or desc | False | GetCVEsSortOrder("desc") |
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
    Vendors,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Vendors(auth=auth)
try:
    response = client.get_vendors(
        query=None,
        sort_by=None,
        sort_order=desc,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_vendor_stats**
### Get statistics for a vendor including CVE/fingerprint counts, IP counts, and top affected products 
- Endpoint: `/vendors/{vendor}/stats`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| vendor | str |  | True |  |
### Returns:
[VendorStatsResponse](./Models.md#vendorstatsresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Vendors,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Vendors(auth=auth)
try:
    response = client.get_vendor_stats(
        vendor='vendor',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **download_vendor_ips**
### Download the list of IPs exploiting a specific vendor in raw format 
- Endpoint: `/vendors/{vendor}/ips-download`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| vendor | str |  | True |  |
### Returns:
[str](./Models.md#str)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Vendors,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Vendors(auth=auth)
try:
    response = client.download_vendor_ips(
        vendor='vendor',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_vendor_ips_details**
### Get detailed information about IPs exploiting a specific vendor 
- Endpoint: `/vendors/{vendor}/ips-details`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| vendor | str |  | True |  |
| since | Optional[str] | Filter IPs seen since this date, format duration (e.g., 7d, 24h), default to 14d | False | "14d" |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[GetVendorIPsResponsePage](./Models.md#getvendoripsresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Vendors,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Vendors(auth=auth)
try:
    response = client.get_vendor_ips_details(
        vendor='vendor',
        since=14d,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_vendor_ips_details_stats**
### Get aggregated statistics about IPs exploiting a specific vendor 
- Endpoint: `/vendors/{vendor}/ips-details-stats`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| vendor | str |  | True |  |
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
    Vendors,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Vendors(auth=auth)
try:
    response = client.get_vendor_ips_details_stats(
        vendor='vendor',
        since=14d,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_vendor_subscribed_integrations**
### Get the list of integrations subscribed to a specific vendor 
- Endpoint: `/vendors/{vendor}/integrations`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| vendor | str |  | True |  |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[GetVendorSubscribedIntegrationsResponsePage](./Models.md#getvendorsubscribedintegrationsresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Vendors,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Vendors(auth=auth)
try:
    response = client.get_vendor_subscribed_integrations(
        vendor='vendor',
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **subscribe_integration_to_vendor**
### Subscribe an integration to receive threats related to a specific vendor 
- Endpoint: `/vendors/{vendor}/integrations`
- Method: `POST`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [SubscribeVendorIntegrationRequest](./Models.md#subscribevendorintegrationrequest) | Request body | Yes | - |
| vendor | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Vendors,
    ApiKeyAuth,
    SubscribeVendorIntegrationRequest,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Vendors(auth=auth)
request = SubscribeVendorIntegrationRequest(
        name=None,
)
try:
    response = client.subscribe_integration_to_vendor(
        request=request,
        vendor='vendor',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **unsubscribe_integration_from_vendor**
### Unsubscribe an integration from receiving threats related to a specific vendor 
- Endpoint: `/vendors/{vendor}/integrations/{integration_name}`
- Method: `DELETE`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| vendor | str |  | True |  |
| integration_name | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Vendors,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Vendors(auth=auth)
try:
    response = client.unsubscribe_integration_from_vendor(
        vendor='vendor',
        integration_name='integration_name',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_vendor_impact**
### Get CVE and fingerprint rules affecting a vendor 
- Endpoint: `/vendors/{vendor}`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| vendor | str |  | True |  |
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
    Vendors,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Vendors(auth=auth)
try:
    response = client.get_vendor_impact(
        vendor='vendor',
        sort_by=rule_release_date,
        sort_order=desc,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```

