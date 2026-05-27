from httpx import Response
from clients.http.client import HTTPClient
from clients.http.geteway.cards.schema import CreateVirtualCardSchema, CreatePhysicalCardSchema, \
    CreateCardsIssueVirtualResponseSchema, CreateCardsIssuePhysicalResponseSchema
from clients.http.geteway.client import build_gateway_http_client


class CardsGatewayHTTPClient(HTTPClient):
    """
        Выпуск виртуальной карты.
        """
    def issue_virtual_card_api(self, request: CreateVirtualCardSchema) -> Response:
        return self.post(f"/api/v1/cards/issue-virtual-card", json=request.model_dump(by_alias=True))

    """
        Выпуск физической карты.
        """
    def issue_physical_card_api(self, request: CreatePhysicalCardSchema) -> Response:
        return self.post("/api/v1/cards/issue-physical-card", json=request.model_dump(by_alias=True))

    def create_issue_virtual_card(self, user_id: str, account_id: str) -> CreateCardsIssueVirtualResponseSchema:
        request = CreateVirtualCardSchema(user_id=user_id, account_id=account_id)
        response = self.issue_virtual_card_api(request)
        return CreateCardsIssueVirtualResponseSchema.model_validate_json(response.text)

    def create_issue_physical_card(self, user_id: str, account_id: str) -> CreateCardsIssuePhysicalResponseSchema:
        request = CreatePhysicalCardSchema(user_id=user_id, account_id=account_id)
        response = self.issue_physical_card_api(request)
        return CreateCardsIssuePhysicalResponseSchema.model_validate_json(response.text)

def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    return CardsGatewayHTTPClient(client=build_gateway_http_client())
