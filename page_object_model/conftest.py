from os import path
from views.home_view import HomeView
import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selenium.webdriver.remote.client_config import ClientConfig
from selenium.webdriver.remote.remote_connection import RemoteConnection

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, '..','mobile','TheApp.apk')

# The added ClientConfig parameter is meant to support configurations like timeouts, proxies, and additional client-specific settings that may not have fit neatly into the previous design
client_config = ClientConfig(remote_server_addr = 'http://127.0.0.1:4723')
command_executor = RemoteConnection(client_config=client_config)

@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.device_name = 'Android Emulator'
    options.app = APP
    
    driver = webdriver.Remote(command_executor=command_executor, options=options)
    yield driver
    driver.quit()

@pytest.fixture
def home(driver):
    return HomeView(driver)