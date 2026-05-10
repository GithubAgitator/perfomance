from httpx import Response
from typing import TypedDict
from clients.http.client import HTTPClient
from clients.http.geteway.client import build_gateway_http_client


class DocumentDict(TypedDict):
    """Описание структуры получения ответа документа"""
    url: str
    document: str

class GetDocumentTariffResponseDict(TypedDict):
    tariff: DocumentDict

class GetDocumentContractResponseDict(TypedDict):
    contract: DocumentDict

class DocumentsGatewayHTTPClient(HTTPClient):
    """Получение документа по тарифу"""
    def get_documents_tariff_api(self, account_id: str) -> Response:
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    """Получение контракта по документу"""
    def get_documents_contract_api(self, account_id: str) -> Response:
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    def get_documents_tariff(self, account_id: str) -> GetDocumentTariffResponseDict:
        response = self.get_documents_tariff_api(account_id)
        return response.json()

    def get_documents_contract(self, account_id: str) -> GetDocumentContractResponseDict:
        response = self.get_documents_contract_api(account_id)
        return response.json()

def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())