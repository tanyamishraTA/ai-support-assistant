from pydantic import BaseModel

class TokenPayload(BaseModel):
    sub: str
    email: str
    role: str