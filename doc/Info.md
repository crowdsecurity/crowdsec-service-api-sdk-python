

# Info Methods
| Method | Description |
| ------ | ----------- |
| [get_info](#get_info) | Get the current user and organization informations |

## **get_info**
### Get the current user and organization informations 
- Endpoint: `/info`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
### Usage

```python
from crowdsec_service_api import (
    Info,
    Server,
    ApiKeyAuth,
)
auth = ApiKeyAuth(api_key='your_api_key')
client = Info(base_url=Server.production_server.value, auth=auth)
response = client.get_info(
)
print(response)
```

