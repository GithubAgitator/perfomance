from locust import User, between, task
from clients.http.geteway.accounts.accounts import AccountsGatewayHTTPClient, build_accounts_gateway_locust_http_client
from clients.http.geteway.accounts.schema import CreateOpenDebitAccountResponseSchema
from clients.http.geteway.documents.documents import DocumentsGatewayHTTPClient, build_documents_gateway_locust_http_client
from clients.http.geteway.users.client import UsersGatewayHTTPClient, build_users_gateway_locust_http_client
from clients.http.geteway.users.schema import CreateUserResponseSchema


class GetDocumentsScenario(User):
    host = "localhost"
    # Пауза между запросами для каждого виртуального пользователя (в секундах)
    wait_time = between(1, 3)
    user_create_gateway_client: UsersGatewayHTTPClient
    debit_account_gateway_client: AccountsGatewayHTTPClient
    documents_gateway_client: DocumentsGatewayHTTPClient
    users_create_response: CreateUserResponseSchema
    create_debit_cards_response: CreateOpenDebitAccountResponseSchema

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        self.user_create_gateway_client = build_users_gateway_locust_http_client(self.environment)
        self.debit_account_gateway_client = build_accounts_gateway_locust_http_client(self.environment)
        self.documents_gateway_client = build_documents_gateway_locust_http_client(self.environment)

        self.users_create_response = self.user_create_gateway_client.create_user()

        self.create_debit_cards_response = self.debit_account_gateway_client.create_open_debit_account(self.users_create_response.user.id)


    @task
    def get_documents_tariff(self):
        self.documents_gateway_client.get_documents_tariff_api(self.create_debit_cards_response.account.id)

