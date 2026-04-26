from httpx import Response, QueryParams
from typing import TypedDict
from clients.http.client import HTTPClient


class GetAccountQueryDict(TypedDict):
    userId: str


class OpenDepositAccountRequestDict(TypedDict):
    userId: str


class OpenSavingsAccountRequestDict(TypedDict):
    userId: str


class OpenDebitCardAccountRequestDict(TypedDict):
    userId: str


class OpenCreditCardAccountRequestDict(TypedDict):
    userId: str


class AccountsGatewayHTTPClient(HTTPClient):
    """Получение аккаунта"""
    def get_account_api(self, query: GetAccountQueryDict) -> Response:
        return self.get(f"/api/v1/accounts", params=QueryParams(**query))

    """Создание депозитной карты"""
    def create_open_deposit_account(self, request: OpenDepositAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-deposit-account", json=request)

    """Создание saving карты"""
    def create_open_savings_account(self, request: OpenSavingsAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-savings-account", json=request)

    """Создание debit карты"""
    def create_open_debit_account(self, request: OpenDebitCardAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-debit-card-account", json=request)

    """Создание credit карты"""
    def create_open_credit_account(self, request: OpenCreditCardAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-credit-card-account", json=request)


