from httpx import Response
from typing import TypedDict
from clients.http.client import HTTPClient
from clients.http.geteway.client import build_gateway_http_client


class CardIssueVirtualDict(TypedDict):
    id: str
    pin: str
    cvv: str
    type: str
    status: str
    accountId: str
    cardNumber: str
    cardHolder: str
    expiryDate: str
    paymentSystem: str

class CreateCardsIssueVirtualResponse(TypedDict):
    card: CardIssueVirtualDict

class CardIssuePhysicalDict(TypedDict):
    id: str
    pin: str
    cvv: str
    type: str
    status: str
    accountId: str
    cardNumber: str
    cardHolder: str
    expiryDate: str
    paymentSystem: str

class CreateCardsIssuePhysicalResponse(TypedDict):
    card: CardIssuePhysicalDict

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

    def create_issue_virtual_card(self, userId: str, accountId: str) -> CreateCardsIssueVirtualResponse:
        request = CreateVirtualCard(userId=userId, accountId=accountId)
        response = self.issue_virtual_card_api(request)
        return response.json()

    def create_issue_physical_card(self, userId: str, accountId: str) -> CreateCardsIssuePhysicalResponse:
        request = CreatePhysicalCard(userId=userId, accountId=accountId)
        response = self.issue_virtual_card_api(request)
        return response.json()

def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    return CardsGatewayHTTPClient(client=build_gateway_http_client())
