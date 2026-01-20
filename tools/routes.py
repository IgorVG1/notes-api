from enum import Enum


class APIRoutes(str, Enum):
    USERS = '/users'
    AUTHENTICATION = '/users'

    def __str__(self):
        return self.value