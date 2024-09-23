

# Blocklists Methods
| Method | Description |
| ------ | ----------- |
| [get_blocklists](#get_blocklists) | Get multiple blocklists. Only blocklists owned by your organization, shared with your organization or public blocklists are returned. Filters and pagination are available as query parameters. |
| [create_blocklist](#create_blocklist) | Create a new blocklist owned by your organization. The name must be unique within your organization. The list will only be visible to your organization and organizations you shared the blocklist with. This operation is submitted to quotas |
| [search_blocklist](#search_blocklist) | Search blocklists |
| [get_blocklist](#get_blocklist) | Get the details of a blocklist by ID. The content of the blocklist is not returned. |
| [delete_blocklist](#delete_blocklist) | Delete a blocklist by ID. If the blocklist is shared with other organizations or it has subscriptions, the operation will fail. If you want to force delete the blocklist, you can use the force query parameter, so the blocklists will be unshared / unsubscribed. |
| [update_blocklist](#update_blocklist) | Update a blocklist's details by ID. It is not possible to update the blocklist content using this operation. |
| [add_ips_to_blocklist](#add_ips_to_blocklist) | Add IPs to a blocklist. If an IP is already in the blocklist, its expiration will be updated with the new expiration. |
| [delete_ips_from_blocklist](#delete_ips_from_blocklist) | Delete IPs from a blocklist |
| [download_blocklist_content](#download_blocklist_content) | Download blocklist content as a list of ips as plain text separated by new lines. The response will include the ETag header for cache control. If_Modified_Since and If_None_Match cache control headers are supported for conditional requests. |
| [get_blocklist_subscribers](#get_blocklist_subscribers) | Get blocklist subscribers within your organization. |
| [subscribe_blocklist](#subscribe_blocklist) | Subscribe to a blocklist with a remediation type. If the entity type is the full organization or a Tag, all the engines belonging to the organization or the Tag will be subscribed and new engines that will join the organization or the Tag will also be automatically subscribed. If the subscription has been done on an organization or Tag you cannot unsubscribe individual engines. In case of errors for some subscribers, the operation will still succeed for the entities that were successfully subscribed and you'll have the list of errors in the operation's result. This operation is submitted to quotas. |
| [unsubscribe_blocklist](#unsubscribe_blocklist) | Unsubscribe from a blocklist. You cannot unsubscribe individual engines if the subscription has been done on an organization or Tag. |
| [share_blocklist](#share_blocklist) | Share a blocklist with other organizations given their IDs. The blocklist must be owned by your organization. You can give read-only access or read-write access to the blocklist. Sharing a blocklist will not automatically subscribe the shared organizations to the blocklist. |
| [unshare_blocklist](#unshare_blocklist) | Unshare a blocklist with other organizations. If the blocklist is subscribed by the organization, the operation will fail.Use force query parameter to unshare a blocklist even if subscriptions exists. |

## **get_blocklists**
### Get multiple blocklists. Only blocklists owned by your organization, shared with your organization or public blocklists are returned. Filters and pagination are available as query parameters. 
- Endpoint: `/blocklists`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| page | int | Page number | False | 1 |
| page_size | int | Page size | False | 100 |
| subscribed_only | bool | Fetch only blocklists subscribed by your organization, engines or tags | False | False |
| exclude_subscribed | bool | Exclude subscribed blocklists | False | False |
| include_filter | list[BlocklistIncludeFilters] | Include blocklists with the specified filters | False | ['private', 'shared'] |
| size | int | Page size | False | 50 |
### Returns:
[Page[BlocklistResponse]](./Models.md#page[blocklistresponse])
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Blocklists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Blocklists(base_url=Server.production_server.value, auth=auth)
response = client.get_blocklists(
    page=1,
    page_size=100,
    subscribed_only=True,
    exclude_subscribed=True,
    include_filter=['private', 'shared'],
    size=50,
)
print(response)
```


## **create_blocklist**
### Create a new blocklist owned by your organization. The name must be unique within your organization. The list will only be visible to your organization and organizations you shared the blocklist with. This operation is submitted to quotas 
- Endpoint: `/blocklists`
- Method: `POST`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [BlocklistCreateRequest](./Models.md#blocklistcreaterequest) | Request body | Yes | - |
### Returns:
[BlocklistCreateResponse](./Models.md#blocklistcreateresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 409 | Blocklist already exists |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Blocklists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Blocklists(base_url=Server.production_server.value, auth=auth)
request = BlocklistCreateRequest(
        name='name',
        label='label',
        description='description',
        references=['sample-item'],
        tags=['sample-item'],
        from_cti_query='from_cti_query',
        since='since',
)
response = client.create_blocklist(
    request=request,
)
print(response)
```


## **search_blocklist**
### Search blocklists 
- Endpoint: `/blocklists/search`
- Method: `POST`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [BlocklistSearchRequest](./Models.md#blocklistsearchrequest) | Request body | Yes | - |
### Returns:
[PaginatedBlocklistResponse](./Models.md#paginatedblocklistresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Blocklists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Blocklists(base_url=Server.production_server.value, auth=auth)
request = BlocklistSearchRequest(
        page=1,
        page_size=100,
        pricing_tiers=None,
        query='query',
        targeted_countries=['sample-item'],
        classifications=['sample-item'],
        behaviors=['sample-item'],
        min_ips=1,
        sources=None,
        is_private=None,
        is_subscribed=None,
)
response = client.search_blocklist(
    request=request,
)
print(response)
```


## **get_blocklist**
### Get the details of a blocklist by ID. The content of the blocklist is not returned. 
- Endpoint: `/blocklists/{blocklist_id}`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| blocklist_id | str |  | True |  |
### Returns:
[BlocklistGetResponse](./Models.md#blocklistgetresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Blocklist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Blocklists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Blocklists(base_url=Server.production_server.value, auth=auth)
response = client.get_blocklist(
    blocklist_id='sample-blocklist-id',
)
print(response)
```


## **delete_blocklist**
### Delete a blocklist by ID. If the blocklist is shared with other organizations or it has subscriptions, the operation will fail. If you want to force delete the blocklist, you can use the force query parameter, so the blocklists will be unshared / unsubscribed. 
- Endpoint: `/blocklists/{blocklist_id}`
- Method: `DELETE`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| blocklist_id | str |  | True |  |
| force | bool | Force delete the blocklist if it is shared or subscribed | False | False |
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Blocklist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Blocklists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Blocklists(base_url=Server.production_server.value, auth=auth)
response = client.delete_blocklist(
    blocklist_id='sample-blocklist-id',
    force=True,
)
print(response)
```


## **update_blocklist**
### Update a blocklist's details by ID. It is not possible to update the blocklist content using this operation. 
- Endpoint: `/blocklists/{blocklist_id}`
- Method: `PATCH`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [BlocklistUpdateRequest](./Models.md#blocklistupdaterequest) | Request body | Yes | - |
| blocklist_id | str |  | True |  |
### Returns:
[BlocklistResponse](./Models.md#blocklistresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 403 | Blocklist is read-only |
| 404 | Blocklist not found |
| 500 | Internal server error |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Blocklists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Blocklists(base_url=Server.production_server.value, auth=auth)
request = BlocklistUpdateRequest(
        label='label',
        description='description',
        references=['sample-item'],
        tags=['sample-item'],
        from_cti_query='from_cti_query',
        since='since',
)
response = client.update_blocklist(
    request=request,
    blocklist_id='sample-blocklist-id',
)
print(response)
```


## **add_ips_to_blocklist**
### Add IPs to a blocklist. If an IP is already in the blocklist, its expiration will be updated with the new expiration. 
- Endpoint: `/blocklists/{blocklist_id}/ips`
- Method: `POST`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [BlocklistAddIPsRequest](./Models.md#blocklistaddipsrequest) | Request body | Yes | - |
| blocklist_id | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 403 | Blocklist is read-only |
| 404 | Blocklist not found |
| 412 | Payload too large for one operation, limit is 20000 IPs per request |
| 500 | Internal server error |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Blocklists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Blocklists(base_url=Server.production_server.value, auth=auth)
request = BlocklistAddIPsRequest(
        ips=['sample-item'],
        expiration='expiration',
)
response = client.add_ips_to_blocklist(
    request=request,
    blocklist_id='sample-blocklist-id',
)
print(response)
```


## **delete_ips_from_blocklist**
### Delete IPs from a blocklist 
- Endpoint: `/blocklists/{blocklist_id}/ips/delete`
- Method: `POST`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [BlocklistDeleteIPsRequest](./Models.md#blocklistdeleteipsrequest) | Request body | Yes | - |
| blocklist_id | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 403 | Blocklist is read-only |
| 404 | Blocklist not found |
| 500 | Internal server error |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Blocklists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Blocklists(base_url=Server.production_server.value, auth=auth)
request = BlocklistDeleteIPsRequest(
        ips=['sample-item'],
)
response = client.delete_ips_from_blocklist(
    request=request,
    blocklist_id='sample-blocklist-id',
)
print(response)
```


## **download_blocklist_content**
### Download blocklist content as a list of ips as plain text separated by new lines. The response will include the ETag header for cache control. If_Modified_Since and If_None_Match cache control headers are supported for conditional requests. 
- Endpoint: `/blocklists/{blocklist_id}/download`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| blocklist_id | str |  | True |  |
| if_modified_since | Optional[str] | If_Modified_Since cache control header | False | None |
| if_none_match | Optional[str] | If_None_Match cache control header | False | None |
### Returns:
[str](./Models.md#str)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Blocklist not found |
| 204 | Blocklist is empty |
| 500 | Internal server error |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Blocklists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Blocklists(base_url=Server.production_server.value, auth=auth)
response = client.download_blocklist_content(
    blocklist_id='sample-blocklist-id',
    if_modified_since=None,
    if_none_match=None,
)
print(response)
```


## **get_blocklist_subscribers**
### Get blocklist subscribers within your organization. 
- Endpoint: `/blocklists/{blocklist_id}/subscribers`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| blocklist_id | str |  | True |  |
### Returns:
[BlocklistSubscribersResponse](./Models.md#blocklistsubscribersresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Blocklist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Blocklists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Blocklists(base_url=Server.production_server.value, auth=auth)
response = client.get_blocklist_subscribers(
    blocklist_id='sample-blocklist-id',
)
print(response)
```


## **subscribe_blocklist**
### Subscribe to a blocklist with a remediation type. If the entity type is the full organization or a Tag, all the engines belonging to the organization or the Tag will be subscribed and new engines that will join the organization or the Tag will also be automatically subscribed. If the subscription has been done on an organization or Tag you cannot unsubscribe individual engines. In case of errors for some subscribers, the operation will still succeed for the entities that were successfully subscribed and you'll have the list of errors in the operation's result. This operation is submitted to quotas. 
- Endpoint: `/blocklists/{blocklist_id}/subscribers`
- Method: `POST`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [BlocklistSubscriptionRequest](./Models.md#blocklistsubscriptionrequest) | Request body | Yes | - |
| blocklist_id | str |  | True |  |
### Returns:
[BlocklistSubscriptionResponse](./Models.md#blocklistsubscriptionresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Blocklist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Blocklists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Blocklists(base_url=Server.production_server.value, auth=auth)
request = BlocklistSubscriptionRequest(
        ids=['sample-item'],
        entity_type='entity_type',
        remediation=None,
)
response = client.subscribe_blocklist(
    request=request,
    blocklist_id='sample-blocklist-id',
)
print(response)
```


## **unsubscribe_blocklist**
### Unsubscribe from a blocklist. You cannot unsubscribe individual engines if the subscription has been done on an organization or Tag. 
- Endpoint: `/blocklists/{blocklist_id}/subscribers/{entity_id}`
- Method: `DELETE`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| blocklist_id | str |  | True |  |
| entity_id | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Blocklist not found |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Blocklists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Blocklists(base_url=Server.production_server.value, auth=auth)
response = client.unsubscribe_blocklist(
    blocklist_id='sample-blocklist-id',
    entity_id='entity_id',
)
print(response)
```


## **share_blocklist**
### Share a blocklist with other organizations given their IDs. The blocklist must be owned by your organization. You can give read-only access or read-write access to the blocklist. Sharing a blocklist will not automatically subscribe the shared organizations to the blocklist. 
- Endpoint: `/blocklists/{blocklist_id}/shares`
- Method: `POST`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| request | [BlocklistShareRequest](./Models.md#blocklistsharerequest) | Request body | Yes | - |
| blocklist_id | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Blocklist not found |
| 409 | Blocklist is not private |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Blocklists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Blocklists(base_url=Server.production_server.value, auth=auth)
request = BlocklistShareRequest(
        organizations=None,
)
response = client.share_blocklist(
    request=request,
    blocklist_id='sample-blocklist-id',
)
print(response)
```


## **unshare_blocklist**
### Unshare a blocklist with other organizations. If the blocklist is subscribed by the organization, the operation will fail.Use force query parameter to unshare a blocklist even if subscriptions exists. 
- Endpoint: `/blocklists/{blocklist_id}/shares/{unshare_organization_id}`
- Method: `DELETE`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| blocklist_id | str |  | True |  |
| unshare_organization_id | str |  | True |  |
### Errors:
| Code | Description |
| ---- | ----------- |
| 404 | Blocklist not found |
| 409 | Blocklist is not private |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Blocklists,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Blocklists(base_url=Server.production_server.value, auth=auth)
response = client.unshare_blocklist(
    blocklist_id='sample-blocklist-id',
    unshare_organization_id='unshare_organization_id',
)
print(response)
```

