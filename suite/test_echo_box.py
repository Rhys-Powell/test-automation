from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_echo_box(driver):
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
    