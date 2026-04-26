from httpx import Response
from typing import TypedDict
from clients.http.client import HTTPClient


class CreateVirtualCard(TypedDict):
    userId: str
    accountId: str

class CreatePhysicalCard(TypedDict):
    userId: str
    accountId: str

class CardsGatewayHTTPClient(HTTPClient):
    """
        Выпуск виртуальной карты.
        """
    def issue_virtual_card_api(self, request: CreateVirtualCard) -> Response:
        return self.post(f"/api/v1/cards/issue-virtual-card", json=request)

    """
        Выпуск физической карты.
        """
    def issue_physical_card_api(self, request: CreatePhysicalCard) -> Response:
        return self.post("/api/v1/cards/issue-physical-card", json=request)
