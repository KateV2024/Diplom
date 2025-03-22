import pytest
import allure
from tests.ui.pages.register_page import RegisterPage
from tests.ui.pages.login_page import LoginPage
from tests.ui.pages.tasks_page import TasksPage


@pytest.mark.parametrize(
    "username, password",
    [
        ('423025', '411111'),
        ('', 'password'),
        ('979597', ''),
        ('', ''),
        ('4', '48998987')
    ]
)

@allure.feature("User Registration")
@allure.story("Register User with Different Credentials")
@allure.severity(allure.severity_level.CRITICAL)

def test_register_user(driver, username, password):
    with allure.step("Navigate to the registration page"):
        register_user = RegisterPage(driver)
        register_user.get_register_page()
        assert "register" in driver.current_url, "User is not on the registration page"

    with allure.step("Enter username and password"):
        register_user.enter_username(username)
        register_user.enter_password(password)

    with allure.step("Click the register button"):
        register_user.click_register()

    with allure.step("Validate registration outcome"):
        if username == '':
            assert register_user.get_error_message(), "Registration without username"
        elif password == '':
            assert "Пароль обязателен" in register_user.get_error_message(), "Registration without password"
        elif password == '' and username == '':
            assert "Пароль обязателен" in register_user.get_error_message(), "Registration without password"
            assert "Имя пользователя обязательно" in register_user.get_error_message(), "Registration without username"
        elif len(password) < 6 and len(username) < 3:
            assert "Пароль должен содержать не менее 6 символов" in register_user.get_error_message(), \
                "Registration with short password"
            assert "Имя пользователя должно содержать не менее 3 символов" in register_user.get_error_message(), \
                "Registration with short username"
        elif len(password) < 6:
            assert "Пароль должен содержать не менее 6 символов" in register_user.get_error_message(), \
                "Registration with short password"
        elif len(username) < 3:
            assert "Имя пользователя должно содержать не менее 3 символов" in register_user.get_error_message(), \
                "Registration with short username"
        else:
            assert register_user.get_success_message(), "User is not registered"

    allure.attach(driver.get_screenshot_as_png(), name="Registration_Result", attachment_type=allure.attachment_type.PNG)
    print("Registration test is completed")


@pytest.mark.parametrize(
    "username, password",
    [
        ('423025', '411111'),
        ('', 'password'),
        ('username', ''),
        ('', '')
    ]
)

@allure.feature("User Login")
@allure.story("Login User with Different Credentials")
@allure.severity(allure.severity_level.CRITICAL)

def test_login_user(driver, username, password):
    with allure.step("Navigate to the login page"):
        logged_user = LoginPage(driver)
        logged_user.get_login_page()
        assert "login" in driver.current_url, "User is not on the login page"

    with allure.step("Enter username and password"):
        logged_user.enter_username(username)
        logged_user.enter_password(password)

    with allure.step("Click the login button"):
        logged_user.click_login()

    with allure.step("Validate login outcome"):
        if username == '':
            assert logged_user.get_error_message(), "Authentication without username"
        elif password == '':
            assert "Пароль обязателен" in logged_user.get_error_message(), "Authentication without password"
        elif password == '' and username == '':
            assert "Пароль обязателен" in logged_user.get_error_message(), "Authentication without password"
            assert "Имя пользователя обязательно" in logged_user.get_error_message(), "Authentication without username"
        else:
            assert logged_user.get_success_message(), "User is not authenticated"

    allure.attach(driver.get_screenshot_as_png(), name="Login_Result", attachment_type=allure.attachment_type.PNG)
    print("Login test is completed")

@allure.feature("User Tasks")
@allure.story("User Logout and Task Verification")
@allure.severity(allure.severity_level.CRITICAL)

def test_user_on_tasks(driver):
    username = "kate11"
    password = "kate11"

    with allure.step("Navigate to the login page and authenticate"):
        user_on_tasks = LoginPage(driver)
        user_on_tasks.get_login_page()
        user_on_tasks.authenticated_user(username, password)

    with allure.step("Verify successful login"):
        tasks = TasksPage(driver)
        tasks.get_success_message()
        assert "Вы успешно вошли в систему" in tasks.get_success_message(), "User is not authorized"

    with allure.step("Verify username in logout section"):
        tasks.find_username_in_logout()
        assert username in tasks.find_username_in_logout(), "Another user is authorized"

    with allure.step("Logout and verify logout message"):
        tasks.log_out()
        tasks.find_info_message()
        assert "Вы вышли из системы" in tasks.find_info_message(), "User didn't log out"
        assert "login" in driver.current_url, "User is not on the login page"
        allure.attach(driver.get_screenshot_as_png(), name="Logout_Result", attachment_type=allure.attachment_type.PNG)
        print("Tasks and logout test is completed")