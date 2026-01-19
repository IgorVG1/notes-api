from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake


class PublicUserDataSchema(BaseModel):
    id: str
    name: str
    email: str


class CreateUserRequestSchema(BaseModel):
    name: str       = Field(default_factory=fake.name)
    email: str      = Field(default_factory=fake.email)
    password: str   = Field(default_factory=fake.password)


class CreateUserResponseSchema(BaseModel):
    success: bool
    message: str
    data: PublicUserDataSchema


class ForgetPasswordRequestSchema(BaseModel):
    email: str


class ForgetPasswordResponseSchema(BaseModel):
    success: bool
    status: int
    message: str


class VerifyResetPasswordTokenRequestSchema(BaseModel):
    token: str


class VerifyResetPasswordTokenResponseSchema(BaseModel):
    success: bool
    status: int
    message: str


class ResetPasswordRequestSchema(BaseModel):
    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    token: str
    new_password: str    = Field(alias="newPassword")


class ResetPasswordResponseSchema(BaseModel):
    success: bool
    status: int
    message: str