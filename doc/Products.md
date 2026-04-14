

# Products Methods
| Method | Description |
| ------ | ----------- |
| [get_products](#get_products) | Get a paginated list of products |
| [get_product_impact](#get_product_impact) | Get CVE and fingerprint rules affecting a product |

## **get_products**
### Get a paginated list of products 
- Endpoint: `/products`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| query | Optional[str] | Search query for products | False | None |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[LookupListWithStatsResponsePage](./Models.md#lookuplistwithstatsresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Products,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Products(auth=auth)
try:
    response = client.get_products(
        query=None,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```


## **get_product_impact**
### Get CVE and fingerprint rules affecting a product 
- Endpoint: `/products/{product}`
- Method: `GET`

### Parameters:
| Parameter | Type | Description | Required | Default |
| --------- | ---- | ----------- | -------- | ------- |
| product | str |  | True |  |
| sort_by | Optional[GetCVEsSortBy] | Field to sort by | False | GetCVEsSortBy("rule_release_date") |
| sort_order | Optional[GetCVEsSortOrder] | Sort order: ascending or descending | False | GetCVEsSortOrder("desc") |
| page | int | Page number | False | 1 |
| size | int | Page size | False | 50 |
### Returns:
[LookupImpactResponsePage](./Models.md#lookupimpactresponsepage)
### Errors:
| Code | Description |
| ---- | ----------- |
| 422 | Validation Error |
### Usage

```python
from crowdsec_service_api import (
    Products,
    ApiKeyAuth,
)
from httpx import HTTPStatusError
auth = ApiKeyAuth(api_key='your_api_key')
client = Products(auth=auth)
try:
    response = client.get_product_impact(
        product='product',
        sort_by=rule_release_date,
        sort_order=desc,
        page=1,
        size=50,
    )
    print(response)
except HTTPStatusError as e:
    print(f"An error occurred: {e.response.status_code} - {e.response.text}")
```

