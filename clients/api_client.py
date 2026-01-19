from typing import Any
from httpx import Client, URL, QueryParams, Response
from httpx._types import RequestData, RequestFiles


class APIClient:
    def __init__(self, client: Client):
        """
        Базовый API клиент, принимающий объект httpx.Client.

        :param client: экземпляр httpx.Client для выполнения HTTP-запросов
        """
        self.client = client


    def get(self,
            url: str | URL,
            params: QueryParams | None = None
            ) -> Response:
        """
        Выполняет GET-запрос.

        :param url: URL-адрес эндпоинта.
        :param params: GET-параметры запроса (например, ?key=value).
        :return: Объект Response с данными ответа.
        """
        return self.client.get(
            url=url,
            params=params
        )


    def post(self,
             url: str | URL,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None
             ) -> Response:
        """
        Выполняет POST-запрос.

        :param url: URL-адрес эндпоинта.
        :param json: Данные в формате JSON.
        :param data: Форматированные данные формы (например, application/x-www-form-urlencoded).
        :param files: Файлы для загрузки на сервер.
        :return: Объект Response с данными ответа.
        """
        return self.client.post(
            url=url,
            json=json,
            data=data,
            files=files
        )


    def put(self,
            url: str | URL,
            json: Any
            ) -> Response:
        """
        Выполняет PUT-запрос (полное обновление данных).

        :param url: URL-адрес эндпоинта.
        :param json: Данные для обновления в формате JSON.
        :return: Объект Response с данными ответа.
        """
        return self.client.put(
            url=url,
            json=json
        )


    def patch(self,
              url: str | URL,
              json: Any | None = None
              ) -> Response:
        """
        Выполняет PATCH-запрос (частичное обновление данных).

        :param url: URL-адрес эндпоинта.
        :param json: Данные для обновления в формате JSON.
        :return: Объект Response с данными ответа.
        """
        return self.client.patch(
            url=url,
            json=json
        )


    def delete(self,
               url: str | URL
               ) -> Response:
        """
        Выполняет DELETE-запрос (удаление данных).

        :param url: URL-адрес эндпоинта.
        :return: Объект Response с данными ответа.
        """
        return self.client.delete(url=url)