from pydantic import Field
from pydantic import BaseModel

class LoginResponse(BaseModel):
    user_id: int
    name: str
    role_id: int
    roles: list[str] = Field(default_factory=list)
