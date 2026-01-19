from httpx import Client


def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(
        base_url='https://practice.expandtesting.com/notes/api',
        timeout=100
    )