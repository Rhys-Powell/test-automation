from os import path
from views.home_view import HomeView
import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selenium.webdriver.remote.client_config import ClientConfig
from selenium.webdriver.remote.remote_connection import RemoteConnection

CUR_DIR = path.dirname(path.abspath(__file__))
ANDROID_APP = path.join(CUR_DIR, '..','mobile','TheApp.apk')
IOS_APP = path.join(CUR_DIR, '..','mobile','TheApp.app.zip')

PLATFORMS = {
    'android': {
        'platform_name': 'Android',
        'device_name': 'Android Emulator',
        'app': ANDROID_APP
    },
    'ios': {
        'platform_name': 'iOS',
        'device_name': 'iPhone Simulator',
        'app': IOS_APP
    }
}

def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='android')

@pytest.fixture
def platform(request):
    plat = request.config.getoption('platform').lower()
    if plat not in ['ios', 'android']:
        raise ValueError(f'Unsupported platform: {plat}')
    return plat

# The added ClientConfig parameter is meant to support configurations like timeouts, proxies, and additional client-specific settings that may not have fit neatly into the previous design
client_config = ClientConfig(remote_server_addr = 'http://127.0.0.1:4723')
command_executor = RemoteConnection(client_config=client_config)

@pytest.fixture
def driver(platform):
    options = UiAutomator2Options() if platform == 'android' else "XCUITestOptions()"
    options.platform_name = PLATFORMS[platform]['platform_name']
    options.device_name = PLATFORMS[platform]['device_name']
    options.app = PLATFORMS[platform]['app']

    print("options: ", vars(options))
    driver = webdriver.Remote(command_executor=command_executor, options=options)
    driver._platform = platform
    yield driver
    driver.quit()

@pytest.fixture
def home(driver):
    return HomeView.instance(driver)