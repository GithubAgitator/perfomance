from locust import TaskSet, SequentialTaskSet
from clients.grpc.gateway.users.client import UsersGatewayGRPCClient, build_users_locust_gateway_grpc_client
from clients.grpc.gateway.operations.client import OperationsGatewayGRPCClient, build_operationa_locust_gateway_grpc_client
from clients.grpc.gateway.documents.client import DocumetsGatewayGRPCClient, build_documents_locust_gateway_grpc_client
from clients.grpc.gateway.cards.client import CardsGatewayGRPCClient, build_cards_locust_gateway_grpc_client
from clients.grpc.gateway.accounts.client import AccountsGatewayGRPCClient, build_account_locust_gateway_grpc_client
class GatewayGRPCTaskSet(TaskSet):
    users_gateway_client: UsersGatewayGRPCClient
    operations_gateway_client: OperationsGatewayGRPCClient
    documents_gateway_client: DocumetsGatewayGRPCClient
    cards_gateway_client: CardsGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient
    def on_start(self) -> None:
        self.users_gateway_client = build_users_locust_gateway_grpc_client(self.user.environment)
        self.operations_gateway_client = build_operationa_locust_gateway_grpc_client(self.user.environment)
        self.documents_gateway_client = build_documents_locust_gateway_grpc_client(self.user.environment)
        self.cards_gateway_client = build_cards_locust_gateway_grpc_client(self.user.environment)
        self.accounts_gateway_client = build_account_locust_gateway_grpc_client(self.user.environment)


class GatewayGRPCSequentialTaskSet(SequentialTaskSet):
    users_gateway_client: UsersGatewayGRPCClient
    operations_gateway_client: OperationsGatewayGRPCClient
    documents_gateway_client: DocumetsGatewayGRPCClient
    cards_gateway_client: CardsGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient

    def on_start(self) -> None:
        self.users_gateway_client = build_users_locust_gateway_grpc_client(self.user.environment)
        self.operations_gateway_client = build_operationa_locust_gateway_grpc_client(self.user.environment)
        self.documents_gateway_client = build_documents_locust_gateway_grpc_client(self.user.environment)
        self.cards_gateway_client = build_cards_locust_gateway_grpc_client(self.user.environment)
        self.accounts_gateway_client = build_account_locust_gateway_grpc_client(self.user.environment)