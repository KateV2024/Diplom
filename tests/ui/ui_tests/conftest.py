import pytest
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# Comment line 7 for docker
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    config_driver = webdriver.Chrome(service=service, options=options)
    yield config_driver
    config_driver.quit()

# @pytest.fixture
# def driver():
#     options = Options()
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--headless")
#     options.binary_location = '/usr/bin/google-chrome-stable'
#
#     # Явно указываем путь к ChromeDriver в контейнере
#     service = Service('/usr/local/bin/chromedriver')
#     driver = webdriver.Chrome(service=service, options=options)
#
#     yield driver
#     driver.quit()