from enum import Enum
from .base_model import Page
from .models import *
from .services.blocklists import Blocklists
from .services.integrations import Integrations
from .services.info import Info
from .services.hub import Hub
from .http_client import ApiKeyAuth

class Server(Enum):
    production_server = 'https://admin.api.crowdsec.net/v1/'

__all__ = [
    'Blocklists',
    'Integrations',
    'Info',
    'Hub',
    'ApiKeyCredentials',
    'BasicAuthCredentials',
    'BlocklistAddIPsRequest',
    'BlocklistContentStats',
    'BlocklistCreateRequest',
    'BlocklistCreateResponse',
    'BlocklistDeleteIPsRequest',
    'BlocklistGetResponse',
    'BlocklistIncludeFilters',
    'BlocklistResponse',
    'BlocklistShareRequest',
    'BlocklistSources',
    'BlocklistStats',
    'BlocklistSubscriberEntity',
    'BlocklistSubscribersResponse',
    'BlocklistSubscription',
    'BlocklistSubscriptionRequest',
    'BlocklistSubscriptionResponse',
    'BlocklistUpdateRequest',
    'BlocklistUsageStats',
    'Body_uploadBlocklistContent',
    'CtiAs',
    'CtiBehavior',
    'CtiCategory',
    'CtiCountry',
    'CtiIp',
    'CtiScenario',
    'EntityType',
    'HTTPValidationError',
    'InfoResponse',
    'IntegrationCreateRequest',
    'IntegrationCreateResponse',
    'IntegrationGetResponse',
    'IntegrationType',
    'IntegrationUpdateRequest',
    'IntegrationUpdateResponse',
    'Links',
    'OutputFormat',
    'Page_BlocklistResponse_',
    'Page_IntegrationGetResponse_',
    'Permission',
    'PricingTiers',
    'Share',
    'Stats',
    'ValidationError',
    'HubType',
    'ApiKeyAuth',
    'Server',
    'Page'
]