import pytest
from pydantic import BaseModel

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.public_users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> str:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password


    @property
    def authenticated_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email,
                                        password=self.password)


@pytest.fixture(scope='function')
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request=request)
    return UserFixture(request=request,
                       response=response)


@pytest.fixture(scope='function')
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()


@pytest.fixture(scope='function')
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    return get_private_users_client(function_user.authenticated_user)