from urllib.parse import urlparse
from pydantic import BaseModel, ConfigDict
from typing import Generic, Sequence, Optional, TypeVar
from httpx import Auth
from .http_client import HttpClient


class BaseModelSdk(BaseModel):
    model_config = ConfigDict(
        extra="ignore",
    )


T = TypeVar("T")


class Page(BaseModelSdk, Generic[T]):
    _client: "Service"
    items: Sequence[T]
    total: Optional[int]
    page: Optional[int]
    size: Optional[int]
    pages: Optional[int] = None
    links: Optional[dict] = None

    def __init__(self, _client: "Service", **data):
        super().__init__(**data)
        self._client = _client

    def next(self, client: "Service" = None) -> "Page[T]":
        return (client if client is not None else self._client).next_page(self)


class Service:
    def __init__(self, base_url: str, auth: Auth) -> None:
        self.http_client = HttpClient(base_url=base_url, auth=auth)

    def next_page(self, page: Page[T]) -> Page[T]:
        if not page.links:
            raise ValueError(
                "No links found in the response, this is not a paginated response."
            )
        if page.links.get("next"):
            # links are relative to host not to full base url. We need to pass a full formatted url here
            parsed_url = urlparse(self.http_client.base_url)
            response = self.http_client.get(
                f"{parsed_url.scheme}://{parsed_url.netloc}{page.links['next']}", path_params=None, params=None, headers=None
            )
            return page.__class__(_client=self, **response.json())
        return None
