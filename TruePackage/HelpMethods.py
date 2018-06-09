from time import sleep
from selenium.common.exceptions import NoSuchElementException

from TruePackage.ElemProduct import ElemProduct
from TruePackage.ElemMain import ElemMain
from TruePackage.ElemAuth import ElemAuth
from TruePackage.ElemSettings import ElemSettings
from TruePackage.ElemDeal import ElemDeal

element_on_main = ElemMain()
element_on_auth = ElemAuth()
element_on_deal = ElemDeal()
element_on_product = ElemProduct()
element_on_settings = ElemSettings()

class HelpMeths:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def swipe(driver, count=1):
        for i in range(count):
            driver.swipe(driver.get_window_size()['width'] * 0.5, driver.get_window_size()['height'] * 0.7,
                         driver.get_window_size()['width'] * 0.5, driver.get_window_size()['height'] * 0.1, 700)
            sleep(3)

    def is_product_mine(driver):
        sleep(2)
        try:
            if driver.find_element_by_xpath(element_on_product.button_statistics).is_displayed():
                return True
            else:
                return False
        except NoSuchElementException:
            return False



