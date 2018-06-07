import unittest
import ElemProduct
from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class HelpMeths:
    def _init_(self, driver):
        self.driver = driver

    @staticmethod
    def is_visible(elem):
        try:
            elem.is_displayed()
            return True
        except NoSuchElementException:
            return False

    @staticmethod
    def swipe(driver, count=1):
        for i in range(count):
            driver.swipe(driver.get_window_size()['width'] * 0.5, driver.get_window_size()['height'] * 0.7,
                         driver.get_window_size()['width'] * 0.5, driver.get_window_size()['height'] * 0.1, 700)
            sleep(3)

    @staticmethod
    def is_product_mine(driver):
        sleep(2)
        try:
            if driver.find_element_by_xpath(Elem_product.button_statistics).is_displayed():
                return True
            else:
                return False
        except NoSuchElementException:
            return False



