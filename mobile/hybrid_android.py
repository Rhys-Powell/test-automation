from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path
from appium.options.common import AppiumOptions
from appium.options.android import UiAutomator2Options


CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://127.0.0.1:4723'

options = UiAutomator2Options()
options.platform_name = 'Android'
options.device_name = 'Android Emulator'
options.app = APP

driver = webdriver.Remote(command_executor=APPIUM, options=options)

class webview_active(object):

    def __call__(self, driver):
        for context in driver.contexts:
            if context != 'NATIVE_APP':
                driver.switch_to.context(context)
                return True

        return False

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Webview Demo'))).click()
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@content-desc="urlInput"]'))).send_keys('https://appiumpro.com')
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'navigateBtn').click()
    wait.until(webview_active())
    print(driver.current_url)
    print(driver.title)
finally:
    driver.quit()
