from clients.http.geteway.accounts.schema import CreateOpenSavingsAccountResponseSchema
from clients.http.geteway.locust import GatewayHTTPSequentialTaskSet
from locust import User, between, task

from clients.http.geteway.users.schema import CreateUserResponseSchema


class GetDocumentsSequentialTaskSet(GatewayHTTPSequentialTaskSet):
    create_user_response: CreateUserResponseSchema | None = None
    open_savings_account_response: CreateOpenSavingsAccountResponseSchema | None = None

    @task
    def create_user(self):
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_savings_account(self):
        if not self.create_user_response:
            return
        self.open_savings_account_response = self.accounts_gateway_client.create_open_savings_account(
            user_id=self.create_user_response.user.id
        )

    @task
    def get_documents(self):
        if not self.open_savings_account:
            return
        self.documents_gateway_client.get_documents_contract(
            account_id=self.open_savings_account_response.account.id
        )
        self.documents_gateway_client.get_documents_tariff(
            account_id=self.open_savings_account_response.account.id
        )




class GetDocumentsUser(User):
    host = "localhost"
    tasks = [GetDocumentsSequentialTaskSet]
    wait_time = between(1, 3)

