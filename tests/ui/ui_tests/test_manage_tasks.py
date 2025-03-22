import allure
from tests.ui.pages.login_page import LoginPage
from tests.ui.pages.tasks_page import TasksPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@allure.feature("Operations with tasks")
@allure.story("Task creation")
@allure.severity(allure.severity_level.CRITICAL)

def test_user_creates_new_task(driver):
    username = "kate11"
    password = "kate11"
    title = "ola1"
    description = "desc1"

    with allure.step("Navigate to the login page and authenticate"):
        user_on_tasks = LoginPage(driver)
        user_on_tasks.get_login_page()
        user_on_tasks.authenticated_user(username, password)

    with allure.step("Verify successful login"):
        tasks = TasksPage(driver)
        tasks.get_success_message()
        assert "Вы успешно вошли в систему" in tasks.get_success_message(), "User is not authorized"

    with allure.step("Create a new task"):
        tasks.click_new_task_btn()
        assert "create" in driver.current_url, "User is not on the new task creation page"
        tasks.enter_new_task_title(title)
        tasks.enter_new_task_description(description)
        tasks.submit_task()

    with allure.step("Check user is redirected to tasks page"):
        assert "tasks" in driver.current_url, "User is not on tasks page"

    with allure.step("Check user received success message that new task was created"):
        assert "Задача успешно создана" in tasks.get_success_message(), "User is not on tasks page"

    with allure.step("Check user created task with correct title"):
        assert title in tasks.check_task_title(), "User didn't create task with correct title"

@allure.feature("Operations with tasks")
@allure.story("Check task duplicates")
@allure.severity(allure.severity_level.NORMAL)

def test_user_creates_task_duplicate(driver):
    username = "kate11"
    password = "kate11"
    title = "ola1"
    description = "desc1"

    with allure.step("Navigate to the login page and authenticate"):
        user_on_tasks = LoginPage(driver)
        user_on_tasks.get_login_page()
        user_on_tasks.authenticated_user(username, password)

    with allure.step("Verify successful login"):
        tasks = TasksPage(driver)
        tasks.get_success_message()
        assert "Вы успешно вошли в систему" in tasks.get_success_message(), "User is not authorized"

    with allure.step("Create a task with the same title and description"):
        tasks.click_new_task_btn()
        assert "create" in driver.current_url, "User is not on the new task creation page"
        tasks.enter_new_task_title(title)
        tasks.enter_new_task_description(description)
        tasks.submit_task()

        task_count = tasks.count_tasks_with_title_duplicate(title)
        assert task_count == 1, f"Duplicate task found! Expected 1, but found {task_count}"


@allure.feature("Operations with tasks")
@allure.story("Check task details")
@allure.severity(allure.severity_level.NORMAL)

def test_user_get_task_details(driver):
    username = "kate11"
    password = "kate11"
    title = "ola2"
    description = "desc2"

    with allure.step("Navigate to the login page and authenticate"):
        user_on_tasks = LoginPage(driver)
        user_on_tasks.get_login_page()
        user_on_tasks.authenticated_user(username, password)

    with allure.step("Verify successful login"):
        tasks = TasksPage(driver)
        tasks.get_success_message()
        assert "Вы успешно вошли в систему" in tasks.get_success_message(), "User is not authorized"

    with allure.step("Create a new task"):
        tasks.click_new_task_btn()
        assert "create" in driver.current_url, "User is not on the new task creation page"
        tasks.enter_new_task_title(title)
        tasks.enter_new_task_description(description)
        tasks.submit_task()

    with allure.step("Move to task details"):
        tasks.get_task_details()
        tasks.check_task_status_btn()
        assert tasks.check_task_status_btn(), "User is not on the task details page"

def test_user_updates_task(driver):
    username = "kate11"
    password = "kate11"
    title = "ola3"
    description = "desc3"
    new_description = "updated description"

    with allure.step("Navigate to the login page and authenticate"):
        user_on_tasks = LoginPage(driver)
        user_on_tasks.get_login_page()
        user_on_tasks.authenticated_user(username, password)

    with allure.step("Verify successful login"):
        tasks = TasksPage(driver)
        tasks.get_success_message()
        assert "Вы успешно вошли в систему" in tasks.get_success_message(), "User is not authorized"

    with allure.step("Create a new task"):
        tasks.click_new_task_btn()
        assert "create" in driver.current_url, "User is not on the new task creation page"
        tasks.enter_new_task_title(title)
        tasks.enter_new_task_description(description)
        tasks.submit_task()

    with allure.step("Move to task details"):
        tasks.get_task_details()
        tasks.check_task_status_btn()
        assert tasks.check_task_status_btn(), "User is not on the task details page"

    with allure.step("Move to edit task page"):
        tasks.click_edit_btn()
        assert "edit" in driver.current_url, "User is not on the edit task page"

    with allure.step("edit task description and mark task done"):
        tasks.enter_new_task_description(new_description)
        tasks.mark_task_done()
        tasks.submit_task()
        WebDriverWait(driver, 10).until(EC.url_contains("tasks"))

    with allure.step("check task description is updated and marked as done"):
        assert new_description in tasks.check_task_description()
        assert tasks.check_done_task()

def test_user_deletes_task(driver):
    username = "kate11"
    password = "kate11"
    title = "ola4"
    description = "desc4"

    with allure.step("Navigate to the login page and authenticate"):
        user_on_tasks = LoginPage(driver)
        user_on_tasks.get_login_page()
        user_on_tasks.authenticated_user(username, password)

    with allure.step("Verify successful login"):
        tasks = TasksPage(driver)
        tasks.get_success_message()
        assert "Вы успешно вошли в систему" in tasks.get_success_message(), "User is not authorized"

    with allure.step("Create a new task"):
        tasks.click_new_task_btn()
        assert "create" in driver.current_url, "User is not on the new task creation page"
        tasks.enter_new_task_title(title)
        tasks.enter_new_task_description(description)
        tasks.submit_task()

    with allure.step("Delete task"):
        tasks.delete_task()
        assert "Задача успешно удалена" in tasks.get_success_message()