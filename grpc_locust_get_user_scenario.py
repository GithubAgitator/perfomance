from locust import User, between, task
from clients.grpc.gateway.users.client import UsersGatewayGRPCClient, build_users_locust_gateway_grpc_client
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse


class GetUserScenarioUser(User):
    # Пауза между запросами для каждого виртуального пользователя (в секундах)
    host = "localhost"
    wait_time = between(1, 3)

    # В этой переменной будем хранить данные созданного пользователя
    users_gateway_client: UsersGatewayGRPCClient
    create_user_response: CreateUserResponse

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """

        self.users_gateway_client = build_users_locust_gateway_grpc_client(self.environment)

        self.create_user_response = self.users_gateway_client.create_user()



    @task
    def get_user(self):
        self.users_gateway_client.get_user(self.create_user_response.user.id)
        """
        Основная нагрузочная задача: получение информации о пользователе.
        Здесь мы выполняем GET-запрос к /api/v1/users/{user_id}.
        """

