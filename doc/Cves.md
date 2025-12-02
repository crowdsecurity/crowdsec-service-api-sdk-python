

# Cves Methods
| Method | Description |
| ------ | ----------- |
| [get_cve](#get_cve) | Get information about a specific CVE ID |
| [get_cve_ips](#get_cve_ips) | Get information about IPs exploiting a specific CVE ID |
| [subscribe_integration_to_cve](#subscribe_integration_to_cve) | Subscribe an integration to receive threats related to a specific CVE ID |
| [unsubscribe_integration_from_cve](#unsubscribe_integration_from_cve) | Unsubscribe an integration from receiving threats related to a specific CVE ID |

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
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Cves(base_url=Server.production_server.value, auth=auth)
response = client.get_cve(
    cve_id='cve_id',
)
print(response)
```


## **get_cve_ips**
### Get information about IPs exploiting a specific CVE ID 
- Endpoint: `/cves/{cve_id}/ips`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| cve_id | str |  | True |  |
| since | Optional[str] | Filter IPs seen since this date, format duration (e.g., 7d, 24h) | False | None |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[Page[IPItem]](./Models.md#page[ipitem])
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | CVE Not Found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Cves,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Cves(base_url=Server.production_server.value, auth=auth)
response = client.get_cve_ips(
    cve_id='cve_id',
    since=None,
    page=1,
    size=50,
)
print(response)
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
    Server,
    ApiKeyAuth,
    SubscribeCVEIntegrationRequest,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Cves(base_url=Server.production_server.value, auth=auth)
request = SubscribeCVEIntegrationRequest(
        name=None,
)
response = client.subscribe_integration_to_cve(
    request=request,
    cve_id='cve_id',
)
print(response)
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
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Cves(base_url=Server.production_server.value, auth=auth)
response = client.unsubscribe_integration_from_cve(
    cve_id='cve_id',
    integration_name='integration_name',
)
print(response)
```

