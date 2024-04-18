from models.user_model import LoginModel
from core import db_method as db


def query_user_list(loginModel: LoginModel):
    print('====')
    query_sql = "SELECT * FROM user WHERE user_name = '%s'" % (
        loginModel.user_name)
    return db.query_sql_one(query_sql)


def save_user(loginModel: LoginModel):
    query_sql = "INSERT INTO user (user_name,pass_word) VALUES ('%s' ,'%s')" % (
        loginModel.user_name, loginModel.pass_word)
    return db.save_sql(query_sql)
