from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from views.base_view import BaseView

class EchoView(BaseView):
    MESSAGE_INPUT = (AppiumBy.ACCESSIBILITY_ID, 'messageInput')
    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'messageSaveBtn')

    def save_message(self, message):
        self.wait_for(self.MESSAGE_INPUT).send_keys(message)
        self.find(self.SAVE_BUTTON).click()

    def read_message(self):
        try:
            return self.wait_for(self.MESSAGE_LABEL).text
        except TimeoutException:
            return None
    
    def nav_back(self):
        from views.home_view import HomeView
        self.driver.back()
        return HomeView.instance(self.driver)
    
class EchoViewAndroid(EchoView):
    MESSAGE_LABEL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("savedMessage")')

class EchoViewIOS(EchoView):
    MESSAGE_LABEL = (AppiumBy.ACCESSIBILITY_ID, 'savedMessage')

EchoView._IOS = EchoViewIOS
EchoView._ANDROID = EchoViewAndroid