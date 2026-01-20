from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.private_users_schema import GetUserResponseSchema, ChangePasswordRequestSchema, \
    ChangePasswordResponseSchema, UpdateUserRequestSchema, UpdateUserResponseSchema, LogoutResponseSchema, \
    DeleteUserResponseSchema
from httpx import Response

from tools.routes import APIRoutes


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/users после аутентификации
    """
    def get_user_api(self) -> Response:
        """
        Метод запрашивает данные аутентифицированного пользователя.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'{APIRoutes.USERS}/profile')

    def get_user(self) -> GetUserResponseSchema:
        """
        Десериализация pydantic-model из ответа от сервера

        :return: Ответ от сервера в виде pydantic-model
        """
        response = self.get_user_api()
        return GetUserResponseSchema.model_validate_json(response.text)


    def change_password_api(self,
                            request: ChangePasswordRequestSchema
                            ) -> Response:
        """
        Метод замены пароля.

        :param request: Словарь с currentPassword, newPassword.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=f'{APIRoutes.USERS}/change-password',
                         json=request.model_dump(by_alias=True)
                         )

    def change_password(self,
                        request: ChangePasswordRequestSchema
                        ) -> ChangePasswordResponseSchema:
        """
        Десериализация pydantic-model из ответа от сервера

        :param request: Словарь с currentPassword, newPassword.
        :return: Ответ от сервера в виде pydantic-model
        """
        response = self.change_password_api(request=request)
        return ChangePasswordResponseSchema.model_validate_json(response.text)

    def update_user_api(self,
                    request: UpdateUserRequestSchema
                    ) -> Response:
        """
        Метод частичного обновления данных пользователя.

        :param request: Словарь с name, phone, company.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f'{APIRoutes.USERS}/profile',
                          json=request.model_dump())

    def update_user(self,
                    request: UpdateUserRequestSchema
                    ) -> UpdateUserResponseSchema:
        """
        Десериализация pydantic-model из ответа от сервера

        :param request: Словарь с name, phone, company.
        :return: Ответ от сервера в виде pydantic-model
        """
        response = self.update_user_api(request=request)
        return UpdateUserResponseSchema.model_validate_json(response.text)


    def logout_api(self) -> Response:
        """
        Метод выхода из учетной записи.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'{APIRoutes.USERS}/logout')

    def logout(self) -> LogoutResponseSchema:
        """
        Десериализация pydantic-model из ответа от сервера

        :return: Ответ от сервера в виде pydantic-model
        """
        response = self.logout_api()
        return LogoutResponseSchema.model_validate_json(response.text)


    def delete_user_api(self) -> Response:
        """
        Метод удаления учетной записи.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'{APIRoutes.USERS}/delete-account')


    def delete_user(self) -> DeleteUserResponseSchema:
        """
        Десериализация pydantic-model из ответа от сервера

        :return: Ответ от сервера в виде pydantic-model
        """
        response = self.delete_user_api()
        return DeleteUserResponseSchema.model_validate_json(response.text)


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user=user))