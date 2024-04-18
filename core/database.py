from sqlalchemy import create_engine
from config import Config
engine = None


def init_db_engine():
    global engine
    if not engine:
        engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(
            Config.username,
            Config.password,
            Config.host,
            Config.port,
            Config.db_name
        ))


class ConnectionPool:
    def __init__(self):
        self.conn = None

    def __enter__(self):
        try:
            self.conn = engine.connect()

        except:
            init_db_engine()
            self.conn = engine.connect()
        finally:
            return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
