from httpx import Response, QueryParams
from typing import TypedDict, List
from clients.http.client import HTTPClient
from clients.http.geteway.client import build_gateway_http_client
from clients.http.geteway.users.client import GetUserResponseDict, UsersGatewayHTTPClient


class CardDict(TypedDict):
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


class AccountDict(TypedDict):
    id: str
    type: str
    cards: List[CardDict]
    status: str
    balance: float

class GetAccountResponseDict(TypedDict):
    accounts: List[AccountDict]

class CreateOpenDepositAccountResponseDict(TypedDict):
    account: AccountDict

class CreateOpenSavingsAccountResponseDict(TypedDict):
    account: AccountDict
class CreateOpenDebitAccountResponseDict(TypedDict):
    account: AccountDict
class CreateOpenCreditAccountResponseDict(TypedDict):
    account: AccountDict


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
    def create_open_deposit_account_api(self, request: OpenDepositAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-deposit-account", json=request)

    """Создание saving карты"""
    def create_open_savings_account_api(self, request: OpenSavingsAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-savings-account", json=request)

    """Создание debit карты"""
    def create_open_debit_account_api(self, request: OpenDebitCardAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-debit-card-account", json=request)

    """Создание credit карты"""
    def create_open_credit_account_api(self, request: OpenCreditCardAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-credit-card-account", json=request)

    def get_account(self, user_id: str) -> GetAccountResponseDict:
        query: GetAccountQueryDict = {"userId": user_id}
        response = self.get_account_api(query=query)
        return response.json()

    def create_open_deposit_account(self, user_id: str) -> CreateOpenDepositAccountResponseDict:
        request = OpenDepositAccountRequestDict(userId=user_id)
        response = self.create_open_deposit_account_api(request)
        return response.json()

    def create_open_savings_account(self, user_id: str) -> CreateOpenSavingsAccountResponseDict:
        request = OpenSavingsAccountRequestDict(userId=user_id)
        response = self.create_open_savings_account_api(request)
        return response.json()

    def create_open_debit_account(self, user_id: str) -> CreateOpenDebitAccountResponseDict:
        request = OpenDebitCardAccountRequestDict(userId=user_id)
        response = self.create_open_debit_account_api(request)
        return response.json()

    def create_open_credit_account(self, user_id: str) -> CreateOpenCreditAccountResponseDict:
        request = OpenCreditCardAccountRequestDict(userId=user_id)
        response = self.create_open_credit_account_api(request)
        return response.json()

def build_accounts_gateway_http_client() -> AccountsGatewayHTTPClient:
    return AccountsGatewayHTTPClient(client=build_gateway_http_client())


