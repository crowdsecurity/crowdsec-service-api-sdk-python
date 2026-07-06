

# **AggregatedDecisionItem**
## Required: 
id, first_created_at, last_created_at, origin, scenario, min_duration, max_duration, first_expiration, last_expiration, count, machines, target
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the decision aggregated item ||
| first_created_at | str | Creation date of the first decision in the group ||
| last_created_at | str | Creation date of the last decision in the group ||
| origin | str | Origin of the decision ||
| scenario | str | Scenario of the decision ||
| min_duration | str | Min duration in the group of decisions ||
| max_duration | str | Max durations in the group of decisions ||
| first_expiration | str | First expiration date in the group of decisions ||
| last_expiration | str | Last expiration date in the group of decisions ||
| count | int | Number of decisions in the group ||
| machines | Machines | Machines object (the instance ID is the key) with the decision status and timestamp ||
| target | DecisionTargetModel | None ||

# **AggregatedDecisionsGetResponse**
## Required: 
id, scope, type, value, decisions
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the decision aggregated item ||
| scope | str | Scope of the decision ||
| type | str | Type of the decision ||
| value | str | Value of the decision ||
| country | Optional[str] | Country associated with the decision ||
| as_name | Optional[str] | AS name associated with the decision ||
| as_num | Optional[int] | AS number associated with the decision ||
| city | Optional[str] | City associated with the decision ||
| latitude | Optional[float] | Latitude associated with the decision ||
| longitude | Optional[float] | Longitude associated with the decision ||
| first_created_at | str | Creation date of the first decision in the group ||
| last_created_at | str | Creation date of the last decision in the group ||
| first_expiration | str | Expiration date of the first decision in the group ||
| last_expiration | str | Expiration date of the last decision in the group ||
| decisions | list[AggregatedDecisionItem] | List of decisions in the group ||

# **AggregatedDecisionsGetResponsePage**
## Required: 
items, page, size, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[AggregatedDecisionsGetResponse] | None ||
| total | Optional[int] | None ||
| page | Optional[int] | None ||
| size | Optional[int] | None ||
| pages | Optional[int] | None ||
| links | Links | None ||

# **AggregatedDecisionsSortBy**
## Enum: 
FIRST_CREATED_AT, FIRST_EXPIRATION

# **AllowlistCreateRequest**
## Required: 
name
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | Name of the allowlist ||
| description | Optional[str] | Description of the allowlist ||

# **AllowlistCreateResponse**
## Required: 
id, organization_id, name, created_at, total_items
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the allowlist ||
| organization_id | str | ID of the owner organization ||
| name | str | Name of the allowlist ||
| description | str | Description of the allowlist ||
| created_at | str | Time the allowlist was created ||
| updated_at | Optional[str] | Time the allowlist was updated ||
| from_cti_query | Optional[str] | CTI query from which the blocklist was created ||
| since | Optional[str] | Since duration for the CTI query (eg. 5m, 2h, 7d). Max is 30 days ||
| total_items | int | Number of items in the allowlist ||

# **AllowlistGetItemsResponse**
## Required: 
id, allowlist_id, description, scope, value, created_at, created_by
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the allowlist entry ||
| allowlist_id | str | ID of the allowlist ||
| description | str | Description of the allowlist entry ||
| scope | AllowlistScope | None ||
| value | Union[str, str] | Value of the allowlist entry ||
| created_at | str | Time the allowlist entry was created ||
| updated_at | Optional[str] | Time the allowlist entry was updated ||
| created_by | SourceInfo | None ||
| updated_by | Optional[SourceInfo] | The source user who updated the allowlist entry ||
| expiration | Optional[str] | Time the allowlist entry will expire ||

# **AllowlistGetItemsResponsePage**
## Required: 
items, page, size, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[AllowlistGetItemsResponse] | None ||
| total | Optional[int] | None ||
| page | Optional[int] | None ||
| size | Optional[int] | None ||
| pages | Optional[int] | None ||
| links | Links | None ||

# **AllowlistGetResponse**
## Required: 
id, organization_id, name, created_at, total_items
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the allowlist ||
| organization_id | str | ID of the owner organization ||
| name | str | Name of the allowlist ||
| description | str | Description of the allowlist ||
| created_at | str | Time the allowlist was created ||
| updated_at | Optional[str] | Time the allowlist was updated ||
| from_cti_query | Optional[str] | CTI query from which the blocklist was created ||
| since | Optional[str] | Since duration for the CTI query (eg. 5m, 2h, 7d). Max is 30 days ||
| total_items | int | Number of items in the allowlist ||
| subscribers | list[AllowlistSubscribersCount] | List of subscribers count by entity type ||

# **AllowlistGetResponsePage**
## Required: 
items, page, size, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[AllowlistGetResponse] | None ||
| total | Optional[int] | None ||
| page | Optional[int] | None ||
| size | Optional[int] | None ||
| pages | Optional[int] | None ||
| links | Links | None ||

# **AllowlistItemUpdateRequest**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| description | str | Description of the allowlist entry ||
| expiration | Optional[str] | Time the allowlist entry will expire ||

# **AllowlistItemUpdateResponse**
## Required: 
id, allowlist_id, description, scope, value, created_at, updated_at, created_by, updated_by
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the allowlist entry ||
| allowlist_id | str | ID of the allowlist ||
| description | str | Description of the allowlist entry ||
| scope | AllowlistScope | None ||
| value | Union[str, str] | Value of the allowlist entry ||
| created_at | str | Time the allowlist entry was created ||
| updated_at | str | Time the allowlist entry was updated ||
| created_by | SourceInfo | None ||
| updated_by | SourceInfo | None ||
| expiration | Optional[str] | Time the allowlist entry will expire ||

# **AllowlistItemsCreateRequest**
## Required: 
items, description
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[Union[str, str]] | List of values to add to the allowlist ||
| description | str | Description of the allowlist entry ||
| expiration | Optional[str] | Time the allowlist entry will expire ||

# **AllowlistScope**
## Enum: 
IP, RANGE

# **AllowlistSubscriberEntity**
## Required: 
id, entity_type
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | Subscriber entity id ||
| entity_type | SubscriberEntityType | None ||

# **AllowlistSubscriberEntityPage**
## Required: 
items, page, size, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[AllowlistSubscriberEntity] | None ||
| total | Optional[int] | None ||
| page | Optional[int] | None ||
| size | Optional[int] | None ||
| pages | Optional[int] | None ||
| links | Links | None ||

