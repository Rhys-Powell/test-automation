from os import path
import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, '..','mobile','TheApp.apk')
APPIUM = 'http://127.0.0.1:4723'

@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.device_name = 'Android Emulator'
    options.app = APP
    
    driver = webdriver.Remote(command_executor=APPIUM, options=options)
    yield driver
    driver.quit()