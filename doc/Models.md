

# **ApiKeyCredentials**
## Required: 
api_key
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| api_key | str | API key for the integration ||

# **BasicAuthCredentials**
## Required: 
username, password
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| username | str | Basic auth username for the integration ||
| password | str | Basic auth password for the integration ||

# **BlocklistAddIPsRequest**
## Required: 
ips
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| ips | list[str] | List of IPs or networks ||
| expiration | str | Expiration date ||

# **BlocklistContentStats**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| total_seen | int | None ||
| total_fire | int | None ||
| total_seen_1m | int | None ||
| total_in_other_lists | int | None ||
| total_false_positive | int | None ||
| false_positive_removed_by_crowdsec | int | None ||
| most_present_behaviors | list[CtiBehavior] | None ||
| most_present_categories | list[CtiCategory] | None ||
| most_present_scenarios | list[CtiScenario] | None ||
| top_as | list[CtiAs] | None ||
| top_attacking_countries | list[CtiCountry] | None ||
| top_ips | list[CtiIp] | None ||
| updated_at | str | None ||

# **BlocklistCreateRequest**
## Required: 
name, description
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | Blocklist name, must be unique within the organization ||
| label | str | Blocklist human readable name (Default: name) ||
| description | str | Blocklist description ||
| references | list[str] | Useful references on the list's origins ||
| tags | list[str] | Classification tags ||
| from_cti_query | str | CTI query (doc link available soon) ||
| since | str | Since duration for the CTI query (5m, 2h, 7d). Max is 30 days ||

# **BlocklistCreateResponse**
## Required: 
id, created_at, updated_at, name, label, description, references, is_private, tags, pricing_tier, source, stats, from_cti_query, since, shared_with, organization_id, subscribers
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | Blocklist id ||
| created_at | str | Blocklist creation date ||
| updated_at | str | Blocklist update date ||
| name | str | Blocklist name, unique within the organization ||
| label | str | Blocklist human readable name ||
| description | str | Blocklist description ||
| references | list[str] | Blocklist references ||
| is_private | bool | Private blocklist if True or public if False ||
| tags | list[str] | Classification tags ||
| pricing_tier | str | None ||
| source | str | None ||
| stats | object | None ||
| from_cti_query | Optional[str] | CTI query from which the blocklist was created ||
| since | Optional[str] | Since duration for the CTI query (eg. 5m, 2h, 7d). Max is 30 days ||
| shared_with | list[Share] | List of organizations shared with ||
| organization_id | Optional[str] | Blocklists owner's organization id ||
| subscribers | list[BlocklistSubscriberEntity] | List of subscribers to the blocklist. Only subscribers belonging to your organization are returned ||

# **BlocklistDeleteIPsRequest**
## Required: 
ips
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| ips | list[str] | List of IPs or networks ||

# **BlocklistGetResponse**
## Required: 
id, created_at, updated_at, name, label, description, references, is_private, tags, pricing_tier, source, stats, from_cti_query, since, shared_with, organization_id, subscribers
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | Blocklist id ||
| created_at | str | Blocklist creation date ||
| updated_at | str | Blocklist update date ||
| name | str | Blocklist name, unique within the organization ||
| label | str | Blocklist human readable name ||
| description | str | Blocklist description ||
| references | list[str] | Blocklist references ||
| is_private | bool | Private blocklist if True or public if False ||
| tags | list[str] | Classification tags ||
| pricing_tier | str | None ||
| source | str | None ||
| stats | object | None ||
| from_cti_query | Optional[str] | CTI query from which the blocklist was created ||
| since | Optional[str] | Since duration for the CTI query (eg. 5m, 2h, 7d). Max is 30 days ||
| shared_with | list[Share] | List of organizations shared with ||
| organization_id | Optional[str] | Blocklists owner's organization id ||
| subscribers | list[BlocklistSubscriberEntity] | List of subscribers to the blocklist. Only subscribers belonging to your organization are returned ||

# **BlocklistIncludeFilters**
## Enum: 
PUBLIC, PRIVATE, SHARED, ALL