# **AllowlistSubscribersCount**
## Required: 
entity_type, count
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| entity_type | SubscriberEntityType | None ||
| count | int | Subscriber entity count ||

# **AllowlistSubscriptionRequest**
## Required: 
entity_type
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| ids | list[str] | List of subscriber entity id ||
| entity_type | EntityType | None ||

# **AllowlistSubscriptionResponse**
## Required: 
updated, errors
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| updated | Optional[list[str]] | List of updated allowlist ids ||
| errors | Optional[list[object]] | List of errors if any ||

# **AllowlistUpdateRequest**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | Optional[str] | Name of the allowlist ||
| description | Optional[str] | Description of the allowlist ||

# **AllowlistUpdateResponse**
## Required: 
id, organization_id, name, created_at, total_items
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the allowlist ||
| organization_id | str | ID of the owner organization ||
| name | str | Name of the allowlist ||
| description | str | Description of the allowlist ||
| created_at | str | Time the allowlist was created ||
| updated_at | Optional[str] | Time the allowlist was updated ||
| from_cti_query | Optional[str] | CTI query from which the blocklist was created ||
| since | Optional[str] | Since duration for the CTI query (eg. 5m, 2h, 7d). Max is 30 days ||
| total_items | int | Number of items in the allowlist ||
| subscribers | list[AllowlistSubscribersCount] | List of subscribers count by entity type ||

# **ApiKeyCredentials**
## Required: 
api_key
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| api_key | str | API key for the integration ||

# **AttacksMetrics**
## Required: 
total, label, progression, data
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| total | Union[int, float] | Total value of the metric ||
| label | str | Label of the metric which is the attack type ||
| progression | Optional[int] | Progression of the metric value from the previous period ||
| data | list[RemediationMetricsData] | Data points ||

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

# **BlocklistCategory**
## Required: 
name, label, description, priority
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | None ||
| label | str | None ||
| description | str | None ||
| priority | int | None ||

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
| updated_at | Optional[str] | None ||

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
| store_full_content_in_s3 | bool | Whether to store the full blocklist content in S3 or not ||

# **BlocklistDeleteIPsRequest**
## Required: 
ips
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| ips | list[str] | List of IPs or networks ||

# **BlocklistIncludeFilters**
## Enum: 
PUBLIC, PRIVATE, SHARED, ALL

# **BlocklistOrigin**
## Required: 
label, id, pricing_tier
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| label | str | Label of the blocklist ||
| id | str | ID of the blocklist ||
| pricing_tier | PricingTiers | None ||

# **BlocklistSearchRequest**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| page | int | Page number ||
| page_size | int | Page size ||
| pricing_tiers | list[PricingTiers] | Pricing tiers ||
| query | str | Search query ||
| targeted_countries | list[str] | Targeted countries ||
| classifications | list[str] | Classifications ||
| behaviors | list[str] | Behaviors ||
| min_ips | int | Minimum number of IPs ||
| sources | list[BlocklistSources] | Sources ||
| categories | list[str] | Categories ||
| is_private | Optional[bool] | Private blocklist ||
| is_subscribed | Optional[bool] | Subscribed blocklist (None: all) ||

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
| content_stats | BlocklistContentStats | None ||
| usage_stats | Optional[BlocklistUsageStats] | None ||
| addition_2days | int | None ||
| addition_month | int | None ||
| suppression_2days | int | None ||
| suppression_month | int | None ||
| change_2days_percentage | float | None ||
| change_month_percentage | float | None ||
| count | int | None ||
| updated_at | Optional[str] | None ||

# **BlocklistSubscriberEntity**
## Required: 
id, entity_type, remediation
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | Subscriber entity id ||
| entity_type | SubscriberEntityType | None ||
| remediation | str | Remediation ||

# **BlocklistSubscriberEntityPage**
## Required: 
items, page, size, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[BlocklistSubscriberEntity] | None ||
| total | Optional[int] | None ||
| page | Optional[int] | None ||
| size | Optional[int] | None ||
| pages | Optional[int] | None ||
| links | Links | None ||

# **BlocklistSubscribersCount**
## Required: 
entity_type, count
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| entity_type | SubscriberEntityType | None ||
| count | int | Subscriber entity count ||

# **BlocklistSubscription**
## Required: 
id, name, label
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | None ||
| remediation | Optional[str] | None ||
| name | str | None ||
| label | str | None ||

# **BlocklistSubscriptionRequest**
## Required: 
entity_type
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| ids | list[str] | List of subscriber entity id ||
| entity_type | SubscriberEntityType | None ||
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
| total_subscribed_organizations | int | None ||
| updated_at | Optional[str] | None ||

# **Body_uploadBlocklistContent**
## Required: 
file
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| file | str | Blocklist file in txt format ||

# **CVESubscription**
## Required: 
id
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | CVE ID ||

# **ComputedMetrics**
## Required: 
saved
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| saved | ComputedSavedMetrics | None ||
| dropped | list[RemediationMetrics] | estimated dropped metrics ||
| prevented | list[AttacksMetrics] | prevented attacks metrics ||

# **ComputedSavedMetrics**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| log_lines | list[RemediationMetrics] | estimated log lines saved ||
| storage | list[RemediationMetrics] | estimated storage saved ||
| egress_traffic | list[RemediationMetrics] | estimated egress traffic saved ||

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

# **DecisionCreateRequest**
## Required: 
duration, origin, scenario, scope, type, value, target
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| created_at | str | None ||
| uuid | Optional[str] | UUID of the decision ||
| id | Optional[int] | ID of the decision ||
| duration | str | Duration of the decision ||
| origin | str | Origin of the decision ||
| scenario | str | Scenario of the decision ||
| scope | str | Scope of the decision ||
| type | str | Type of the decision ||
| value | str | Value of the decision ||
| country | Optional[str] | Country associated with the decision ||
| as_name | Optional[str] | AS name associated with the decision ||
| as_num | Optional[int] | AS number associated with the decision ||
| city | Optional[str] | City associated with the decision ||
| latitude | Optional[float] | Latitude associated with the decision ||
| longitude | Optional[float] | Longitude associated with the decision ||
| target | DecisionTargetModel | None ||

# **DecisionCreateResponse**
## Required: 
uuid
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| uuid | str | UUID of the created decision ||

# **DecisionMachineState**
## Required: 
timestamp, state
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| timestamp | str | Date of when the state has been set ||
| state | DecisionMachineStateEnum | None ||

