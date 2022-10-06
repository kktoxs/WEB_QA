import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    # time.sleep(10)
    driver.quit()


KTOX_ID = 23475
DENCHIG_ID = 15
BASE_URL = 'https://planetfor.me'
#  BASE_URL = 'https://stage-web.pfm.team'
