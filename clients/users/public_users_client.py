from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.public_users_schema import CreateUserRequestSchema, CreateUserResponseSchema, ForgetPasswordRequestSchema, \
    ForgetPasswordResponseSchema, VerifyResetPasswordTokenRequestSchema, VerifyResetPasswordTokenResponseSchema, \
    ResetPasswordRequestSchema, ResetPasswordResponseSchema
from tools.routes import APIRoutes


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/users без аутентификации
    """
    def create_user_api(self,
                        request: CreateUserRequestSchema
                        ) -> Response:
        """
        Метод создает пользователя.

        :param request: Словарь с name, email, password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url=f'{APIRoutes.USERS}/register',
            json=request.model_dump()
        )

    def create_user(self,
                    request: CreateUserRequestSchema
                    ) -> CreateUserResponseSchema:
        """
        Десериализация pydantic-model из ответа от сервера

        :param request: Словарь с name, email, password.
        :return: Ответ от сервера в виде pydantic-model
        """
        response = self.create_user_api(request=request)
        return CreateUserResponseSchema.model_validate_json(response.text)


    def forget_password_api(self,
                            request: ForgetPasswordRequestSchema
                            ) -> Response:
        """
        Метод запрашивает ссылку для смены пароля на email.

        :param request: Словарь с email.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=f'{APIRoutes.USERS}/forgot-password',
                         json=request.model_dump()
                         )

    def forget_password(self,
                        request: ForgetPasswordRequestSchema
                        ) -> ForgetPasswordResponseSchema:
        """
        Десериализация pydantic-model из ответа от сервера

        :param request: Словарь с email.
        :return: Ответ от сервера в виде pydantic-model
        """
        response = self.forget_password_api(request=request)
        return ForgetPasswordResponseSchema.model_validate_json(response.text)


    def verify_reset_password_token_api(self,
                                        request: VerifyResetPasswordTokenRequestSchema
                                        ) -> Response:
        """
        Метод проверяет предоставленный токен для смены пароля

        :param request: Словарь с token.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=f'{APIRoutes.USERS}/verify-reset-password-token',
                         json=request.model_dump()
                         )

    def verify_reset_password_token(self,
                                    request: VerifyResetPasswordTokenRequestSchema
                                    ) -> VerifyResetPasswordTokenResponseSchema:
        """
        Десериализация pydantic-model из ответа от сервера

        :param request: Словарь с token.
        :return: Ответ от сервера в виде pydantic-model
        """
        response = self.verify_reset_password_token_api(request=request)
        return VerifyResetPasswordTokenResponseSchema.model_validate_json(response.text)


    def reset_password_api(self,
                           request: ResetPasswordRequestSchema
                           ) -> Response:
        """
        Метод смены пароля

        :param request: Словарь с token, newPassword.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=f'{APIRoutes.USERS}/reset-password',
                         json=request.model_dump(by_alias=True)
                         )

    def reset_password(self,
                       request: ResetPasswordRequestSchema
                       ) -> ResetPasswordResponseSchema:
        """
        Десериализация pydantic-model из ответа от сервера

        :param request: Словарь с token, newPassword.
        :return: Ответ от сервера в виде pydantic-model
        """
        response = self.reset_password_api(request=request)
        return ResetPasswordResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())