# **DecisionMachineStateEnum**
## Enum: 
PENDING_CREATE, PENDING_DELETE, APPLIED

# **DecisionResponse**
## Required: 
uuid, id, duration, origin, scenario, scope, type, value, target
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| created_at | str | None ||
| uuid | str | UUID of the decision ||
| id | int | ID of the decision ||
| duration | str | Duration of the decision ||
| origin | str | Origin of the decision ||
| scenario | str | Scenario of the decision ||
| scope | str | Scope of the decision ||
| type | str | Type of the decision ||
| value | str | Value of the decision ||
| country | Optional[str] | Country associated with the decision ||
| as_name | Optional[str] | AS name associated with the decision ||
| as_num | Optional[int] | AS number associated with the decision ||
| city | Optional[str] | City associated with the decision ||
| latitude | Optional[float] | Latitude associated with the decision ||
| longitude | Optional[float] | Longitude associated with the decision ||
| target | DecisionTargetModel | None ||

# **DecisionTargetModel**
## Required: 
type, value
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| type | DecisionTargetType | None ||
| value | str | Value of the decision target ||

# **DecisionTargetType**
## Enum: 
ORG, TAG, ENTITY

# **DecisionsGetResponsePage**
## Required: 
items, page, size, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[DecisionResponse] | None ||
| total | Optional[int] | None ||
| page | Optional[int] | None ||
| size | Optional[int] | None ||
| pages | Optional[int] | None ||
| links | Links | None ||

# **DecisionsSortBy**
## Enum: 
CREATED_AT, EXPIRE_AT

# **DecisionsSortOrder**
## Enum: 
ASC, DESC

# **EntityType**
## Enum: 
ORG, TAG, ENGINE, FIREWALL_INTEGRATION, REMEDIATION_COMPONENT_INTEGRATION, REMEDIATION_COMPONENT, LOG_PROCESSOR

# **FingerprintSubscription**
## Required: 
id
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | Fingerprint ID ||

# **GetRemediationMetricsResponse**
## Required: 
raw, computed
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| raw | RawMetrics | None ||
| computed | ComputedMetrics | None ||
| stats | RemediationStats | None ||

# **HTTPValidationError**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| detail | list[ValidationError] | None ||

# **InfoResponse**
## Required: 
organization_id, subscription_type, api_key_name
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| organization_id | str | The organization ID ||
| subscription_type | str | The organization subscription type ||
| api_key_name | str | The API key name that is used ||

# **IntegrationCreateRequest**
## Required: 
name, entity_type, output_format
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | Name of the integration ||
| description | str | Description of the integration ||
| entity_type | IntegrationType | None ||
| output_format | OutputFormat | None ||
| pull_limit | Optional[int] | Maximum number of items to pull ||
| enable_ip_aggregation | bool | Whether to enable IP aggregation into ranges ||

# **IntegrationCreateResponse**
## Required: 
id, name, organization_id, created_at, updated_at, entity_type, output_format, blocklists, cves, fingerprints, vendors, endpoint, credentials
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the integration ||
| name | str | Name of the integration. Should be unique within the organization ||
| organization_id | str | ID of the owner organization ||
| description | str | Description of the integration ||
| created_at | str | Time the integration was created ||
| updated_at | str | Last time the integration was updated ||
| entity_type | IntegrationType | None ||
| output_format | OutputFormat | None ||
| last_pull | Optional[str] | Last time the integration pulled blocklists ||
| blocklists | list[BlocklistSubscription] | Blocklists that are subscribed by the integration ||
| cves | list[CVESubscription] | CVEs that are subscribed by the integration ||
| fingerprints | list[FingerprintSubscription] | Fingerprints that are subscribed by the integration ||
| vendors | list[VendorSubscription] | Vendors that are subscribed by the integration ||
| endpoint | str | Url that should be used by the firewall or the remediation component to fetch the integration's content ||
| stats | Stats | None ||
| tags | list[str] | Tags associated with the integration ||
| pull_limit | Optional[int] | Maximum number of items to pull ||
| enable_ip_aggregation | bool | Whether to enable IP aggregation into ranges ||
| credentials | Union[ApiKeyCredentials, BasicAuthCredentials] | Credentials that were generated for the integration ||

# **IntegrationGetResponse**
## Required: 
id, name, organization_id, created_at, updated_at, entity_type, output_format, blocklists, cves, fingerprints, vendors, endpoint
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the integration ||
| name | str | Name of the integration. Should be unique within the organization ||
| organization_id | str | ID of the owner organization ||
| description | str | Description of the integration ||
| created_at | str | Time the integration was created ||
| updated_at | str | Last time the integration was updated ||
| entity_type | IntegrationType | None ||
| output_format | OutputFormat | None ||
| last_pull | Optional[str] | Last time the integration pulled blocklists ||
| blocklists | list[BlocklistSubscription] | Blocklists that are subscribed by the integration ||
| cves | list[CVESubscription] | CVEs that are subscribed by the integration ||
| fingerprints | list[FingerprintSubscription] | Fingerprints that are subscribed by the integration ||
| vendors | list[VendorSubscription] | Vendors that are subscribed by the integration ||
| endpoint | str | Url that should be used by the firewall or the remediation component to fetch the integration's content ||
| stats | Stats | None ||
| tags | list[str] | Tags associated with the integration ||
| pull_limit | Optional[int] | Maximum number of items to pull ||
| enable_ip_aggregation | bool | Whether to enable IP aggregation into ranges ||

# **IntegrationGetResponsePage**
## Required: 
items, page, size, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[IntegrationGetResponse] | None ||
| total | Optional[int] | None ||
| page | Optional[int] | None ||
| size | Optional[int] | None ||
| pages | Optional[int] | None ||
| links | Links | None ||

# **IntegrationType**
## Enum: 
FIREWALL_INTEGRATION, REMEDIATION_COMPONENT_INTEGRATION

# **IntegrationUpdateRequest**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | New name ||
| description | str | New description ||
| output_format | OutputFormat | None ||
| regenerate_credentials | bool | Regenerate credentials for the integration ||
| pull_limit | Optional[int] | Maximum number of items to pull ||
| enable_ip_aggregation | bool | Whether to enable IP aggregation into ranges ||

