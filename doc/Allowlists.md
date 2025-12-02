

# Allowlists Methods
| Method | Description |
| ------ | ----------- |
| [list_allowlists](#list_allowlists) | List all allowlists for an organization |
| [create_allowlist](#create_allowlist) | Create a new allowlist for an organization |
| [get_allowlist](#get_allowlist) | Get an allowlist by ID |
| [delete_allowlist](#delete_allowlist) | Delete an allowlist by ID |
| [update_allowlist](#update_allowlist) | Update an allowlist by ID |
| [get_allowlist_items](#get_allowlist_items) | Get items in an allowlist |
| [create_allowlist_items](#create_allowlist_items) | Create items for an allowlist |
| [get_allowlist_item](#get_allowlist_item) | Get an allowlist item by ID |
| [delete_allowlist_item](#delete_allowlist_item) | Delete an allowlist item by ID |
| [update_allowlist_item](#update_allowlist_item) | Update an allowlist item by ID |
| [get_allowlist_subscribers](#get_allowlist_subscribers) | Get subscribers of an allowlist |
| [subscribe_allowlist](#subscribe_allowlist) | Subscribe to an allowlist |
| [unsubscribe_allowlist](#unsubscribe_allowlist) | Unsubscribe from an allowlist |

## **list_allowlists**
### List all allowlists for an organization 
- Endpoint: `/allowlists`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[AllowlistGetResponsePage](./Models.md#allowlistgetresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Allowlists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Allowlists(base_url=Server.production_server.value, auth=auth)
response = client.list_allowlists(
    page=1,
    size=50,
)
print(response)
```


## **create_allowlist**
### Create a new allowlist for an organization 
- Endpoint: `/allowlists`
- Method: `POST`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [AllowlistCreateRequest](./Models.md#allowlistcreaterequest) | Request body | Yes | - |
### Returns:
[AllowlistCreateResponse](./Models.md#allowlistcreateresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Allowlists,
    Server,
    ApiKeyAuth,
    AllowlistCreateRequest,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Allowlists(base_url=Server.production_server.value, auth=auth)
request = AllowlistCreateRequest(
        name=None,
        description=None,
)
response = client.create_allowlist(
    request=request,
)
print(response)
```


## **get_allowlist**
### Get an allowlist by ID 
- Endpoint: `/allowlists/{allowlist_id}`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| allowlist_id | str |  | True |  |
### Returns:
[AllowlistGetResponse](./Models.md#allowlistgetresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Allowlist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Allowlists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Allowlists(base_url=Server.production_server.value, auth=auth)
response = client.get_allowlist(
    allowlist_id='allowlist_id',
)
print(response)
```


## **delete_allowlist**
### Delete an allowlist by ID 
- Endpoint: `/allowlists/{allowlist_id}`
- Method: `DELETE`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| allowlist_id | str |  | True |  |
| force | bool | Force delete the allowlist, even if it has subscribers | False | False |
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Allowlist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Allowlists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Allowlists(base_url=Server.production_server.value, auth=auth)
response = client.delete_allowlist(
    allowlist_id='allowlist_id',
    force=True,
)
print(response)
```


## **update_allowlist**
### Update an allowlist by ID 
- Endpoint: `/allowlists/{allowlist_id}`
- Method: `PATCH`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [AllowlistUpdateRequest](./Models.md#allowlistupdaterequest) | Request body | Yes | - |
| allowlist_id | str |  | True |  |
### Returns:
[AllowlistUpdateResponse](./Models.md#allowlistupdateresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Allowlist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Allowlists,
    Server,
    ApiKeyAuth,
    AllowlistUpdateRequest,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Allowlists(base_url=Server.production_server.value, auth=auth)
request = AllowlistUpdateRequest(
        name=None,
        description=None,
)
response = client.update_allowlist(
    request=request,
    allowlist_id='allowlist_id',
)
print(response)
```


## **get_allowlist_items**
### Get items in an allowlist 
- Endpoint: `/allowlists/{allowlist_id}/items`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| allowlist_id | str |  | True |  |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[AllowlistGetItemsResponsePage](./Models.md#allowlistgetitemsresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Allowlist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Allowlists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Allowlists(base_url=Server.production_server.value, auth=auth)
response = client.get_allowlist_items(
    allowlist_id='allowlist_id',
    page=1,
    size=50,
)
print(response)
```


## **create_allowlist_items**
### Create items for an allowlist 
- Endpoint: `/allowlists/{allowlist_id}/items`
- Method: `POST`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [AllowlistItemsCreateRequest](./Models.md#allowlistitemscreaterequest) | Request body | Yes | - |
| allowlist_id | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Allowlist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Allowlists,
    Server,
    ApiKeyAuth,
    AllowlistItemsCreateRequest,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Allowlists(base_url=Server.production_server.value, auth=auth)
request = AllowlistItemsCreateRequest(
        items=None,
        description=None,
        expiration=None,
)
response = client.create_allowlist_items(
    request=request,
    allowlist_id='allowlist_id',
)
print(response)
```


## **get_allowlist_item**
### Get an allowlist item by ID 
- Endpoint: `/allowlists/{allowlist_id}/items/{item_id}`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| allowlist_id | str |  | True |  |
| item_id | str |  | True |  |
### Returns:
[AllowlistGetItemsResponse](./Models.md#allowlistgetitemsresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Allowlist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Allowlists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Allowlists(base_url=Server.production_server.value, auth=auth)
response = client.get_allowlist_item(
    allowlist_id='allowlist_id',
    item_id='item_id',
)
print(response)
```


## **delete_allowlist_item**
### Delete an allowlist item by ID 
- Endpoint: `/allowlists/{allowlist_id}/items/{item_id}`
- Method: `DELETE`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| allowlist_id | str |  | True |  |
| item_id | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Allowlist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Allowlists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Allowlists(base_url=Server.production_server.value, auth=auth)
response = client.delete_allowlist_item(
    allowlist_id='allowlist_id',
    item_id='item_id',
)
print(response)
```


## **update_allowlist_item**
### Update an allowlist item by ID 
- Endpoint: `/allowlists/{allowlist_id}/items/{item_id}`
- Method: `PATCH`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [AllowlistItemUpdateRequest](./Models.md#allowlistitemupdaterequest) | Request body | Yes | - |
| allowlist_id | str |  | True |  |
| item_id | str |  | True |  |
### Returns:
[AllowlistItemUpdateResponse](./Models.md#allowlistitemupdateresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Allowlist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Allowlists,
    Server,
    ApiKeyAuth,
    AllowlistItemUpdateRequest,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Allowlists(base_url=Server.production_server.value, auth=auth)
request = AllowlistItemUpdateRequest(
        description=None,
        expiration=None,
)
response = client.update_allowlist_item(
    request=request,
    allowlist_id='allowlist_id',
    item_id='item_id',
)
print(response)
```


## **get_allowlist_subscribers**
### Get subscribers of an allowlist 
- Endpoint: `/allowlists/{allowlist_id}/subscribers`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| allowlist_id | str |  | True |  |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[AllowlistSubscriberEntityPage](./Models.md#allowlistsubscriberentitypage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Allowlist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Allowlists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Allowlists(base_url=Server.production_server.value, auth=auth)
response = client.get_allowlist_subscribers(
    allowlist_id='allowlist_id',
    page=1,
    size=50,
)
print(response)
```


## **subscribe_allowlist**
### Subscribe to an allowlist 
- Endpoint: `/allowlists/{allowlist_id}/subscribers`
- Method: `POST`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [AllowlistSubscriptionRequest](./Models.md#allowlistsubscriptionrequest) | Request body | Yes | - |
| allowlist_id | str |  | True |  |
### Returns:
[AllowlistSubscriptionResponse](./Models.md#allowlistsubscriptionresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Allowlist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Allowlists,
    Server,
    ApiKeyAuth,
    AllowlistSubscriptionRequest,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Allowlists(base_url=Server.production_server.value, auth=auth)
request = AllowlistSubscriptionRequest(
        ids=None,
        entity_type=None,
)
response = client.subscribe_allowlist(
    request=request,
    allowlist_id='allowlist_id',
)
print(response)
```


## **unsubscribe_allowlist**
### Unsubscribe from an allowlist 
- Endpoint: `/allowlists/{allowlist_id}/subscribers/{entity_id}`
- Method: `DELETE`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| allowlist_id | str |  | True |  |
| entity_id | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Allowlist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Allowlists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Allowlists(base_url=Server.production_server.value, auth=auth)
response = client.unsubscribe_allowlist(
    allowlist_id='allowlist_id',
    entity_id='entity_id',
)
print(response)
```

