

# Integrations Methods
| Method | Description |
| ------ | ----------- |
| [get_integrations](#get_integrations) | Get integrations owned by your organization |
| [create_integration](#create_integration) | Create an integration to a firewall or remediation component, owned by your organization. The name should be unique within the organization. This operation is submitted to quotas. |
| [get_integration](#get_integration) | Get an integration by ID |
| [delete_integration](#delete_integration) | Delete the integration by ID |
| [update_integration](#update_integration) | Update the integration details |
| [get_integration_content](#get_integration_content) | Get the ips associated to the integration in plain text format. The content can be paginated to accomodate limits in firewalls. |
| [head_integration_content](#head_integration_content) | Check if the integration has content |
| [get_integration_content_stream](#get_integration_content_stream) | Get the ips associated to the integration in a format compatible with a remediation component. As for the remediation components, you can fetch the full content with startup=true or only the changes since the last pull |

## **get_integrations**
### Get integrations owned by your organization 
- Endpoint: `/integrations`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| tag | Optional[list[str]] | List of tags associated with the integrations (any of) | False | None |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[IntegrationGetResponsePage](./Models.md#integrationgetresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Integrations,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Integrations(auth=auth)
try:
    response = client.get_integrations(
        tag=None,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **create_integration**
### Create an integration to a firewall or remediation component, owned by your organization. The name should be unique within the organization. This operation is submitted to quotas. 
- Endpoint: `/integrations`
- Method: `POST`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [IntegrationCreateRequest](./Models.md#integrationcreaterequest) | Request body | Yes | - |
### Returns:
[IntegrationCreateResponse](./Models.md#integrationcreateresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Integrations,
    ApiKeyAuth,
    IntegrationCreateRequest,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Integrations(auth=auth)
request = IntegrationCreateRequest(
        name=None,
        description=None,
        entity_type=None,
        output_format=None,
        pull_limit=None,
        enable_ip_aggregation=None,
)
try:
    response = client.create_integration(
        request=request,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_integration**
### Get an integration by ID 
- Endpoint: `/integrations/{integration_id}`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| integration_id | str |  | True |  |
### Returns:
[IntegrationGetResponse](./Models.md#integrationgetresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Integrations,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Integrations(auth=auth)
try:
    response = client.get_integration(
        integration_id='integration_id',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **delete_integration**
### Delete the integration by ID 
- Endpoint: `/integrations/{integration_id}`
- Method: `DELETE`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| integration_id | str |  | True |  |
| force | bool | Force delete the integration even if it has active subscriptions (it will unsubscribe from all lists) | False | False |
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Integrations,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Integrations(auth=auth)
try:
    response = client.delete_integration(
        integration_id='integration_id',
        force=True,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **update_integration**
### Update the integration details 
- Endpoint: `/integrations/{integration_id}`
- Method: `PATCH`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [IntegrationUpdateRequest](./Models.md#integrationupdaterequest) | Request body | Yes | - |
| integration_id | str |  | True |  |
### Returns:
[IntegrationUpdateResponse](./Models.md#integrationupdateresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Integrations,
    ApiKeyAuth,
    IntegrationUpdateRequest,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Integrations(auth=auth)
request = IntegrationUpdateRequest(
        name=None,
        description=None,
        output_format=None,
        regenerate_credentials=None,
        pull_limit=None,
        enable_ip_aggregation=None,
)
try:
    response = client.update_integration(
        request=request,
        integration_id='integration_id',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_integration_content**
### Get the ips associated to the integration in plain text format. The content can be paginated to accomodate limits in firewalls. 
- Endpoint: `/integrations/{integration_id}/content`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| integration_id | str |  | True |  |
| page | int | Page number to return | False | 1 |
| page_size | Optional[int] | Maximum number of items to return, 0 means no limit (default), should be greater than 10000 | False | None |
| pull_limit | Optional[int] |  | False | None |
| enable_ip_aggregation | bool |  | False | False |
### Returns:
[str](./Models.md#str)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Integration not found |
| 204 | Integration has no subscribed blocklists or no content available |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Integrations,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Integrations(auth=auth)
try:
    response = client.get_integration_content(
        integration_id='integration_id',
        page=1,
        page_size=None,
        pull_limit=None,
        enable_ip_aggregation=True,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **head_integration_content**
### Check if the integration has content 
- Endpoint: `/integrations/{integration_id}/content`
- Method: `HEAD`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| integration_id | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Integration not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Integrations,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Integrations(auth=auth)
try:
    response = client.head_integration_content(
        integration_id='integration_id',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_integration_content_stream**
### Get the ips associated to the integration in a format compatible with a remediation component. As for the remediation components, you can fetch the full content with startup=true or only the changes since the last pull 
- Endpoint: `/integrations/{integration_id}/v1/decisions/stream`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| integration_id | str |  | True |  |
| startup | bool | Set to true if it's the first run to fetch all the content, otherwise only changes since the last pull. | False | False |
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Integration not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Integrations,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Integrations(auth=auth)
try:
    response = client.get_integration_content_stream(
        integration_id='integration_id',
        startup=True,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```

