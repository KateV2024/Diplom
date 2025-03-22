import pytest
import requests
import psycopg2
import os
from tests.api.endpoints.authentication import AuthenticateUser
from tests.api.endpoints.create_user import CreateUser
from tests.api.payload.payloads import valid_user


DB_PARAMS = {
    'dbname': os.environ.get('POSTGRES_DB', 'taskmanager'),
    'user': os.environ.get('POSTGRES_USER', 'postgres'),
    'password': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
    #local
    'host': os.environ.get('POSTGRES_HOST', 'localhost'),
    #Docker
    # 'host': os.environ.get('POSTGRES_HOST', 'db'),
    # 'port': os.environ.get('POSTGRES_PORT', '5432')
}

@pytest.fixture(scope="function")
def db_connection():
    print("🔌 Подключение к БД...")
    conn = psycopg2.connect(**DB_PARAMS)  # Устанавливаем соединение с БД
    yield conn  # Передаем соединение в тест
    conn.close()  # Закрываем соединение после теста
    print("🔌 Соединение с БД закрыто.")

@pytest.fixture
def create_user():
    return CreateUser()


@pytest.fixture
def authenticated_user():
    session = requests.Session()
    auth = AuthenticateUser()
    auth.login_user(valid_user, session)
    auth.check_response_is_200()
    return auth, session

@pytest.fixture(params=[
    (valid_user, True)
])
def test_data(request):
    return request.param