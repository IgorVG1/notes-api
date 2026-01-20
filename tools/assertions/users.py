from clients.users.public_users_schema import CreateUserRequestSchema, CreateUserResponseSchema, \
    CreateInvalidUserResponseSchema
from tools.assertions.base import assert_equal
from tools.logger import get_logger

logger = get_logger("USERS_ASSERTIONS")


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check create user response')
    assert_equal(response.data.name, request.name, 'name')
    assert_equal(response.data.email, request.email, 'email')
    assert_equal(response.success, True, 'success')
    assert_equal(response.status, 201, 'status')
    assert_equal(response.message, 'User account created successfully', 'message')


def assert_create_user_response_with_invalid_email(response: CreateInvalidUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя с невалидным email соответствует запросу.

    :param request: Исходный некорректный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check create user response with invalid email')
    assert_equal(response.success, False, 'success')
    assert_equal(response.status, 400, 'status')
    assert_equal(response.message, 'A valid email address is required', 'message')


def assert_create_user_response_with_invalid_password(response: CreateInvalidUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя с невалидным password соответствует запросу.

    :param request: Исходный некорректный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check create user response with invalid password')
    assert_equal(response.success, False, 'success')
    assert_equal(response.status, 400, 'status')
    assert_equal(response.message, 'Password must be between 6 and 30 characters', 'message')