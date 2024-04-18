import jwt
import secrets
from datetime import datetime, timedelta


class AutoToken:
    def __init__(self, secret_key=None, expiration_minutes=30):
        if (secret_key is None):
            self.secret_key = secrets.token_urlsafe(32)
        else:
            self.secret_key = secret_key
        self.expiration_minutes = expiration_minutes

    def generate_token(self, data):
        # 计算过期时间
        expiration_time = datetime.utcnow()+timedelta(minutes=self.expiration_minutes)
        pyload = {
            'unique': data,
            'exp': expiration_time
        }
        token = jwt.encode(pyload, self.secret_key, algorithm='HS256')
        return token

    def get_user_data_from_token(self, token: str):
        try:
            pyload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            data = pyload['unique']
            return data
        except jwt.ExpiredSignatureError:
            # 处理 token 过期
            return "Token has expired"
        except jwt.InvalidTokenError:
            # 处理无效的 token
            return "Invalid token"
