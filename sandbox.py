import httpx

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.public_users_schema import CreateUserRequestSchema

response = httpx.get('https://practice.expandtesting.com/notes/api/health-check')

print(response.status_code)
print(response.text)


def get_user():
    public_users_client = get_public_users_client()
    create_user_request = CreateUserRequestSchema(
        name='habdfhgawevsdd21dg',
        email='sdkg234nkds2d1dg@test.com',
        password='password'
    )
    create_user_response = public_users_client.create_user_api(create_user_request)
    print(create_user_response.json())

    authentication_user = AuthenticationUserSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )

    private_users_client = get_private_users_client(authentication_user)
    get_user_response = private_users_client.get_user_api()
    print(get_user_response.json())


get_user()