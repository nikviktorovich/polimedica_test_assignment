import os


def get_database_connection_url() -> str:
    """Возвращает строку для подключения к базе данных"""
    db_name = os.environ['POSTGRES_DB']
    username = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    host = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    port = os.environ.get('POSTGRES_PORT', '5432')
    connection_url = f'postgresql://{username}:{password}@{host}:{port}/{db_name}'
    return connection_url
