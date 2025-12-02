# Introduction

**crowdsec_service_api** is a Python library to use the [Crowdsec Service API](https://docs.crowdsec.net/u/service_api/intro/).
You can manage your Crowdsec resources such as (blocklists, integrations) from your Python applications.

If you have any question, any remark, or if you find a bug in this library, please [open an issue](https://github.com/crowdsecurity/crowdsec-service-api-sdk-python/issues).

You can find a Quickstart about this SDK, following this [documentation](https://docs.crowdsec.net/u/service_api/sdks)



## API Endpoint services

[Allowlists](./Allowlists.md)

[Blocklists](./Blocklists.md)

[Integrations](./Integrations.md)

[Info](./Info.md)

[Metrics](./Metrics.md)

[Hub](./Hub.md)

[Cves](./Cves.md)

## API Endpoint models

[AllowlistCreateRequest](./Models.md#allowlistcreaterequest)

[AllowlistCreateResponse](./Models.md#allowlistcreateresponse)

[AllowlistGetItemsResponse](./Models.md#allowlistgetitemsresponse)

[AllowlistGetResponse](./Models.md#allowlistgetresponse)

[AllowlistItemUpdateRequest](./Models.md#allowlistitemupdaterequest)

[AllowlistItemUpdateResponse](./Models.md#allowlistitemupdateresponse)

[AllowlistItemsCreateRequest](./Models.md#allowlistitemscreaterequest)

[AllowlistScope](./Models.md#allowlistscope)

[AllowlistSubscriberEntity](./Models.md#allowlistsubscriberentity)

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

[BlocklistSubscribersCount](./Models.md#blocklistsubscriberscount)

[BlocklistSubscription](./Models.md#blocklistsubscription)

[BlocklistSubscriptionRequest](./Models.md#blocklistsubscriptionrequest)

[BlocklistSubscriptionResponse](./Models.md#blocklistsubscriptionresponse)

[BlocklistUpdateRequest](./Models.md#blocklistupdaterequest)

[BlocklistUsageStats](./Models.md#blocklistusagestats)

[Body_uploadBlocklistContent](./Models.md#body_uploadblocklistcontent)

[ComputedMetrics](./Models.md#computedmetrics)

[ComputedSavedMetrics](./Models.md#computedsavedmetrics)

[CtiAs](./Models.md#ctias)

[CtiBehavior](./Models.md#ctibehavior)

[CtiCategory](./Models.md#cticategory)

[CtiCountry](./Models.md#cticountry)

[CtiIp](./Models.md#ctiip)

[CtiScenario](./Models.md#ctiscenario)

[EntityType](./Models.md#entitytype)

[GetRemediationMetricsResponse](./Models.md#getremediationmetricsresponse)

[HTTPValidationError](./Models.md#httpvalidationerror)

[InfoResponse](./Models.md#inforesponse)

[IntegrationCreateRequest](./Models.md#integrationcreaterequest)

[IntegrationCreateResponse](./Models.md#integrationcreateresponse)

[IntegrationGetResponse](./Models.md#integrationgetresponse)

[IntegrationType](./Models.md#integrationtype)

[IntegrationUpdateRequest](./Models.md#integrationupdaterequest)

[IntegrationUpdateResponse](./Models.md#integrationupdateresponse)

[Links](./Models.md#links)

[MetricUnits](./Models.md#metricunits)

[OriginMetrics](./Models.md#originmetrics)

[OutputFormat](./Models.md#outputformat)

[PageTAnyCustomizedAllowlistGetItemsResponse](./Models.md#pagetanycustomizedallowlistgetitemsresponse)

[PageTAnyCustomizedAllowlistGetResponse](./Models.md#pagetanycustomizedallowlistgetresponse)

[PageTAnyCustomizedAllowlistSubscriberEntity](./Models.md#pagetanycustomizedallowlistsubscriberentity)

[PageTAnyCustomizedBlocklistSubscriberEntity](./Models.md#pagetanycustomizedblocklistsubscriberentity)

[PageTAnyCustomizedIntegrationGetResponse](./Models.md#pagetanycustomizedintegrationgetresponse)

[PageTAnyCustomizedPublicBlocklistResponse](./Models.md#pagetanycustomizedpublicblocklistresponse)

[Permission](./Models.md#permission)

[PricingTiers](./Models.md#pricingtiers)

[PublicBlocklistResponse](./Models.md#publicblocklistresponse)

[PublicPaginatedBlocklistResponse](./Models.md#publicpaginatedblocklistresponse)

[RawMetrics](./Models.md#rawmetrics)

[RemediationMetrics](./Models.md#remediationmetrics)

[RemediationMetricsData](./Models.md#remediationmetricsdata)

[Share](./Models.md#share)

[SourceInfo](./Models.md#sourceinfo)

[SourceType](./Models.md#sourcetype)

[Stats](./Models.md#stats)

[SubscriberEntityType](./Models.md#subscriberentitytype)

[ValidationError](./Models.md#validationerror)

[AppsecConfigIndex](./Models.md#appsecconfigindex)

[AppsecRuleIndex](./Models.md#appsecruleindex)

[CollectionIndex](./Models.md#collectionindex)

[ContextIndex](./Models.md#contextindex)

[Index](./Models.md#index)

[ParserIndex](./Models.md#parserindex)

[PostoverflowIndex](./Models.md#postoverflowindex)

[ScenarioIndex](./Models.md#scenarioindex)

[VersionDetail](./Models.md#versiondetail)

[AffectedComponent](./Models.md#affectedcomponent)

[AttackDetail](./Models.md#attackdetail)

[Behavior](./Models.md#behavior)

[Classification](./Models.md#classification)

[Classifications](./Models.md#classifications)

[GetCVEResponse](./Models.md#getcveresponse)

[History](./Models.md#history)

[IPItem](./Models.md#ipitem)

[Location](./Models.md#location)

[MitreTechnique](./Models.md#mitretechnique)

[PageTypeVarCustomizedIPItem](./Models.md#pagetypevarcustomizedipitem)

[Reference](./Models.md#reference)

[ScoreBreakdown](./Models.md#scorebreakdown)

[Scores](./Models.md#scores)

[SubscribeCVEIntegrationRequest](./Models.md#subscribecveintegrationrequest)