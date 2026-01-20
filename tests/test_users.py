import pytest
import allure

from http import HTTPStatus
from clients.users.public_users_client import PublicUsersClient
from clients.users.public_users_schema import CreateUserRequestSchema, CreateUserResponseSchema, \
    CreateInvalidUserResponseSchema
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.severity import AllureSeverity
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_create_user_response_with_invalid_email, \
    assert_create_user_response_with_invalid_password
from testdata.users import INVALID_EMAILS, INVALID_PASSWORDS


@pytest.mark.regression
@pytest.mark.users
@allure.tag(AllureTag.REGRESSION, AllureTag.USERS)
@allure.epic(AllureEpic.NOTES_APP)
@allure.feature(AllureFeature.USERS)
@allure.parent_suite(AllureEpic.NOTES_APP)
@allure.suite(AllureFeature.USERS)
class TestUsers:

    @allure.title("Create user")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(AllureSeverity.BLOCKER)
    def test_create_user(self, public_users_client: PublicUsersClient):
        request = CreateUserRequestSchema()
        response = public_users_client.create_user_api(request=request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_user_response(request=request, response=response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())


    @pytest.mark.parametrize("invalid_email", INVALID_EMAILS)
    @allure.title("Create user with invalid email")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(AllureSeverity.MINOR)
    def test_create_user_with_invalid_email(self, invalid_email: str, public_users_client: PublicUsersClient):
        request = CreateUserRequestSchema(email=invalid_email)
        response = public_users_client.create_user_api(request=request)
        response_data = CreateInvalidUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_create_user_response_with_invalid_email(response=response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())


    @pytest.mark.parametrize("invalid_password", INVALID_PASSWORDS)
    @allure.title("Create user with invalid password")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(AllureSeverity.MINOR)
    def test_create_user_with_invalid_password(self, invalid_password: str, public_users_client: PublicUsersClient):
        request = CreateUserRequestSchema(password=invalid_password)
        response = public_users_client.create_user_api(request=request)
        response_data = CreateInvalidUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_create_user_response_with_invalid_password(response=response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())