# **BlocklistResponse**
## Required: 
id, created_at, updated_at, name, label, description, references, is_private, tags, pricing_tier, source, stats, from_cti_query, since, shared_with, organization_id, subscribers
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | Blocklist id ||
| created_at | str | Blocklist creation date ||
| updated_at | str | Blocklist update date ||
| name | str | Blocklist name, unique within the organization ||
| label | str | Blocklist human readable name ||
| description | str | Blocklist description ||
| references | list[str] | Blocklist references ||
| is_private | bool | Private blocklist if True or public if False ||
| tags | list[str] | Classification tags ||
| pricing_tier | str | None ||
| source | str | None ||
| stats | object | None ||
| from_cti_query | Optional[str] | CTI query from which the blocklist was created ||
| since | Optional[str] | Since duration for the CTI query (eg. 5m, 2h, 7d). Max is 30 days ||
| shared_with | list[Share] | List of organizations shared with ||
| organization_id | Optional[str] | Blocklists owner's organization id ||
| subscribers | list[BlocklistSubscriberEntity] | List of subscribers to the blocklist. Only subscribers belonging to your organization are returned ||

# **BlocklistShareRequest**
## Required: 
organizations
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| organizations | list[Share] | List of organizations to share the blocklist ||

# **BlocklistSources**
## Enum: 
CROWDSEC, THIRD_PARTY, CUSTOM

# **BlocklistStats**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| content_stats | object | None ||
| usage_stats | Optional[object] | None ||
| addition_2days | int | None ||
| addition_month | int | None ||
| suppression_2days | int | None ||
| suppression_month | int | None ||
| change_2days_percentage | float | None ||
| change_month_percentage | float | None ||
| count | int | None ||
| updated_at | str | None ||

# **BlocklistSubscriberEntity**
## Required: 
id, entity_type, remediation
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | Subscriber entity id ||
| entity_type | str | None ||
| remediation | str | Remediation ||

# **BlocklistSubscribersResponse**
## Required: 
subscribers
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| subscribers | list[BlocklistSubscriberEntity] | List of subscribers ||

# **BlocklistSubscription**
## Required: 
id, name, label
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | None ||
| name | str | None ||
| label | str | None ||

# **BlocklistSubscriptionRequest**
## Required: 
entity_type
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| ids | list[str] | List of subscriber entity id ||
| entity_type | str | None ||
| remediation | Optional[str] | Remediation ||

# **BlocklistSubscriptionResponse**
## Required: 
updated, errors
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| updated | Optional[list[str]] | List of updated blocklist ids ||
| errors | Optional[list[object]] | List of errors if any ||

# **BlocklistUpdateRequest**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| label | str | Blocklist human readable name ||
| description | str | Blocklist description ||
| references | list[str] | Blocklist references ||
| tags | list[str] | Blocklist tags ||
| from_cti_query | str | CTI query (doc link available soon) ||
| since | str | Since duration for the CTI query (eg. 5m, 2h, 7d). Max is 30 days ||

# **BlocklistUsageStats**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| engines_subscribed_directly | int | None ||
| engines_subscribed_through_org | int | None ||
| engines_subscribed_through_tag | int | None ||
| total_subscribed_engines | int | None ||
| updated_at | str | None ||

# **Body_uploadBlocklistContent**
## Required: 
file
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| file | str | Blocklist file in txt format ||

# **CtiAs**
## Required: 
as_num, as_name, total_ips
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| as_num | str | None ||
| as_name | str | None ||
| total_ips | int | None ||

# **CtiBehavior**
## Required: 
name, label, description, references, total_ips
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | None ||
| label | str | None ||
| description | str | None ||
| references | list[str] | None ||
| total_ips | int | None ||

# **CtiCategory**
## Required: 
name, label, description, total_ips
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | None ||
| label | str | None ||
| description | str | None ||
| total_ips | int | None ||

# **CtiCountry**
## Required: 
country_short, total_ips
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| country_short | str | None ||
| total_ips | int | None ||

# **CtiIp**
## Required: 
ip, total_signals_1m
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| ip | str | None ||
| total_signals_1m | int | None ||
| reputation | str | None ||

# **CtiScenario**
## Required: 
name, label, description, references, total_ips
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | None ||
| label | str | None ||
| description | str | None ||
| references | list[str] | None ||
| total_ips | int | None ||

# **EntityType**
## Enum: 
ORG, TAG, ENGINE, FIREWALL_INTEGRATION, REMEDIATION_COMPONENT_INTEGRATION

# **HTTPValidationError**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| detail | list[ValidationError] | None ||

