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
    driver.quit()


TEST_PROFILE_PHONE = '71231231237'
TEST_PROFILE_MAIL = 'qct38003@xcoxc.com'
TEST_PROFILE_LOGIN = "ktox_ui"
TEST_PROFILE_PASSWORD = "123123123"

EMPTY_PERSONAL_COLLECTION_ID = '92991'
EMPTY_PROFILE_COLLECTION_ID = '92990'

PROFILE_COLLECTION_ID = '92992'
PERSONAL_COLLECTION_ID = '92993'

CHILD_PERSONAL_COLLECTION_ID = '92995'
CHILD_PROFILE_COLLECTION_ID = '92994'

DENCHIG_ID = 15
KTOX_ID = 22250

MAX_COLLECTIONS_COUNT = 9
MAX_OBJECTS_COUNT = 99
BASE_URL = 'https://stage-web.pfm.team'
