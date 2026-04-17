

# Metrics Methods
| Method | Description |
| ------ | ----------- |
| [get_metrics_remediation](#get_metrics_remediation) | Get remediation metrics |

## **get_metrics_remediation**
### Get remediation metrics 
- Endpoint: `/metrics/remediation`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| start_date | str | Start date of the metrics, default to last day | False |  |
| end_date | str | End date of the metrics | False |  |
| engine_ids | list[str] | List of engine ids | False | [] |
| integration_ids | list[str] | List of integration ids | False | [] |
| tags | list[str] | List of tags | False | [] |
### Returns:
[GetRemediationMetricsResponse](./Models.md#getremediationmetricsresponse)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Metrics,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Metrics(auth=auth)
try:
    response = client.get_metrics_remediation(
        start_date='start_date',
        end_date='end_date',
        engine_ids=['sample-item'],
        integration_ids=['sample-item'],
        tags=['sample-item'],
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```