# **IntegrationCreateRequest**
## Required: 
name, entity_type, output_format
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | Name of the integration ||
| description | str | Description of the integration ||
| entity_type | str | None ||
| output_format | str | None ||

# **IntegrationCreateResponse**
## Required: 
id, name, organization_id, created_at, updated_at, entity_type, output_format, blocklists, endpoint, credentials
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the integration ||
| name | str | Name of the integration. Should be unique within the organization ||
| organization_id | str | ID of the owner organization ||
| description | str | Description of the integration ||
| created_at | str | Time the integration was created ||
| updated_at | str | Last time the integration was updated ||
| entity_type | str | None ||
| output_format | str | None ||
| last_pull | str | Last time the integration pulled blocklists ||
| blocklists | list[BlocklistSubscription] | Blocklists that are subscribed by the integration ||
| endpoint | str | Url that should be used by the firewall or the remediation component to fetch the integration's content ||
| stats | object | None ||
| credentials | Union[object, object] | Credentials that were generated for the integration ||

# **IntegrationGetResponse**
## Required: 
id, name, organization_id, created_at, updated_at, entity_type, output_format, blocklists, endpoint
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the integration ||
| name | str | Name of the integration. Should be unique within the organization ||
| organization_id | str | ID of the owner organization ||
| description | str | Description of the integration ||
| created_at | str | Time the integration was created ||
| updated_at | str | Last time the integration was updated ||
| entity_type | str | None ||
| output_format | str | None ||
| last_pull | str | Last time the integration pulled blocklists ||
| blocklists | list[BlocklistSubscription] | Blocklists that are subscribed by the integration ||
| endpoint | str | Url that should be used by the firewall or the remediation component to fetch the integration's content ||
| stats | object | None ||

# **IntegrationType**
## Enum: 
FIREWALL_INTEGRATION, REMEDIATION_COMPONENT_INTEGRATION

# **IntegrationUpdateRequest**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | New name ||
| description | str | New description ||
| output_format | str | None ||
| regenerate_credentials | bool | Regenerate credentials for the integration ||

# **IntegrationUpdateResponse**
## Required: 
id, name, organization_id, created_at, updated_at, entity_type, output_format, blocklists, endpoint
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the integration ||
| name | str | Name of the integration. Should be unique within the organization ||
| organization_id | str | ID of the owner organization ||
| description | str | Description of the integration ||
| created_at | str | Time the integration was created ||
| updated_at | str | Last time the integration was updated ||
| entity_type | str | None ||
| output_format | str | None ||
| last_pull | str | Last time the integration pulled blocklists ||
| blocklists | list[BlocklistSubscription] | Blocklists that are subscribed by the integration ||
| endpoint | str | Url that should be used by the firewall or the remediation component to fetch the integration's content ||
| stats | object | None ||
| credentials | Optional[object, object] | Credentials for the integration ||

# **Links**
## Required: 
first, last, self, next, prev
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| first | Optional[str] | None ||
| last | Optional[str] | None ||
| self | Optional[str] | None ||
| next | Optional[str] | None ||
| prev | Optional[str] | None ||

# **OutputFormat**
## Enum: 
PLAIN_TEXT, F5, REMEDIATION_COMPONENT, FORTIGATE, PALOALTO, CHECKPOINT, CISCO

# **Page_BlocklistResponse_**
## Required: 
items, total, page, size, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[BlocklistResponse] | None ||
| total | Optional[int] | None ||
| page | Optional[int] | None ||
| size | Optional[int] | None ||
| pages | Optional[int] | None ||
| links | object | None ||

# **Page_IntegrationGetResponse_**
## Required: 
items, total, page, size, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[IntegrationGetResponse] | None ||
| total | Optional[int] | None ||
| page | Optional[int] | None ||
| size | Optional[int] | None ||
| pages | Optional[int] | None ||
| links | object | None ||

# **Permission**
## Enum: 
READ, WRITE

# **PricingTiers**
## Enum: 
FREE, PREMIUM, PLATINUM

# **Share**
## Required: 
organization_id, permission
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| organization_id | str | None ||
| permission | str | None ||

# **Stats**
## Required: 
count
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| count | int | Number of total blocklists items the integration will pull ||

# **ValidationError**
## Required: 
loc, msg, type
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| loc | list[Union[str, int]] | None ||
| msg | str | None ||
| type | str | None ||