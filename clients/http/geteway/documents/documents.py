from httpx import Response, QueryParams
from clients.http.client import HTTPClient


class DocumentsGatewayHTTPClient(HTTPClient):
    """Получение документа по тарифу"""
    def get_documents_tariff_api(self, account_id: str) -> Response:
        return self.get(f"/api/v1/accounts{account_id}")

    """Получение контракта по документу"""
    def get_documents_contract_api(self, account_id: str) -> Response:
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

