import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
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
    wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'List Demo'))).click()
    wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Altocumulus')))
    
    scroll = ActionBuilder(driver)
    finger = scroll.add_pointer_input(POINTER_TOUCH, "finger")
    # viewport_size = driver.get_window_size()
    # print(viewport_size['width'], viewport_size['height'])
    finger.create_pointer_move(duration=0, x=100, y=1000)
    finger.create_pointer_down(button=0)
    finger.create_pointer_move(duration=250, x=0, y=-1000, origin="pointer")
    finger.create_pointer_up(button=0)
    scroll.perform()

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Stratocumulus')
finally:
    driver.quit()