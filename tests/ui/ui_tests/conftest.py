import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager # Comment for docker

# Fixture for local testing
# @pytest.fixture
# def driver():
#     options = Options()
#     options.add_argument("--start-maximized")
#     service = Service(ChromeDriverManager().install())
#     config_driver = webdriver.Chrome(service=service, options=options)
#     yield config_driver
#     config_driver.quit()

# Fixture for docker
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    options.binary_location = '/usr/bin/google-chrome-stable'

    # Явно указываем путь к ChromeDriver в контейнере
    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()