from typing import Any, Sized



def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус-код.
    :raises AssertionError: Если статус-коды не совпадают.
    """
    assert actual == expected, \
        (
            'Incorrect response status code.'
            f'\nExpected status code:   {expected}'
            f'Actual status code:       {actual}'
        )


def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raise
    """
    assert actual, \
        (
            f'Incorrect value: "{name}"'
            f'\nExpected true value, but actual: {actual}'
        )


def assert_equal(actual: Any, expexted: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """
    assert actual == expexted, \
        (
            f'Incorrect value: "{name}"'
            f'\nExpected value: {expected}'
            f'Actual value:     {actual}'
        )


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    assert len(actual) == len(expected),\
        (
            f'Incorrect object length: "{name}" .'
            f'Expected length: {len(expected)}. '
            f'Actual length: {len(actual)}.'
        )