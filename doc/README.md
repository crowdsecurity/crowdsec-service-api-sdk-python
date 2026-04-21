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

[Cves](./Cves.md)

[Vendors](./Vendors.md)

[Products](./Products.md)

[TrackerTags](./TrackerTags.md)

[Fingerprints](./Fingerprints.md)

[TrackerEvents](./TrackerEvents.md)

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

[AdjustmentScore](./Models.md#adjustmentscore)

[AffectedComponent](./Models.md#affectedcomponent)

[AllowlistSubscription](./Models.md#allowlistsubscription)

[AttackDetail](./Models.md#attackdetail)

[AttackerObjective](./Models.md#attackerobjective)

[Behavior](./Models.md#behavior)

[CVEEventOutput](./Models.md#cveeventoutput)

[CVEExploitationPhase](./Models.md#cveexploitationphase)

[CVEResponseBase](./Models.md#cveresponsebase)

[CVEsubscription](./Models.md#cvesubscription)

[CWE](./Models.md#cwe)

[Classification](./Models.md#classification)

[Classifications](./Models.md#classifications)

[ExploitationPhase](./Models.md#exploitationphase)

[ExploitationPhaseChangeEventItem](./Models.md#exploitationphasechangeeventitem)

[ExploitationPhaseChangeEventsResponsePage](./Models.md#exploitationphasechangeeventsresponsepage)

[FacetBucket](./Models.md#facetbucket)

[FingerprintEventOutput](./Models.md#fingerprinteventoutput)

[FingerprintRuleResponse](./Models.md#fingerprintruleresponse)

[FingerprintRuleSummary](./Models.md#fingerprintrulesummary)

[FingerprintTimelineItem](./Models.md#fingerprinttimelineitem)

[GetCVEIPsResponsePage](./Models.md#getcveipsresponsepage)

[GetCVEProtectRulesResponse](./Models.md#getcveprotectrulesresponse)

[GetCVEResponse](./Models.md#getcveresponse)

[GetCVESubscribedIntegrationsResponsePage](./Models.md#getcvesubscribedintegrationsresponsepage)

[GetCVEsResponsePage](./Models.md#getcvesresponsepage)

[GetCVEsSortBy](./Models.md#getcvessortby)

[GetCVEsSortOrder](./Models.md#getcvessortorder)

[GetFingerprintIPsResponsePage](./Models.md#getfingerprintipsresponsepage)

[GetFingerprintRulesResponsePage](./Models.md#getfingerprintrulesresponsepage)

[GetFingerprintSubscribedIntegrationsResponsePage](./Models.md#getfingerprintsubscribedintegrationsresponsepage)

[GetVendorIPsResponsePage](./Models.md#getvendoripsresponsepage)

[GetVendorSubscribedIntegrationsResponsePage](./Models.md#getvendorsubscribedintegrationsresponsepage)

[History](./Models.md#history)

[IPItem](./Models.md#ipitem)

[IndustryRiskProfile](./Models.md#industryriskprofile)

[IndustryType](./Models.md#industrytype)

[IntegrationResponse](./Models.md#integrationresponse)

[IntervalOptions](./Models.md#intervaloptions)

[IpsDetailsStats](./Models.md#ipsdetailsstats)

[Location](./Models.md#location)

[LookupImpactCVEItem](./Models.md#lookupimpactcveitem)

[LookupImpactFingerprintItem](./Models.md#lookupimpactfingerprintitem)

[LookupImpactResponsePage](./Models.md#lookupimpactresponsepage)

[LookupListItemWithStats](./Models.md#lookuplistitemwithstats)

[LookupListWithStatsResponsePage](./Models.md#lookuplistwithstatsresponsepage)

[MitreTechnique](./Models.md#mitretechnique)

[ProtectRule](./Models.md#protectrule)

[ProtectRuleTag](./Models.md#protectruletag)

[Reference](./Models.md#reference)

[ScoreBreakdown](./Models.md#scorebreakdown)

[Scores](./Models.md#scores)

[SinceOptions](./Models.md#sinceoptions)

[SubscribeCVEIntegrationRequest](./Models.md#subscribecveintegrationrequest)

[SubscribeFingerprintIntegrationRequest](./Models.md#subscribefingerprintintegrationrequest)

[SubscribeVendorIntegrationRequest](./Models.md#subscribevendorintegrationrequest)

[ThreatContext](./Models.md#threatcontext)

[TimelineItem](./Models.md#timelineitem)

[TopProductItem](./Models.md#topproductitem)

[VendorSortBy](./Models.md#vendorsortby)

[VendorStatsResponse](./Models.md#vendorstatsresponse)