# **IntegrationUpdateResponse**
## Required: 
id, name, organization_id, created_at, updated_at, entity_type, output_format, blocklists, cves, fingerprints, vendors, endpoint
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the integration ||
| name | str | Name of the integration. Should be unique within the organization ||
| organization_id | str | ID of the owner organization ||
| description | str | Description of the integration ||
| created_at | str | Time the integration was created ||
| updated_at | str | Last time the integration was updated ||
| entity_type | IntegrationType | None ||
| output_format | OutputFormat | None ||
| last_pull | Optional[str] | Last time the integration pulled blocklists ||
| blocklists | list[BlocklistSubscription] | Blocklists that are subscribed by the integration ||
| cves | list[CVESubscription] | CVEs that are subscribed by the integration ||
| fingerprints | list[FingerprintSubscription] | Fingerprints that are subscribed by the integration ||
| vendors | list[VendorSubscription] | Vendors that are subscribed by the integration ||
| endpoint | str | Url that should be used by the firewall or the remediation component to fetch the integration's content ||
| stats | Stats | None ||
| tags | list[str] | Tags associated with the integration ||
| pull_limit | Optional[int] | Maximum number of items to pull ||
| enable_ip_aggregation | bool | Whether to enable IP aggregation into ranges ||
| credentials | Optional[ApiKeyCredentials, BasicAuthCredentials] | Credentials for the integration ||

# **Links**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| first | Optional[str] | None ||
| last | Optional[str] | None ||
| self | Optional[str] | None ||
| next | Optional[str] | None ||
| prev | Optional[str] | None ||

# **MetricUnits**
## Enum: 
BYTE, PACKET, REQUEST, IP, LINE, EVENT

# **OriginMetrics**
## Required: 
origin, data
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| origin | Optional[BlocklistOrigin, str] | Origin of the metric ||
| data | list[RemediationMetricsData] | Data points ||

# **OutputFormat**
## Enum: 
PLAIN_TEXT, F5, REMEDIATION_COMPONENT, FORTIGATE, PALOALTO, CHECKPOINT, CISCO, JUNIPER, MIKROTIK, PFSENSE, OPNSENSE, SOPHOS

# **Permission**
## Enum: 
READ, WRITE

# **PricingTiers**
## Enum: 
FREE, PREMIUM, PLATINUM

# **PublicBlocklistResponse**
## Required: 
id, created_at, updated_at, name, description, is_private, pricing_tier, source, stats
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
| pricing_tier | PricingTiers | None ||
| source | BlocklistSources | None ||
| stats | BlocklistStats | None ||
| from_cti_query | Optional[str] | CTI query from which the blocklist was created ||
| since | Optional[str] | Since duration for the CTI query (eg. 5m, 2h, 7d). Max is 30 days ||
| shared_with | list[Share] | List of organizations shared with ||
| organization_id | Optional[str] | Blocklists owner's organization id ||
| subscribers | list[BlocklistSubscribersCount] | List of subscribers to the blocklist. Only subscribers belonging to your organization are returned ||
| categories | list[BlocklistCategory] | List of categories for the blocklist ||

# **PublicBlocklistResponsePage**
## Required: 
items, page, size, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[PublicBlocklistResponse] | None ||
| total | Optional[int] | None ||
| page | Optional[int] | None ||
| size | Optional[int] | None ||
| pages | Optional[int] | None ||
| links | Links | None ||

# **RawMetrics**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| dropped | list[RemediationMetrics] | dropped metrics ||
| processed | list[RemediationMetrics] | processed metrics ||

# **RemediationMetrics**
## Required: 
total, unit, progression, data
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| total | Union[int, float] | Total value of the metric ||
| unit | MetricUnits | None ||
| progression | Optional[int] | Progression of the metric value from the previous period ||
| data | list[OriginMetrics] | Data points per origin ||

# **RemediationMetricsData**
## Required: 
value, timestamp
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| value | Union[int, float] | Value of the metric ||
| timestamp | str | Timestamp of the metric ||

# **RemediationStats**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| dropped_rate | Dropped Rate | Percentage of dropped traffic over total processed traffic, per unit, rounded to 2 decimals. Null when no processed traffic was observed for the unit. ||
| allowed_rate | Allowed Rate | Percentage of allowed (passed-through) traffic over total processed traffic, per unit, rounded to 2 decimals. Null when no processed traffic was observed for the unit. ||

# **Share**
## Required: 
organization_id, permission
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| organization_id | str | None ||
| permission | Permission | None ||

# **SourceInfo**
## Required: 
source_type, identifier
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| source_type | SourceType | None ||
| identifier | str | The source identifier that created the allowlist entry ||

# **SourceType**
## Enum: 
USER, APIKEY

# **Stats**
## Required: 
count
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| count | int | Number of total blocklists items the integration will pull ||

# **SubscriberEntityType**
## Enum: 
ORG, TAG, ENGINE, FIREWALL_INTEGRATION, REMEDIATION_COMPONENT_INTEGRATION

# **ValidationError**
## Required: 
loc, msg, type
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| loc | list[Union[str, int]] | None ||
| msg | str | None ||
| type | str | None ||

# **VendorSubscription**
## Required: 
id
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | Vendor ID ||

# **AppsecConfigIndex**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| content | Optional[str] | The YAML content of the item, in plaintext. ||
| description | Optional[str] | A short, plaintext description of the item ||
| labels | Optional[object] | Classification labels for the item ||
| path | Optional[str] | Relative path to the item's YAML content ||
| references | Optional[list[str]] | List of references to external resources ||
| version | Optional[str] | Current version of the collection ||
| versions | Optional[object] | A dictionary where each key is a version number (e.g., '0.1', '0.2') ||

# **AppsecRuleIndex**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| content | Optional[str] | The YAML content of the item, in plaintext. ||
| description | Optional[str] | A short, plaintext description of the item ||
| labels | Optional[object] | Classification labels for the item ||
| path | Optional[str] | Relative path to the item's YAML content ||
| references | Optional[list[str]] | List of references to external resources ||
| version | Optional[str] | Current version of the collection ||
| versions | Optional[object] | A dictionary where each key is a version number (e.g., '0.1', '0.2') ||

