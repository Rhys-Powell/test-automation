# Seems to be able to run two separate Appium server instances and run tests in parallel on two emulated Android devices, udid of each device is required in options param for webdriver.Remote

from os import path
from views.home_view import HomeView
import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver

CUR_DIR = path.dirname(path.abspath(__file__))
ANDROID_APP = path.join(CUR_DIR, '..', 'mobile', 'TheApp.apk')
IOS_APP = path.join(CUR_DIR, '..', 'mobile', 'TheApp.app.zip')

ANDROID_CAPS = [
    {
        'platform_name': 'Android',
        'udid': 'emulator-5554',
        'app': ANDROID_APP
    },
    {
        'platform_name': 'Android',
        'udid': 'emulator-5556',
        'app': ANDROID_APP,
    }
]

IOS_CAPS = [
    {
        'platform_name': 'iOS',
        'device_name': 'iPhone Simulator',
        'app': IOS_APP
    }
]

APPIUMS = ['http://127.0.0.1:4705', 'http://127.0.0.1:4707']

def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='android')

@pytest.fixture
def worker_num(worker_id):
    if worker_id == 'master':
        worker_id = 'gw0'
    print("worker_num", int(worker_id[2:]))    
    return int(worker_id[2:])  

@pytest.fixture
def server(worker_num):
    if worker_num >= len(APPIUMS):
        raise Exception('Too many workers for the number of Appium servers')
    print("server", APPIUMS[worker_num])  
    return APPIUMS[worker_num]

@pytest.fixture
def platform(request):
    plat = request.config.getoption('platform').lower()
    if plat not in ['ios', 'android']:
        raise ValueError(f'Unsupported platform: {plat}')
    return plat

@pytest.fixture
def caps(platform, worker_num):
    cap_set = ANDROID_CAPS if platform == 'android' else IOS_CAPS
    if worker_num >= len(cap_set):
        raise Exception('Too many workers for the number of capability sets')
    print("caps", cap_set[worker_num])
    return cap_set[worker_num]

@pytest.fixture
def driver(caps, platform, server):
    if platform == 'android':
        options = UiAutomator2Options()
    else: 
        # options = XCUITestOptions()
        pass

    options.platform_name = caps['platform_name']
    options.app = caps['app']
    options.udid = caps['udid']

    # print("server in driver fixture: ", server)
    print("caps in driver fixture: ", caps)
    driver = webdriver.Remote(command_executor=server, options=options)
    driver._platform = platform
    yield driver
    driver.quit()


@pytest.fixture
def home(driver):
    return HomeView.instance(driver)
