

# Hub Methods
| Method | Description |
| ------ | ----------- |
| [get_index](#get_index) | Get a (minimized) index file for 'cscli hub update'. May or may not include unused fields
(content, long descriptions, labels...) or redundant ones (author, name). |
| [head_index](#head_index) | This endpoint returns cache-related headers for the index file without the full content. 
It is useful for validating cache, checking resource freshness, and managing client-side 
cache expiration policies. No body content is returned. |
| [get_item_content](#get_item_content) | Get an item's content from its path. This is usually a YAML file. |
| [head_item_content](#head_item_content) | This endpoint returns cache-related headers for an item's content. It is useful for validating 
cache, checking resource freshness, and managing client-side cache expiration policies. No body 
content is returned. |

## **get_index**
### Get a (minimized) index file for 'cscli hub update'. May or may not include unused fields
(content, long descriptions, labels...) or redundant ones (author, name). 
- Endpoint: `/hub/index/{tenant}/{branch}/.index.json`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| branch | str |  | True |  |
| tenant | str |  | True |  |
| with_content | bool | Include content in the index | False | False |
### Returns:
[Index](./Models.md#index)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Hub,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Hub(base_url=Server.production_server.value, auth=auth)
response = client.get_index(
    branch='branch',
    tenant='tenant',
    with_content=True,
)
print(response)
```


## **head_index**
### This endpoint returns cache-related headers for the index file without the full content. 
It is useful for validating cache, checking resource freshness, and managing client-side 
cache expiration policies. No body content is returned. 
- Endpoint: `/hub/index/{tenant}/{branch}/.index.json`
- Method: `HEAD`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| branch | str |  | True |  |
| tenant | str |  | True |  |
| with_content | bool | Include content in the index | False | False |
### Returns:
[Index](./Models.md#index)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Hub,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Hub(base_url=Server.production_server.value, auth=auth)
response = client.head_index(
    branch='branch',
    tenant='tenant',
    with_content=True,
)
print(response)
```


## **get_item_content**
### Get an item's content from its path. This is usually a YAML file. 
- Endpoint: `/hub/index/{tenant}/{branch}/{item_path}`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| item_path | str |  | True |  |
| branch | str |  | True |  |
| tenant | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | No content field |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Hub,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Hub(base_url=Server.production_server.value, auth=auth)
response = client.get_item_content(
    item_path='item_path',
    branch='branch',
    tenant='tenant',
)
print(response)
```


## **head_item_content**
### This endpoint returns cache-related headers for an item's content. It is useful for validating 
cache, checking resource freshness, and managing client-side cache expiration policies. No body 
content is returned. 
- Endpoint: `/hub/index/{tenant}/{branch}/{item_path}`
- Method: `HEAD`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| item_path | str |  | True |  |
| branch | str |  | True |  |
| tenant | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Hub,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Hub(base_url=Server.production_server.value, auth=auth)
response = client.head_item_content(
    item_path='item_path',
    branch='branch',
    tenant='tenant',
)
print(response)
```

