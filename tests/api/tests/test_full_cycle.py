import pytest
import requests
import allure

from tests.api.conftest import db_connection
from tests.api.endpoints.authentication import AuthenticateUser
from tests.api.endpoints.operations_with_task import Task
from tests.api.endpoints.create_user import CreateUser
from tests.api.endpoints.get_tasks import GetTasks
from tests.api.payload.payloads import valid_user, valid_new_task, invalid_new_task, updated_task



@pytest.mark.parametrize("payload", [
    ({"username": '', "password": 'secret_sauce1'}, True),  # Empty username
    ({"username": 'locked_out_user1', "password": ''}, True),  # Empty password
    ({"username": 'problem_user1', "password": 'secret_sauce'}, True),  # Valid username, invalid password
    ({"username": '', "password": ''}, True),  # Both fields empty
])



@allure.feature("Users")
@allure.story("Create invalid users")
@allure.severity(allure.severity_level.NORMAL)

def test_failed_new_users(payload):
    with allure.step("Creating user with invalid credentials"):
        create_user = CreateUser()
        create_user.new_user(payload)
    with allure.step("Checking response status is 400"):
        create_user.check_response_is_400(), "User is created"


@allure.feature("Users")
@allure.story("Create a valid user")
@allure.severity(allure.severity_level.CRITICAL)

def test_create_valid_user():
    with allure.step("Creating user with valid credentials"):
        create_valid_user = CreateUser()
        payload = valid_user
        create_valid_user.new_user(payload)
    with allure.step("Checking response status is 201 for a new user"):
        create_valid_user.check_response_is_201(), "Bad request or user exists"


@allure.feature("Authentication")
@allure.story("Authenticate a user")
@allure.severity(allure.severity_level.CRITICAL)

def test_authenticated_user():
    session = requests.Session()
    with allure.step("Logging in with valid credentials"):
        success_login = AuthenticateUser()
        success_login.login_user(valid_user, session)
    with allure.step("Checking response status is 200"):
        success_login.check_response_is_200(), "You are not authenticated"
    allure.attach(str(success_login.get_data()), name="Auth Response", attachment_type=allure.attachment_type.JSON)


@allure.feature("Tasks")
@allure.story("Create an invalid task by authenticated user")
@allure.severity(allure.severity_level.MINOR)

def test_create_invalid_task_by_auth_user():
    session = requests.Session()
    with allure.step("Authenticating user"):
        auth = AuthenticateUser()
        auth.login_user(valid_user, session)
        assert auth.response.status_code == 200, f"Login failed: {auth.response_json}"
    with allure.step("Creating task with invalid data"):
        new_invalid_task_by_auth_user = Task()
        new_invalid_task_by_auth_user.new_task(invalid_new_task, session)
    with allure.step("Checking response status is 400"):
        new_invalid_task_by_auth_user.check_response_is_400(), "Task is successfully created with empty values"
    allure.attach(str(new_invalid_task_by_auth_user.get_data()), name="Task Response", attachment_type=allure.attachment_type.JSON)


@allure.feature("Tasks")
@allure.story("Perform operations on task")
@allure.severity(allure.severity_level.BLOCKER)

def test_operations_with_task_by_auth_user(db_connection):

    session = requests.Session()
    with allure.step("Authenticating user"):
        auth = AuthenticateUser()
        auth.login_user(valid_user, session)
        assert auth.response.status_code == 200, f"Login failed: {auth.response_json}"

    with allure.step("Creating a new task"):
        crud_operations_with_task = Task()
        crud_operations_with_task.new_task(valid_new_task, session)

    with allure.step("Checking task creation response is 201"):
        crud_operations_with_task.check_response_is_201(), "Task is not created"
        task_id = crud_operations_with_task.get_task_id()
        allure.attach(str(task_id), name="Task ID", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Find task in db"):
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM task WHERE id = %s', (task_id,))
        task = cursor.fetchone()
        cursor.close()

        assert task is not None, f'Task with ID {task_id} does not exist in the database'
        print(f"Task found in DB: {task}")

    with allure.step("Getting task details"):
        crud_operations_with_task.get_task_details(session)
        crud_operations_with_task.check_response_is_200(), "Task details are not shown"

    with allure.step("Updating task"):
        crud_operations_with_task.update_task(updated_task, session)
        crud_operations_with_task.check_response_is_200(), "Task is not updated"

    with allure.step("Updating task status"):
        crud_operations_with_task.update_status_task(session)
        crud_operations_with_task.check_response_is_200(), "Task status is not updated"

    with allure.step("Deleting task"):
        crud_operations_with_task.delete_task(session)
        crud_operations_with_task.check_response_is_204(), "Task is not deleted"

@allure.feature("Tasks")
@allure.story("Get all tasks")
@allure.severity(allure.severity_level.NORMAL)

def test_get_tasks():
    session = requests.Session()
    with allure.step("Authenticating user"):
        auth = AuthenticateUser()
        auth.login_user(valid_user, session)
    with allure.step("Fetching all tasks"):
        all_tasks = GetTasks()
        all_tasks.get_tasks(session)
    with allure.step("Checking response status is 200"):
        all_tasks.check_response_is_200(), "Tasks are not displayed"
    allure.attach(str(all_tasks.get_data()), name="Tasks Response", attachment_type=allure.attachment_type.JSON)