from pydantic import BaseModel


class LoginDataSchema(BaseModel):
    id: str
    email: str
    name: str
    token: str


class LoginRequestSchema(BaseModel):
    email: str
    password: str


class LoginResponseSchema(BaseModel):
    success: bool
    status: int
    message: str
    data: LoginDataSchema


class HealthCheckResponseSchema(BaseModel):
    success: bool
    status: int
    message: str