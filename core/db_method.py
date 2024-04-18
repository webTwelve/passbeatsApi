from core.database import init_db_engine, ConnectionPool
from sqlalchemy import text
init_db_engine()

Connection = ConnectionPool()


def query_sql_one(_sql: str):
    with Connection as conn:
        result = conn.execute(text(_sql))
        return result.fetchone()


def query_sql_all(_sql: str):
    with Connection as conn:
        result = conn.execute(text(_sql))
        return result.fetchall()


def save_sql(_sql: str):
    with Connection as conn:
        result = conn.execute(text(_sql))
        conn.commit()
        return result.lastrowid


def update_sql(_sql: str):
    with Connection as conn:
        result = conn.execute(text(_sql))
        return result.lastrowid


def delect_sql(_sql: str):
    with Connection as conn:
        result = conn.execute(text(_sql))
        return result.rowcount
