import time
from httpx import Response
from typing import TypedDict
from clients.http.client import HTTPClient
from clients.http.geteway.client import build_gateway_http_client


# Добавили описание структуры пользователя
class UserDict(TypedDict):
    """
    Описание структуры пользователя ответа.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str

class CreateUserRequestDict(TypedDict):
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str

# Добавили описание структуры ответа получения пользователя
class GetUserResponseDict(TypedDict):
    """
    Описание структуры ответа получения пользователя.
    """
    user: UserDict

# Добавили описание структуры ответа создания пользователя
class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserDict

class UsersGatewayHTTPClient(HTTPClient):
    def get_user_api(self, user_id: str) -> Response:
        return self.get(f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        return self.post("/api/v1/users", json=request)

    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_user_api(user_id)
        return response.json()

    def create_user(self) -> CreateUserResponseDict:
        request = CreateUserRequestDict(
            email=f"fd{time.time()}@mail.com",
            lastName="Ivan",
            firstName="Ivanov",
            middleName="Ivanovich",
            phoneNumber="12345"
        )
        response = self.create_user_api(request)
        return response.json()



def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    return UsersGatewayHTTPClient(client=build_gateway_http_client())

