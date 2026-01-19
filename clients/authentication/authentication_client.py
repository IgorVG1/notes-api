from httpx import Response

from clients.api_client import APIClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema, \
    HealthCheckResponseSchema
from clients.public_http_builder import get_public_http_client


class AuthenticationClient(APIClient):
    """
    Клиент для аутентификации пользователя
    """
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url='/users/login',
            json=request.model_dump()
        )

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        """
        Аутентификация пользователя и десериализация pydantic-model из ответа от сервера

        :param request: Словарь с email и password
        :return: Ответ от сервера в виде pydantic-model
        """
        response = self.login_api(request=request)
        return LoginResponseSchema.model_validate_json(response.text)


    def health_check_api(self):
        """
        Метод проверяет статус работы сервера.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url='/health-check')

    def health_check(self):
        """
        Десериализация pydantic-model из ответа от сервера

        :return: Ответ от сервера в виде pydantic-model
        """
        response = self.health_check_api()
        return HealthCheckResponseSchema.model_validate_json(response.text)


def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(get_public_http_client())