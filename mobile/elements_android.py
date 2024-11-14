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

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
    wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'messageInput'))).send_keys('Hello')
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'messageSaveBtn').click()
    saved_text = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("savedMessage")').text
    assert saved_text =='Hello'
    driver.back()
    wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
    saved_text = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("savedMessage")'))).text
    assert saved_text == 'Hello'
finally:
    driver.quit()