

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
### Returns:
[InfoResponse](./Models.md#inforesponse)
### Usage

```python
from crowdsec_service_api import (
    Info,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Info(auth=auth)
try:
    response = client.get_info(
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```

