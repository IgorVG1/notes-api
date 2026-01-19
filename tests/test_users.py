import pytest

from http import HTTPStatus
from clients.users.public_users_client import get_public_users_client
from clients.users.public_users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
class TestUsers:

    def test_create_user(self):
        public_users_client = get_public_users_client()
        request = CreateUserRequestSchema()
        response = public_users_client.create_user_api(request=request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)


        validate_json_schema(response.json(), response_data.model_json_schema())
