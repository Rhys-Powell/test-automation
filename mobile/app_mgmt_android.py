from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://127.0.0.1:4723'

# Initialize options instead of using desired_capabilities
options = UiAutomator2Options()
options.platform_name = 'Android'
options.device_name = 'Android Emulator'
options.app = APP

driver = webdriver.Remote(command_executor=APPIUM, options=options)

app = path.join(CUR_DIR, 'ApiDemos-debug.apk')
app_id = 'io.appium.android.apis'
try:
    driver.remove_app(app_id)   
    driver.install_app(app)
    driver.activate_app(app_id)
    driver.terminate_app(app_id)
finally:
    driver.quit()