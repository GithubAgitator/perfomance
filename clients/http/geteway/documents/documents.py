from httpx import Response
from clients.http.client import HTTPClient
from clients.http.geteway.client import build_gateway_http_client
from clients.http.geteway.documents.schema import GetDocumentTariffResponseSchema, GetDocumentContractResponseSchema


class DocumentsGatewayHTTPClient(HTTPClient):
    """Получение документа по тарифу"""
    def get_documents_tariff_api(self, account_id: str) -> Response:
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    """Получение контракта по документу"""
    def get_documents_contract_api(self, account_id: str) -> Response:
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    def get_documents_tariff(self, account_id: str) -> GetDocumentTariffResponseSchema:
        response = self.get_documents_tariff_api(account_id)
        return GetDocumentTariffResponseSchema.model_validate_json(response.text)

    def get_documents_contract(self, account_id: str) -> GetDocumentContractResponseSchema:
        response = self.get_documents_contract_api(account_id)
        return GetDocumentContractResponseSchema.model_validate_json(response.text)

def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())