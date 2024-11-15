from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EchoView(object):
    MESSAGE_INPUT = (AppiumBy.ACCESSIBILITY_ID, 'messageInput')
    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'messageSaveBtn')
    MESSAGE_LABEL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("savedMessage")')

    def __init__(self, driver):
        self.driver = driver 
    
    def save_message(self, message):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.MESSAGE_INPUT)).send_keys(message)
        self.driver.find_element(*self.SAVE_BUTTON).click()

    def read_message(self):
        return self.driver.find_element(*self.MESSAGE_LABEL).text
    
    def nav_back(self):
        self.driver.back()