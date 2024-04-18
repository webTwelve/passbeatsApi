import os
import importlib.util
import pkgutil

from fastapi import APIRouter
api_router = APIRouter()


def load_routes():
    current_dir = os.path.dirname(__file__)
    files = [f for f in os.listdir(current_dir) if os.path.isdir(
        os.path.join(current_dir, f)) and f != '__pycache__' and f != '__init__.py']
    for file in files:
        for (_, name, ispkg) in pkgutil.iter_modules([current_dir+'/'+file]):
            if not ispkg:
                module = importlib.import_module(f"api.{file}.{name}")
                api_router.include_router(
                    module.router, prefix='', tags=[name])


load_routes()
