from fastapi import APIRouter
from models.user_model import LoginModel
from db_sql import user_sql
from common import result
from utils.password_encipher import encipher
import re
router = APIRouter()


@router.post("/signin/")
async def signin(loginModel: LoginModel):
    data = user_sql.query_user_list(loginModel)
    if data:
        return result.error(message="用户已存在")
    else:
        pattern = r'^(?![\u4e00-\u9fa5]).{6,12}$'
        if not re.match(pattern, loginModel.pass_word):
            return result.error(message="密码必须大于6位小于12位且不能包含中文字符")
        else:
            loginModel.pass_word = encipher(loginModel.pass_word)
            a = user_sql.save_user(loginModel)
            print(a)
            return result.ok(message="注册成功", data=True)