# **CollectionIndex**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| appsec-configs | Optional[list[str]] | List of appsec-configs ||
| appsec-rules | Optional[list[str]] | List of appsec-rules ||
| collections | Optional[list[str]] | List of collections ||
| content | Optional[str] | The YAML content of the item, in plaintext. ||
| contexts | Optional[list[str]] | List of contexts ||
| description | Optional[str] | A short, plaintext description of the item ||
| labels | Optional[object] | Classification labels for the item ||
| parsers | Optional[list[str]] | List of parsers ||
| path | Optional[str] | Relative path to the item's YAML content ||
| postoverflows | Optional[list[str]] | List of postoverflows ||
| references | Optional[list[str]] | List of references to external resources ||
| scenarios | Optional[list[str]] | List of scenarios ||
| version | Optional[str] | Current version of the collection ||
| versions | Optional[object] | A dictionary where each key is a version number (e.g., '0.1', '0.2') ||

# **ContextIndex**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| content | Optional[str] | The YAML content of the item, in plaintext. ||
| description | Optional[str] | A short, plaintext description of the item ||
| labels | Optional[object] | Classification labels for the item ||
| path | Optional[str] | Relative path to the item's YAML content ||
| references | Optional[list[str]] | List of references to external resources ||
| version | Optional[str] | Current version of the collection ||
| versions | Optional[object] | A dictionary where each key is a version number (e.g., '0.1', '0.2') ||

# **Index**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| appsec-configs | Appsec-Configs | None ||
| appsec-rules | Appsec-Rules | None ||
| collections | Collections | None ||
| contexts | Contexts | None ||
| parsers | Parsers | None ||
| postoverflows | Postoverflows | None ||
| scenarios | Scenarios | None ||

# **ParserIndex**
## Required: 
stage
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| content | Optional[str] | The YAML content of the item, in plaintext. ||
| description | Optional[str] | A short, plaintext description of the item ||
| labels | Optional[object] | Classification labels for the item ||
| path | Optional[str] | Relative path to the item's YAML content ||
| references | Optional[list[str]] | List of references to external resources ||
| stage | str | The stage of the parser ||
| version | Optional[str] | Current version of the collection ||
| versions | Optional[object] | A dictionary where each key is a version number (e.g., '0.1', '0.2') ||

# **PostoverflowIndex**
## Required: 
stage
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| content | Optional[str] | The YAML content of the item, in plaintext. ||
| description | Optional[str] | A short, plaintext description of the item ||
| labels | Optional[object] | Classification labels for the item ||
| path | Optional[str] | Relative path to the item's YAML content ||
| references | Optional[list[str]] | List of references to external resources ||
| stage | str | The stage of the postoverflow ||
| version | Optional[str] | Current version of the collection ||
| versions | Optional[object] | A dictionary where each key is a version number (e.g., '0.1', '0.2') ||

# **ScenarioIndex**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| content | Optional[str] | The YAML content of the item, in plaintext. ||
| description | Optional[str] | A short, plaintext description of the item ||
| labels | Optional[object] | Classification labels for the item ||
| path | Optional[str] | Relative path to the item's YAML content ||
| references | Optional[list[str]] | List of references to external resources ||
| version | Optional[str] | Current version of the collection ||
| versions | Optional[object] | A dictionary where each key is a version number (e.g., '0.1', '0.2') ||

# **VersionDetail**
## Required: 
digest
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| deprecated | Optional[bool] | Indicates whether this version is deprecated. ||
| digest | str | The SHA256 digest of the versioned file. ||

# **AdjustmentScore**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| total | int | Total score adjustment ||
| recency | int | Recency score adjustment ||
| low_info | int | Low information score adjustment ||

# **AffectedComponent**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| vendor | Optional[str] | Vendor of the affected component ||
| product | Optional[str] | Product name of the affected component ||

# **AllowlistSubscription**
## Required: 
id
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | None ||

# **AttackDetail**
## Required: 
name, label, description
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | Attack detail name ||
| label | str | Attack detail label ||
| description | str | Attack detail description ||
| references | list[str] | Attack detail references ||

# **AttackerObjective**
## Enum: 
INFRASTRUCTURE_TAKEOVER, RANSOMWARE, DATA_EXFILTRATION

# **Behavior**
## Required: 
name, label, description
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | Behavior name ||
| label | str | Behavior label ||
| description | str | Behavior description ||

# **CVEEventOutput**
## Required: 
name, date, description, label, sorting_priority
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | None ||
| date | str | None ||
| description | str | None ||
| label | str | None ||
| sorting_priority | int | None ||

# **CVEExploitationPhase**
## Enum: 
INSUFFICIENT_DATA, EARLY_EXPLOITATION, FRESH_AND_POPULAR, TARGETED_EXPLOITATION, MASS_EXPLOITATION, BACKGROUND_NOISE, UNPOPULAR, WEARING_OUT, UNCLASSIFIED

# **CVEResponseDetailed**
## Required: 
id, name, title, affected_components, crowdsec_score, nb_ips, published_date, has_public_exploit, exploitation_phase
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the CVE ||
| name | str | Name of the CVE ||
| title | str | Title of the CVE ||
| affected_components | list[AffectedComponent] | List of affected components ||
| crowdsec_score | int | Live Exploit Tracker score of the CVE ||
| opportunity_score | int | Opportunity score indicating if it's an opportunistic(0) or targeted(5) attack (between 0-5) ||
| momentum_score | int | Momentum score indicating the vulnerability's trendiness based on signal comparison with the previous month. Higher scores (4-5) indicate significantly more signals this month than last month's average, while lower scores (0-1) indicate declining activity (between 0-5) ||
| first_seen | Optional[str] | First seen date ||
| last_seen | Optional[str] | Last seen date ||
| nb_ips | int | Number of unique IPs affected ||
| published_date | str | Published date of the CVE ||
| cvss_score | Optional[float] | CVSS score of the CVE ||
| has_public_exploit | bool | Indicates if there is a public exploit for the CVE ||
| rule_release_date | Optional[str] | Release date of the associated detection rule ||
| exploitation_phase | ExploitationPhase | None ||
| adjustment_score | Optional[AdjustmentScore] | Score adjustments applied to the CVE score based on various factors ||
| threat_context | Optional[ThreatContext] | Threat context (attacker/defender countries, industries, objectives) ||
| tags | list[str] | Tags associated with the CVE ||
| references | list[str] | List of references for the CVE ||
| description | Optional[str] | Description of the CVE ||
| crowdsec_analysis | Optional[str] | CrowdSec analysis of the CVE ||
| cwes | list[CWE] | List of CWEs associated with the CVE ||
| events | list[CVEEventOutput] | List of events related to the CVE ||

# **CVEsubscription**
## Required: 
id
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | None ||

