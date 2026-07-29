from locust import User, between, task
from clients.grpc.gateway.operations.client import OperationsGatewayGRPCClient, build_operationa_locust_gateway_grpc_client
from clients.grpc.gateway.cards.client import CardsGatewayGRPCClient, build_cards_locust_gateway_grpc_client
from clients.grpc.gateway.users.client import UsersGatewayGRPCClient, build_users_locust_gateway_grpc_client
from clients.grpc.gateway.accounts.client import AccountsGatewayGRPCClient, build_account_locust_gateway_grpc_client
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import IssueVirtualCardResponse
from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import OpenCreditCardAccountResponse


class GreaterCardsDepositScenarioUser(User):
    # Пауза между запросами для каждого виртуального пользователя (в секундах)
    host = "localhost"
    wait_time = between(1, 3)

    # В этой переменной будем хранить данные созданного пользователя
    operators_gateway_client: OperationsGatewayGRPCClient
    user_gateway_client: UsersGatewayGRPCClient
    credits_account_gateway_client: AccountsGatewayGRPCClient
    cards_gateway_client: CardsGatewayGRPCClient
    user_response: CreateUserResponse
    create_cards_virtual_response: IssueVirtualCardResponse
    open_credits_account: OpenCreditCardAccountResponse


    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """

        self.operators_gateway_client = build_operationa_locust_gateway_grpc_client(self.environment)
        self.user_gateway_client = build_users_locust_gateway_grpc_client(self.environment)
        self.credits_account_gateway_client = build_account_locust_gateway_grpc_client(self.environment)
        self.cards_gateway_client = build_cards_locust_gateway_grpc_client(self.environment)




        self.user_response = self.user_gateway_client.create_user()
        self.create_accounts_response = self.credits_account_gateway_client.open_credit_card(self.user_response.user.id)
        self.create_cards_response = self.cards_gateway_client.issue_virtual_card(self.user_response.user.id, self.create_accounts_response.account.id)



    @task
    def make_free_operations(self):
        self.operators_gateway_client.operations_make_free(self.create_cards_response.card.id, self.create_accounts_response.account.id)


