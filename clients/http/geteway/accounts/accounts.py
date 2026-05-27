from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from clients.http.geteway.accounts.schema import GetAccountQuerySchema, OpenDepositAccountRequestSchema, \
    OpenSavingsAccountRequestSchema, OpenDebitCardAccountRequestSchema, OpenCreditCardAccountRequestSchema, \
    GetAccountResponseSchema, CreateOpenDepositAccountResponseSchema, CreateOpenSavingsAccountResponseSchema, \
    CreateOpenDebitAccountResponseSchema, CreateOpenCreditAccountResponseSchema
from clients.http.geteway.client import build_gateway_http_client



class AccountsGatewayHTTPClient(HTTPClient):
    """Получение аккаунта"""
    def get_account_api(self, query: GetAccountQuerySchema) -> Response:
        return self.get(f"/api/v1/accounts", params=QueryParams(**query.model_dump(by_alias=True)))

    """Создание депозитной карты"""
    def create_open_deposit_account_api(self, request: OpenDepositAccountRequestSchema) -> Response:
        return self.post("/api/v1/accounts/open-deposit-account", json=request.model_dump(by_alias=True))

    """Создание saving карты"""
    def create_open_savings_account_api(self, request: OpenSavingsAccountRequestSchema) -> Response:
        return self.post("/api/v1/accounts/open-savings-account", json=request.model_dump(by_alias=True))

    """Создание debit карты"""
    def create_open_debit_account_api(self, request: OpenDebitCardAccountRequestSchema) -> Response:
        return self.post("/api/v1/accounts/open-debit-card-account", json=request.model_dump(by_alias=True))

    """Создание credit карты"""
    def create_open_credit_account_api(self, request: OpenCreditCardAccountRequestSchema) -> Response:
        return self.post("/api/v1/accounts/open-credit-card-account", json=request.model_dump(by_alias=True))

    def get_account(self, user_id: str) -> GetAccountResponseSchema:
        query = GetAccountQuerySchema(user_id=user_id)
        response = self.get_account_api(query=query)
        return GetAccountResponseSchema.model_validate_json(response.text)

    def create_open_deposit_account(self, user_id: str) -> CreateOpenDepositAccountResponseSchema:
        request = OpenDepositAccountRequestSchema(user_id=user_id)
        response = self.create_open_deposit_account_api(request)
        return CreateOpenDepositAccountResponseSchema.model_validate_json(response.text)

    def create_open_savings_account(self, user_id: str) -> CreateOpenSavingsAccountResponseSchema:
        request = OpenSavingsAccountRequestSchema(user_id=user_id)
        response = self.create_open_savings_account_api(request)
        return CreateOpenSavingsAccountResponseSchema.model_validate_json(response.text)

    def create_open_debit_account(self, user_id: str) -> CreateOpenDebitAccountResponseSchema:
        request = OpenDebitCardAccountRequestSchema(user_id=user_id)
        response = self.create_open_debit_account_api(request)
        return CreateOpenDebitAccountResponseSchema.model_validate_json(response.text)

    def create_open_credit_account(self, user_id: str) -> CreateOpenCreditAccountResponseSchema:
        request = OpenCreditCardAccountRequestSchema(user_id=user_id)
        response = self.create_open_credit_account_api(request)
        return CreateOpenCreditAccountResponseSchema.model_validate_json(response.text)

def build_accounts_gateway_http_client() -> AccountsGatewayHTTPClient:
    return AccountsGatewayHTTPClient(client=build_gateway_http_client())


