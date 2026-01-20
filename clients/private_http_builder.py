from httpx import Client

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema
from pydantic import BaseModel
from config import settings
from clients.event_hooks import log_request_event_hook, log_response_event_hook


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
        base_url=settings.http_client.client_url,
        timeout=settings.http_client.timeout,
        headers={"x-auth-token": f"{login_response.data.token}"},
        event_hooks={
            "request": [log_request_event_hook],
            "response": [log_response_event_hook]
        }
    )