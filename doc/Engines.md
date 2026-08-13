

# Engines Methods
| Method | Description |
| ------ | ----------- |
| [get_engines](#get_engines) | Get engines for an organization |

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

