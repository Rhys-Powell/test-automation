from appium import webdriver
from appium.options.android import UiAutomator2Options
from os import path
import time

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
app_act1 = '.graphics.TouchPaint'
app_act2 = '.text.Marquee'
try:
    driver.install_app(app)
    driver.execute_script('mobile:startActivity', {
        'action': app_act1,
        'component': app_id + '/' + app_act1,
    })
    time.sleep(1)
    driver.execute_script('mobile:startActivity', {
        'action': app_act2,
        'component': app_id + '/' + app_act2,
    })
    time.sleep(1)
  
finally:
    driver.quit()