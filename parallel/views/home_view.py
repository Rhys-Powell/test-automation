from appium.webdriver.common.appiumby import AppiumBy
from views.base_view import BaseView
from views.echo_view import EchoView

class HomeView(BaseView):
    ECHO_ITEM = (AppiumBy.ACCESSIBILITY_ID, 'Echo Box')
    
    def nav_to_echo_box(self):
        self.wait_for(self.ECHO_ITEM).click()
        return EchoView.instance(self.driver)
