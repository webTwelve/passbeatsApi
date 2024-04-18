from fastapi import APIRouter
from models.user_model import LoginModel
from db_sql import user_sql
from common import result
from utils.password_encipher import encipher
from utils.auto_token import AutoToken
autoToken = AutoToken()
router = APIRouter()


@router.post("/login")
async def login(loginModel: LoginModel):
    data = user_sql.query_user_list(loginModel)
    if not data:
        return result.error(message="用户不存在")
    else:
        if data.pass_word == encipher(loginModel.pass_word):
            return result.ok(message="登录成功", data={
                'token': autoToken.generate_token(data.user_name)
            })
        else:
            return result.error(message="密码错误")
