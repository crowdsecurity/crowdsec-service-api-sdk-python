# Introduction

**crowdsec_service_api** is a Python library to use the [Crowdsec Service API](https://docs.crowdsec.net/u/service_api/intro/).
You can manage your Crowdsec resources such as (blocklists, integrations) from your Python applications.

If you have any question, any remark, or if you find a bug in this library, please [open an issue](https://github.com/crowdsecurity/crowdsec-service-api-sdk-python/issues).

You can find a Quickstart about this SDK, following this [documentation](https://docs.crowdsec.net/u/service_api/sdks)



## API Endpoint services

[Allowlists](./Allowlists.md)

[Blocklists](./Blocklists.md)

[Integrations](./Integrations.md)

[Decisions](./Decisions.md)

[Info](./Info.md)

[Metrics](./Metrics.md)

[Hub](./Hub.md)

## API Endpoint models

[AllowlistCreateRequest](./Models.md#allowlistcreaterequest)

[AllowlistCreateResponse](./Models.md#allowlistcreateresponse)

[AllowlistGetItemsResponse](./Models.md#allowlistgetitemsresponse)

[AllowlistGetItemsResponsePage](./Models.md#allowlistgetitemsresponsepage)

[AllowlistGetResponse](./Models.md#allowlistgetresponse)

[AllowlistGetResponsePage](./Models.md#allowlistgetresponsepage)

[AllowlistItemUpdateRequest](./Models.md#allowlistitemupdaterequest)

[AllowlistItemUpdateResponse](./Models.md#allowlistitemupdateresponse)

[AllowlistItemsCreateRequest](./Models.md#allowlistitemscreaterequest)

[AllowlistScope](./Models.md#allowlistscope)

[AllowlistSubscriberEntity](./Models.md#allowlistsubscriberentity)

[AllowlistSubscriberEntityPage](./Models.md#allowlistsubscriberentitypage)

[AllowlistSubscribersCount](./Models.md#allowlistsubscriberscount)

[AllowlistSubscriptionRequest](./Models.md#allowlistsubscriptionrequest)

[AllowlistSubscriptionResponse](./Models.md#allowlistsubscriptionresponse)

[AllowlistUpdateRequest](./Models.md#allowlistupdaterequest)

[AllowlistUpdateResponse](./Models.md#allowlistupdateresponse)

[ApiKeyCredentials](./Models.md#apikeycredentials)

[AttacksMetrics](./Models.md#attacksmetrics)

[BasicAuthCredentials](./Models.md#basicauthcredentials)

[BlocklistAddIPsRequest](./Models.md#blocklistaddipsrequest)

[BlocklistCategory](./Models.md#blocklistcategory)

[BlocklistContentStats](./Models.md#blocklistcontentstats)

[BlocklistCreateRequest](./Models.md#blocklistcreaterequest)

[BlocklistDeleteIPsRequest](./Models.md#blocklistdeleteipsrequest)

[BlocklistIncludeFilters](./Models.md#blocklistincludefilters)

[BlocklistOrigin](./Models.md#blocklistorigin)

[BlocklistSearchRequest](./Models.md#blocklistsearchrequest)

[BlocklistShareRequest](./Models.md#blocklistsharerequest)

[BlocklistSources](./Models.md#blocklistsources)

[BlocklistStats](./Models.md#blockliststats)

[BlocklistSubscriberEntity](./Models.md#blocklistsubscriberentity)

[BlocklistSubscriberEntityPage](./Models.md#blocklistsubscriberentitypage)

[BlocklistSubscribersCount](./Models.md#blocklistsubscriberscount)

[BlocklistSubscription](./Models.md#blocklistsubscription)

[BlocklistSubscriptionRequest](./Models.md#blocklistsubscriptionrequest)

[BlocklistSubscriptionResponse](./Models.md#blocklistsubscriptionresponse)

[BlocklistUpdateRequest](./Models.md#blocklistupdaterequest)

[BlocklistUsageStats](./Models.md#blocklistusagestats)

[Body_uploadBlocklistContent](./Models.md#body_uploadblocklistcontent)

[CVESubscription](./Models.md#cvesubscription)

[ComputedMetrics](./Models.md#computedmetrics)

[ComputedSavedMetrics](./Models.md#computedsavedmetrics)

[CtiAs](./Models.md#ctias)

[CtiBehavior](./Models.md#ctibehavior)

[CtiCategory](./Models.md#cticategory)

[CtiCountry](./Models.md#cticountry)

[CtiIp](./Models.md#ctiip)

[CtiScenario](./Models.md#ctiscenario)

[DecisionCreateRequest](./Models.md#decisioncreaterequest)

[DecisionCreateResponse](./Models.md#decisioncreateresponse)

[DecisionResponse](./Models.md#decisionresponse)

[DecisionTargetModel](./Models.md#decisiontargetmodel)

[DecisionTargetType](./Models.md#decisiontargettype)

[DecisionsGetResponsePage](./Models.md#decisionsgetresponsepage)

[DecisionsSortBy](./Models.md#decisionssortby)

[DecisionsSortOrder](./Models.md#decisionssortorder)

[EntityType](./Models.md#entitytype)

[FingerprintSubscription](./Models.md#fingerprintsubscription)

[GetRemediationMetricsResponse](./Models.md#getremediationmetricsresponse)

[HTTPValidationError](./Models.md#httpvalidationerror)

[InfoResponse](./Models.md#inforesponse)

[IntegrationCreateRequest](./Models.md#integrationcreaterequest)

[IntegrationCreateResponse](./Models.md#integrationcreateresponse)

[IntegrationGetResponse](./Models.md#integrationgetresponse)

[IntegrationGetResponsePage](./Models.md#integrationgetresponsepage)

[IntegrationType](./Models.md#integrationtype)

[IntegrationUpdateRequest](./Models.md#integrationupdaterequest)

[IntegrationUpdateResponse](./Models.md#integrationupdateresponse)

[Links](./Models.md#links)

[MetricUnits](./Models.md#metricunits)

[OriginMetrics](./Models.md#originmetrics)

[OutputFormat](./Models.md#outputformat)

[Permission](./Models.md#permission)

[PricingTiers](./Models.md#pricingtiers)

[PublicBlocklistResponse](./Models.md#publicblocklistresponse)

[PublicBlocklistResponsePage](./Models.md#publicblocklistresponsepage)

[RawMetrics](./Models.md#rawmetrics)

[RemediationMetrics](./Models.md#remediationmetrics)

[RemediationMetricsData](./Models.md#remediationmetricsdata)

[Share](./Models.md#share)

[SourceInfo](./Models.md#sourceinfo)

[SourceType](./Models.md#sourcetype)

[Stats](./Models.md#stats)

[SubscriberEntityType](./Models.md#subscriberentitytype)

[ValidationError](./Models.md#validationerror)

[VendorSubscription](./Models.md#vendorsubscription)

[AppsecConfigIndex](./Models.md#appsecconfigindex)

[AppsecRuleIndex](./Models.md#appsecruleindex)

[CollectionIndex](./Models.md#collectionindex)

[ContextIndex](./Models.md#contextindex)

[Index](./Models.md#index)

[ParserIndex](./Models.md#parserindex)

[PostoverflowIndex](./Models.md#postoverflowindex)

[ScenarioIndex](./Models.md#scenarioindex)

[VersionDetail](./Models.md#versiondetail)