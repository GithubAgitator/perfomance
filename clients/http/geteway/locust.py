from locust import TaskSet, SequentialTaskSet
from clients.http.geteway.users.client import UsersGatewayHTTPClient, build_users_gateway_locust_http_client
from clients.http.geteway.operations.operations import OperationsGatewayHTTPClient, build_operations_gateway_locust_http_client
from clients.http.geteway.documents.documents import DocumentsGatewayHTTPClient, build_documents_gateway_locust_http_client
from clients.http.geteway.cards.cards import CardsGatewayHTTPClient, build_cards_gateway_locust_http_client
from clients.http.geteway.accounts.accounts import AccountsGatewayHTTPClient, build_accounts_gateway_locust_http_client
class GatewayHTTPTaskSet(TaskSet):
    users_gateway_client: UsersGatewayHTTPClient
    operations_gateway_client: OperationsGatewayHTTPClient
    documents_gateway_client: DocumentsGatewayHTTPClient
    cards_gateway_client: CardsGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient
    def on_start(self) -> None:
        self.users_gateway_client = build_users_gateway_locust_http_client(self.user.environment)
        self.operations_gateway_client = build_operations_gateway_locust_http_client(self.user.environment)
        self.documents_gateway_client = build_documents_gateway_locust_http_client(self.user.environment)
        self.cards_gateway_client = build_cards_gateway_locust_http_client(self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.user.environment)


class GatewayHTTPSequentialTaskSet(SequentialTaskSet):
    users_gateway_client: UsersGatewayHTTPClient
    operations_gateway_client: OperationsGatewayHTTPClient
    documents_gateway_client: DocumentsGatewayHTTPClient
    cards_gateway_client: CardsGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient

    def on_start(self) -> None:
        self.users_gateway_client = build_users_gateway_locust_http_client(self.user.environment)
        self.operations_gateway_client = build_operations_gateway_locust_http_client(self.user.environment)
        self.documents_gateway_client = build_documents_gateway_locust_http_client(self.user.environment)
        self.cards_gateway_client = build_cards_gateway_locust_http_client(self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.user.environment)
