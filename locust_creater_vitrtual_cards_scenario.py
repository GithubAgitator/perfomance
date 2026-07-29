from locust import User, between, task
from clients.http.geteway.accounts.accounts import AccountsGatewayHTTPClient, build_accounts_gateway_locust_http_client
from clients.http.geteway.accounts.schema import CreateOpenDebitAccountResponseSchema
from clients.http.geteway.users.client import UsersGatewayHTTPClient, build_users_gateway_locust_http_client
from clients.http.geteway.users.schema import CreateUserResponseSchema
from clients.http.geteway.cards.cards import CardsGatewayHTTPClient, build_cards_gateway_locust_http_client



class CreateDebitCardsAccountScenario(User):
    host = "localhost"
    # Пауза между запросами для каждого виртуального пользователя (в секундах)
    wait_time = between(1, 3)
    users_gateway_client: UsersGatewayHTTPClient
    debit_account_gateway_client: AccountsGatewayHTTPClient
    cards_virtual_gateway_client: CardsGatewayHTTPClient
    create_user_response: CreateUserResponseSchema
    create_debit_cards_response: CreateOpenDebitAccountResponseSchema

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)
        self.debit_account_gateway_client = build_accounts_gateway_locust_http_client(self.environment)
        self.cards_virtual_gateway_client = build_cards_gateway_locust_http_client(self.environment)

        self.create_user_response = self.users_gateway_client.create_user()

        self.create_debit_cards_response = self.debit_account_gateway_client.create_open_debit_account(self.create_user_response.user.id)


    @task
    def create_virtual_cards(self):
        self.cards_virtual_gateway_client.create_issue_virtual_card(
            self.create_user_response.user.id,
            self.create_debit_cards_response.account.id
        )


