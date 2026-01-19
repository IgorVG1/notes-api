from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake


class PrivateUserDataSchema(BaseModel):
    id: str
    name: str
    email: str
    phone: str | None
    company: str | None


class GetUserResponseSchema(BaseModel):
    success: bool
    status: int
    message: str
    data: PrivateUserDataSchema


class ChangePasswordRequestSchema(BaseModel):
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    current_password: str    = Field(alias='currentPassword')
    new_password: str         = Field(alias='newPassword', default_factory=fake.password)


class ChangePasswordResponseSchema(BaseModel):
    success: bool
    status: int
    message: str


class UpdateUserRequestSchema(BaseModel):
    name: str | None    = Field(default_factory=fake.name)
    phone: str | None   = Field(default_factory=fake.phone)
    company: str | None = Field(default_factory=fake.company)


class UpdateUserResponseSchema(BaseModel):
    success: bool
    status: int
    message: str
    data: PrivateUserDataSchema


class LogoutResponseSchema(BaseModel):
    success: bool
    status: int
    message: str


class DeleteUserResponseSchema(BaseModel):
    success: bool
    status: int
    message: str