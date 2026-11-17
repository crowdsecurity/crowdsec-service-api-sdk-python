

# Engines Methods
| Method | Description |
| ------ | ----------- |
| [get_engines](#get_engines) | Get engines for an organization |
| [get_engine](#get_engine) | Get an engine for an organization |
| [associate_tags_with_engine](#associate_tags_with_engine) | Associate tags with an engine |
| [disassociate_tags_with_engine](#disassociate_tags_with_engine) | Disassociate tags from an engine |
| [get_engine_log_processors](#get_engine_log_processors) | Get log processors for an engine |
| [get_engine_remediation_components](#get_engine_remediation_components) | Get remediation components for an engine |

## **get_engines**
### Get engines for an organization 
- Endpoint: `/engines`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| tag | Optional[list[str]] | List of tags associated with the engines (any of) | False | None |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[EngineGetResponsePage](./Models.md#enginegetresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Engines,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Engines(auth=auth)
try:
    response = client.get_engines(
        tag=None,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_engine**
### Get an engine for an organization 
- Endpoint: `/engines/{engine_id}`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| engine_id | str |  | True |  |
### Returns:
[EngineGetResponse](./Models.md#enginegetresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Engines,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Engines(auth=auth)
try:
    response = client.get_engine(
        engine_id='engine_id',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **associate_tags_with_engine**
### Associate tags with an engine 
- Endpoint: `/engines/{engine_id}/tags`
- Method: `POST`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [EngineAssociateTagsRequest](./Models.md#engineassociatetagsrequest) | Request body | Yes | - |
| engine_id | str |  | True |  |
### Returns:
[EngineAssociateTagsResponse](./Models.md#engineassociatetagsresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Engines,
    ApiKeyAuth,
    EngineAssociateTagsRequest,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Engines(auth=auth)
request = EngineAssociateTagsRequest(
        tags=None,
)
try:
    response = client.associate_tags_with_engine(
        request=request,
        engine_id='engine_id',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **disassociate_tags_with_engine**
### Disassociate tags from an engine 
- Endpoint: `/engines/{engine_id}/tags/{tag_name}`
- Method: `DELETE`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| engine_id | str |  | True |  |
| tag_name | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Engines,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Engines(auth=auth)
try:
    response = client.disassociate_tags_with_engine(
        engine_id='engine_id',
        tag_name='tag_name',
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_engine_log_processors**
### Get log processors for an engine 
- Endpoint: `/engines/{engine_id}/log_processors`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| engine_id | str |  | True |  |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[LogProcessorsGetResponsePage](./Models.md#logprocessorsgetresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Engines,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Engines(auth=auth)
try:
    response = client.get_engine_log_processors(
        engine_id='engine_id',
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_engine_remediation_components**
### Get remediation components for an engine 
- Endpoint: `/engines/{engine_id}/remediation_components`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| engine_id | str |  | True |  |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[RemediationComponentsGetResponsePage](./Models.md#remediationcomponentsgetresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Engines,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Engines(auth=auth)
try:
    response = client.get_engine_remediation_components(
        engine_id='engine_id',
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```