# **CWE**
## Required: 
name, label, description
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | Name of the CWE ||
| label | str | Label of the CWE ||
| description | str | Description of the CWE ||

# **Classification**
## Required: 
name, label, description
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | Classification name ||
| label | str | Classification label ||
| description | str | Classification description ||

# **Classifications**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| false_positives | list[Classification] | False positive classifications ||
| classifications | list[Classification] | Main classifications ||

# **ExploitationPhase**
## Required: 
name, label, description
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | Name of the exploitation phase ||
| label | str | Label of the exploitation phase ||
| description | str | Description of the exploitation phase ||

# **ExploitationPhaseChangeEventItem**
## Required: 
cve_id, name, date, label, description, previous_phase, new_phase
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| cve_id | str | CVE identifier ||
| name | str | Event type name ||
| date | str | Date of the phase change ||
| label | str | Human-readable event label ||
| description | str | Rendered event description ||
| previous_phase | str | Previous exploitation phase label ||
| new_phase | str | New exploitation phase label ||

# **ExploitationPhaseChangeEventsResponsePage**
## Required: 
items, total, page, size, pages, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[ExploitationPhaseChangeEventItem] | None ||
| total | int | None ||
| page | int | None ||
| size | int | None ||
| pages | int | None ||
| links | Links | None ||

# **FacetBucket**
## Required: 
value, count
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| value | str | Facet value ||
| count | int | Number of IPs matching this value ||

# **FingerprintEventOutput**
## Required: 
name, date, description, label
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | None ||
| date | str | None ||
| description | str | None ||
| label | str | None ||

# **FingerprintRuleResponse**
## Required: 
id, name, title, affected_components, crowdsec_score, nb_ips, exploitation_phase
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | Fingerprint rule identifier ||
| name | str | Fingerprint rule name ||
| title | str | Fingerprint rule title ||
| affected_components | list[AffectedComponent] | List of affected components ||
| crowdsec_score | int | Live Exploit Tracker score for the fingerprint rule ||
| opportunity_score | int | Opportunity score ||
| momentum_score | int | Momentum score ||
| first_seen | Optional[str] | First seen date ||
| last_seen | Optional[str] | Last seen date ||
| nb_ips | int | Number of unique IPs observed ||
| rule_release_date | Optional[str] | Release date of the fingerprint rule ||
| exploitation_phase | ExploitationPhase | None ||
| adjustment_score | Optional[AdjustmentScore] | Score adjustment details ||
| threat_context | Optional[ThreatContext] | Threat context (attacker/defender countries, industries, objectives) ||
| tags | list[str] | Tags associated with the fingerprint rule ||
| description | Optional[str] | Fingerprint rule description ||
| references | list[str] | Reference links for the fingerprint rule ||
| crowdsec_analysis | Optional[str] | CrowdSec analysis for this fingerprint rule ||
| events | list[FingerprintEventOutput] | List of events related to the fingerprint rule ||

# **FingerprintTimelineItem**
## Required: 
timestamp, count
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| timestamp | str | Timestamp of the timeline event ||
| count | int | Count of occurrences at the timestamp ||

# **GetCVEIPsResponsePage**
## Required: 
items, total, page, size, pages, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[IPItem] | None ||
| total | int | None ||
| page | int | None ||
| size | int | None ||
| pages | int | None ||
| links | Links | None ||

# **GetCVEProtectRulesResponse**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| protect_rules | list[ProtectRule] | Protection/detection rules associated with the CVE ||

# **GetCVEResponse**
## Required: 
id, name, title, affected_components, crowdsec_score, nb_ips, published_date, has_public_exploit, exploitation_phase, references, description, crowdsec_analysis, cwes
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the CVE ||
| name | str | Name of the CVE ||
| title | str | Title of the CVE ||
| affected_components | list[AffectedComponent] | List of affected components ||
| crowdsec_score | int | Live Exploit Tracker score of the CVE ||
| opportunity_score | int | Opportunity score indicating if it's an opportunistic(0) or targeted(5) attack (between 0-5) ||
| momentum_score | int | Momentum score indicating the vulnerability's trendiness based on signal comparison with the previous month. Higher scores (4-5) indicate significantly more signals this month than last month's average, while lower scores (0-1) indicate declining activity (between 0-5) ||
| first_seen | Optional[str] | First seen date ||
| last_seen | Optional[str] | Last seen date ||
| nb_ips | int | Number of unique IPs affected ||
| published_date | str | Published date of the CVE ||
| cvss_score | Optional[float] | CVSS score of the CVE ||
| has_public_exploit | bool | Indicates if there is a public exploit for the CVE ||
| rule_release_date | Optional[str] | Release date of the associated detection rule ||
| exploitation_phase | ExploitationPhase | None ||
| adjustment_score | Optional[AdjustmentScore] | Score adjustments applied to the CVE score based on various factors ||
| threat_context | Optional[ThreatContext] | Threat context (attacker/defender countries, industries, objectives) ||
| tags | list[str] | Tags associated with the CVE ||
| references | list[str] | List of references for the CVE ||
| description | str | Description of the CVE ||
| crowdsec_analysis | Optional[str] | CrowdSec analysis of the CVE ||
| cwes | list[CWE] | List of CWEs associated with the CVE ||
| events | list[CVEEventOutput] | List of events related to the CVE ||

# **GetCVESubscribedIntegrationsResponsePage**
## Required: 
items, total, page, size, pages, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[IntegrationResponse] | None ||
| total | int | None ||
| page | int | None ||
| size | int | None ||
| pages | int | None ||
| links | Links | None ||

# **GetCVEsResponsePage**
## Required: 
items, total, page, size, pages, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[CVEResponseDetailed] | None ||
| total | int | None ||
| page | int | None ||
| size | int | None ||
| pages | int | None ||
| links | Links | None ||

# **GetCVEsSortBy**
## Enum: 
RULE_RELEASE_DATE, TRENDING, NB_IPS, NAME, FIRST_SEEN

# **GetCVEsSortOrder**
## Enum: 
ASC, DESC

# **GetFingerprintIPsResponsePage**
## Required: 
items, total, page, size, pages, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[IPItem] | None ||
| total | int | None ||
| page | int | None ||
| size | int | None ||
| pages | int | None ||
| links | Links | None ||

# **GetFingerprintRulesResponsePage**
## Required: 
items, total, page, size, pages, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[FingerprintRuleResponse] | None ||
| total | int | None ||
| page | int | None ||
| size | int | None ||
| pages | int | None ||
| links | Links | None ||

