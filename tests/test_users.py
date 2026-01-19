
from http import HTTPStatus
from clients.users.public_users_client import get_public_users_client
from clients.users.public_users_schema import CreateUserRequestSchema


class TestUsers:

    def test_create_user(self):
        public_users_client = get_public_users_client()
        request = CreateUserRequestSchema()
        response = public_users_client.create_user_api(request=request)

        assert response.status_code == HTTPStatus.CREATED