import os
from dotenv import load_dotenv
from core.resource.resource_connection import ResourceConnection

load_dotenv()


def create(
        user: str = os.getenv('USER'),
        password: str = os.getenv('PASSWORD'),
        host: str = os.getenv('HOST'),
        database: str = os.getenv('DATABASE')
) -> ResourceConnection:
    return ResourceConnection(
        user=user,
        password=password,
        host=host,
        database=database
    )