# **GetFingerprintSubscribedIntegrationsResponsePage**
## Required: 
items, total, page, size, pages, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[IntegrationResponse] | None ||
| total | int | None ||
| page | int | None ||
| size | int | None ||
| pages | int | None ||
| links | Links | None ||

# **GetVendorIPsResponsePage**
## Required: 
items, total, page, size, pages, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[IPItem] | None ||
| total | int | None ||
| page | int | None ||
| size | int | None ||
| pages | int | None ||
| links | Links | None ||

# **GetVendorSubscribedIntegrationsResponsePage**
## Required: 
items, total, page, size, pages, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[IntegrationResponse] | None ||
| total | int | None ||
| page | int | None ||
| size | int | None ||
| pages | int | None ||
| links | Links | None ||

# **History**
## Required: 
first_seen, last_seen, full_age, days_age
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| first_seen | str | First seen timestamp ||
| last_seen | str | Last seen timestamp ||
| full_age | int | Full age in days ||
| days_age | int | Days age ||

# **IPItem**
## Required: 
ip
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| ip | str | IP address ||
| reputation | Optional[str] | Reputation of the IP ||
| ip_range | Optional[str] | IP range ||
| ip_range_score | Optional[int] | IP range score ||
| ip_range_24 | Optional[str] | IP range /24 ||
| ip_range_24_reputation | Optional[str] | IP range /24 reputation ||
| ip_range_24_score | Optional[int] | IP range /24 score ||
| as_name | Optional[str] | AS name ||
| as_num | Optional[int] | AS number ||
| background_noise_score | Optional[int] | Background noise score ||
| background_noise | Optional[str] | Background noise level ||
| confidence | Optional[str] | Confidence level ||
| location | Optional[Location] | IP location information ||
| reverse_dns | Optional[str] | Reverse DNS ||
| behaviors | list[Behavior] | List of behaviors ||
| references | list[Reference] | List of references ||
| history | Optional[History] | Historical data ||
| classifications | Optional[Classifications] | Classification data ||
| mitre_techniques | list[MitreTechnique] | MITRE techniques ||
| cves | list[str] | List of CVEs ||
| attack_details | list[AttackDetail] | Attack details ||
| target_countries | Target Countries | Target countries ||
| scores | Optional[Scores] | Scoring information ||

# **IndicatorHttpPath**
## Required: 
value, first_seen, last_seen
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| indicator_type | str | None ||
| value | str | None ||
| first_seen | str | None ||
| last_seen | str | None ||
| nb_ips | int | None ||

# **IndicatorType**
Kind of IOC carried in an indicator entry. Add new variants here
as we extend coverage (user_agent, ja3h, …).
## Enum: 
HTTP_PATH

# **IndicatorsSortBy**
How the caller wants the indicators ordered.

``popular`` returns the cache's ``popular`` slice; ``most_recent`` returns
the ``recent`` slice. Both come pre-ranked from the Athena query so the
API doesn't re-sort.
## Enum: 
POPULAR, MOST_RECENT

# **IndustryRiskProfile**
## Enum: 
TECHNOLOGY_BUSINESS, TRADITIONAL_BUSINESS, CRITICAL_INFRASTRUCTURE, PUBLIC_SERVICE, SOHO

# **IndustryType**
## Enum: 
COMMERCE, FINANCIAL_SERVICES, HEALTHCARE, GOVERNMENT, NON_PROFIT, INDUSTRY, MEDIA, EDUCATION, SOHO

# **IntegrationResponse**
## Required: 
organization_id, entity_type, name, output_format
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| tags | list[str] | None ||
| organization_id | str | None ||
| created_at | str | Time the integration was created ||
| entity_type | EntityType | None ||
| id | str | ID of the integration ||
| blocklists | list[BlocklistSubscription] | None ||
| allowlists | list[AllowlistSubscription] | None ||
| cves | Optional[list[CVEsubscription]] | None ||
| fingerprints | Optional[list[FingerprintSubscription]] | None ||
| vendors | Optional[list[VendorSubscription]] | None ||
| name | str | Name of the integration ||
| updated_at | str | Last time the integration was updated ||
| description | Optional[str] | Description of the integration ||
| output_format | OutputFormat | None ||
| last_pull | Optional[str] | Last time the integration pulled blocklists ||
| pull_limit | Optional[int] | Maximum number of items to pull ||
| enable_ip_aggregation | bool | Whether to enable IP aggregation into ranges ||

# **IntervalOptions**
## Enum: 
HOUR, DAY, WEEK

# **IpsDetailsStats**
## Required: 
total, reputation, country, as_name, cves, classifications
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| total | int | Total number of matching IPs ||
| reputation | list[FacetBucket] | IP count by reputation ||
| country | list[FacetBucket] | IP count by country (top 5) ||
| as_name | list[FacetBucket] | IP count by AS name (top 5) ||
| cves | list[FacetBucket] | IP count by CVE (top 5) ||
| classifications | list[FacetBucket] | IP count by classification (top 5) ||

# **Location**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| country | Optional[str] | Country code ||
| city | Optional[str] | City name ||
| latitude | Optional[float] | Latitude coordinate ||
| longitude | Optional[float] | Longitude coordinate ||

# **LookupImpactCVEItem**
## Required: 
id, name, title, affected_components, crowdsec_score, nb_ips, published_date, has_public_exploit, exploitation_phase, references, description, crowdsec_analysis, cwes
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | ID of the CVE ||
| name | str | Name of the CVE ||
| title | str | Title of the CVE ||
| affected_components | list[AffectedComponent] | List of affected components ||
| crowdsec_score | int | Live Exploit Tracker score of the CVE ||
| opportunity_score | int | Opportunity score indicating if it's an opportunistic(0) or targeted(5) attack (between 0-5) ||
| momentum_score | int | Momentum score indicating the vulnerability's trendiness based on signal comparison with the previous month. Higher scores (4-5) indicate significantly more signals this month than last month's average, while lower scores (0-1) indicate declining activity (between 0-5) ||
| first_seen | Optional[str] | First seen date ||
| last_seen | Optional[str] | Last seen date ||
| nb_ips | int | Number of unique IPs affected ||
| published_date | str | Published date of the CVE ||
| cvss_score | Optional[float] | CVSS score of the CVE ||
| has_public_exploit | bool | Indicates if there is a public exploit for the CVE ||
| rule_release_date | Optional[str] | Release date of the associated detection rule ||
| exploitation_phase | ExploitationPhase | None ||
| adjustment_score | Optional[AdjustmentScore] | Score adjustments applied to the CVE score based on various factors ||
| threat_context | Optional[ThreatContext] | Threat context (attacker/defender countries, industries, objectives) ||
| tags | list[str] | Tags associated with the CVE ||
| references | list[str] | List of references for the CVE ||
| description | str | Description of the CVE ||
| crowdsec_analysis | Optional[str] | CrowdSec analysis of the CVE ||
| cwes | list[CWE] | List of CWEs associated with the CVE ||
| events | list[CVEEventOutput] | List of events related to the CVE ||
| type | str | Resource type ||

