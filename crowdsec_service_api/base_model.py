from urllib.parse import urlparse
from pydantic import BaseModel, ConfigDict, PrivateAttr, RootModel
from typing import Generic, Sequence, Optional, TypeVar, Any
from httpx import Auth
from .http_client import HttpClient


class BaseModelSdk(BaseModel):
    model_config = ConfigDict(
        extra="ignore",
    )
    _client: Optional["Service"] = PrivateAttr(default=None)

    def __init__(self, /, _client: "Service" = None, **data):
        super().__init__(**data)
        self._client = _client

    def next(self, client: "Service" = None) -> Optional["BaseModelSdk"]:
        return (client if client is not None else self._client).next_page(self)


class RootModelSdk(RootModel):
    def __getattr__(self, item: str) -> Any:
        return getattr(self.root, item)


T = TypeVar("T")


class Page(BaseModelSdk, Generic[T]):
    items: Sequence[T]
    total: Optional[int]
    page: Optional[int]
    size: Optional[int]
    pages: Optional[int] = None
    links: Optional[dict] = None


class Service:
    def __init__(self, base_url: str, auth: Auth, user_agent: str = None) -> None:
        self.http_client = HttpClient(
            base_url=base_url, auth=auth, user_agent=user_agent
        )

    def next_page(self, page: BaseModelSdk) -> Optional[BaseModelSdk]:
        if not hasattr(page, "links") or not page.links:
            raise ValueError(
                "No links found in the response, this is not a paginated response."
            )
        if page.links.next:
            # links are relative to host not to full base url. We need to pass a full formatted url here
            parsed_url = urlparse(self.http_client.base_url)
            response = self.http_client.get(
                f"{parsed_url.scheme}://{parsed_url.netloc}{page.links.next}",
                path_params=None,
                params=None,
                headers=None,
            )
            return page.__class__(_client=self, **response.json())
        return None
