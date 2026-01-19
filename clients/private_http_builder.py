from httpx import Client

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema
from pydantic import BaseModel

class AuthenticationUserSchema(BaseModel):
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authentication_client  = get_authentication_client()
    login_request = LoginRequestSchema(email=user.email,
                                       password=user.password)
    login_response = authentication_client.login(request=login_request)
    return Client(
        base_url='https://practice.expandtesting.com/notes/api',
        timeout=100,
        headers={"x-auth-token": f"{login_response.data.token}"}
    )