# **LookupImpactFingerprintItem**
## Required: 
id, name, title, affected_components, crowdsec_score, nb_ips, exploitation_phase
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| id | str | Fingerprint rule identifier ||
| name | str | Fingerprint rule name ||
| title | str | Fingerprint rule title ||
| affected_components | list[AffectedComponent] | List of affected components ||
| crowdsec_score | int | Live Exploit Tracker score for the fingerprint rule ||
| opportunity_score | int | Opportunity score ||
| momentum_score | int | Momentum score ||
| first_seen | Optional[str] | First seen date ||
| last_seen | Optional[str] | Last seen date ||
| nb_ips | int | Number of unique IPs observed ||
| rule_release_date | Optional[str] | Release date of the fingerprint rule ||
| exploitation_phase | ExploitationPhase | None ||
| adjustment_score | Optional[AdjustmentScore] | Score adjustment details ||
| threat_context | Optional[ThreatContext] | Threat context (attacker/defender countries, industries, objectives) ||
| tags | list[str] | Tags associated with the fingerprint rule ||
| description | Optional[str] | Fingerprint rule description ||
| references | list[str] | Reference links for the fingerprint rule ||
| crowdsec_analysis | Optional[str] | CrowdSec analysis for this fingerprint rule ||
| events | list[FingerprintEventOutput] | List of events related to the fingerprint rule ||
| type | str | Resource type ||

# **LookupImpactResponsePage**
## Required: 
items, total, page, size, pages, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[Annotated[Union[LookupImpactCVEItem, LookupImpactFingerprintItem], Field(discriminator='type')]] | None ||
| total | int | None ||
| page | int | None ||
| size | int | None ||
| pages | int | None ||
| links | Links | None ||

# **LookupListItemWithStats**
## Required: 
value
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| value | str | Lookup entry value ||
| nb_cves | int | Number of CVEs ||
| nb_fingerprints | int | Number of fingerprint rules ||
| nb_ips | int | Total number of unique IPs targeting this entry ||
| nb_ips_cves | int | Number of IPs across CVEs ||
| nb_ips_fingerprints | int | Number of IPs across fingerprint rules ||
| latest_rule_release | Optional[str] | Most recent rule release date for this entry ||

# **LookupListWithStatsResponsePage**
## Required: 
items, total, page, size, pages, links
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| items | list[LookupListItemWithStats] | None ||
| total | int | None ||
| page | int | None ||
| size | int | None ||
| pages | int | None ||
| links | Links | None ||

# **MitreTechnique**
## Required: 
name, label, description
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | MITRE technique ID ||
| label | str | MITRE technique label ||
| description | str | MITRE technique description ||

# **ProtectRule**
## Required: 
link, name, label
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| link | str | URL to the rule source ||
| published_date | Optional[str] | Date the rule was published ||
| tags | list[ProtectRuleTag] | Tags associated with the rule ||
| name | str | Rule name ||
| label | str | Human-readable rule label ||
| content | Optional[str] | Rule content/definition ||

# **ProtectRuleTag**
## Required: 
tag, label
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| tag | str | Tag identifier ||
| label | str | Human-readable tag label ||

# **Reference**
## Required: 
name, label, description
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | Reference name ||
| label | str | Reference label ||
| description | str | Reference description ||

# **ScoreBreakdown**
## Required: 
aggressiveness, threat, trust, anomaly, total
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| aggressiveness | int | Aggressiveness score ||
| threat | int | Threat score ||
| trust | int | Trust score ||
| anomaly | int | Anomaly score ||
| total | int | Total score ||

# **Scores**
## Required: 
overall, last_day, last_week, last_month
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| overall | ScoreBreakdown | None ||
| last_day | ScoreBreakdown | None ||
| last_week | ScoreBreakdown | None ||
| last_month | ScoreBreakdown | None ||

# **SinceOptions**

# **SubscribeCVEIntegrationRequest**
## Required: 
name
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | Name of the integration to subscribe ||

# **SubscribeFingerprintIntegrationRequest**
## Required: 
name
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | Name of the integration to subscribe ||

# **SubscribeVendorIntegrationRequest**
## Required: 
name
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| name | str | Name of the integration to subscribe ||

# **ThreatContext**
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| attacker_countries | Attacker Countries | Attacker country distribution (country code → count) ||
| defender_countries | Defender Countries | Defender country distribution (country code → count) ||
| industry_types | Industry Types | Industry type distribution (type → count) ||
| industry_risk_profiles | Industry Risk Profiles | Industry risk profile distribution (profile → count) ||
| attacker_objectives | Attacker Objectives | Attacker objective distribution (objective → count) ||

# **TimelineItem**
## Required: 
timestamp, count
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| timestamp | str | Timestamp of the timeline event ||
| count | int | Count of occurrences at the timestamp ||

# **TopProductItem**
## Required: 
value
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| value | str | Product name ||
| nb_ips_cves | int | Number of IPs across CVEs ||
| nb_ips_fingerprints | int | Number of IPs across fingerprint rules ||

# **VendorSortBy**
## Enum: 
VALUE, NB_CVES, NB_IPS, LATEST_RULE_RELEASE

# **VendorStatsResponse**
## Required: 
value
## Properties
| Property | Type | Description | Example |
|----------|------|-------------|---------|
| value | str | Vendor name ||
| nb_cves | int | Number of CVEs ||
| nb_fingerprints | int | Number of fingerprint rules ||
| nb_ips | int | Total number of unique IPs targeting this vendor ||
| nb_ips_cves | int | Number of IPs across CVEs ||
| nb_ips_fingerprints | int | Number of IPs across fingerprint rules ||
| top_products | list[TopProductItem] | Top products for this vendor sorted by total IPs descending ||