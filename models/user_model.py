from pydantic import BaseModel


class LoginModel(BaseModel):
    user_name: str
    pass_word: str
