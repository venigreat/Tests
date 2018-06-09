import time
import re
import unittest

from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

from TruePackage.HelpMethods import HelpMeths
from TruePackage.ElemProduct import ElemProduct
from TruePackage.ElemMain import ElemMain
from TruePackage.ElemAuth import ElemAuth
from TruePackage.ElemSettings import ElemSettings
from TruePackage.ElemDeal import ElemDeal
from TruePackage.Configuration import Configuration

config = Configuration()
driver = webdriver.Remote('http://localhost:4723/wd/hub', config.desired_caps)
driver.implicitly_wait(8)
element_on_main = ElemMain()
element_on_auth = ElemAuth()
element_on_deal = ElemDeal()
element_on_product = ElemProduct()
element_on_settings = ElemSettings()
# driver.find_element_by_id(element_on_auth.button_choose_location).click()
# driver.find_element_by_xpath(element_on_auth.city_from_list_moscow).click()
class Tests(unittest.TestCase):

    def test_login_known_nmbr(self, phone=9009879879):
        driver.launch_app()
        driver.find_element_by_xpath(element_on_main.button_profile).click()
        try:
            driver.find_element_by_xpath(element_on_auth.label_my_profile).is_displayed()
            driver.find_element_by_xpath(element_on_main.button_home).click()
        except NoSuchElementException:
            driver.find_element_by_xpath(element_on_auth.button_phone_auth).click()
            driver.find_element_by_xpath(element_on_auth.field_countrycode).send_keys('7')
            driver.find_element_by_xpath(element_on_auth.field_phone_nmbr).send_keys(str(phone))
            driver.find_element_by_xpath(element_on_auth.button_confirm_nmbr).click()
            driver.find_element_by_xpath(element_on_auth.field_sms_code).send_keys('1')
            # driver.press_keycode(10)
            driver.find_element_by_xpath(element_on_auth.button_success_auth).click()
            sold = driver.find_element_by_xpath(element_on_auth.label_sold)
            self.assertEqual(sold.text, "Продано")
            driver.find_element_by_xpath(element_on_main.button_home).click()

    def test_logout(self):
        driver.launch_app()
        driver.find_element_by_xpath(element_on_main.button_profile).click()
        try:
            driver.find_element_by_xpath(element_on_auth.label_my_profile).is_displayed()
            driver.find_element_by_xpath(element_on_settings.button_gear).click()
            for i in range(5):
                try:
                    if driver.find_element_by_xpath(element_on_settings.button_logout).is_displayed():
                        break
                except NoSuchElementException:
                    HelpMeths.swipe(driver)
            driver.find_element_by_xpath(element_on_settings.button_logout).click()
            driver.find_element_by_xpath(element_on_settings.button_confirm_logout).click()
            driver.find_element_by_xpath(element_on_main.button_profile).click()
        except NoSuchElementException:
            pass
        finally:
            sleep(2)
            self.assertEqual(driver.find_element_by_xpath(element_on_auth.label_anon_header).text,
                             "Авторизуйтесь в приложении")

    def add_ad(self, name="Test", category=0, subcategory=4):
        sleep(2)
        driver.find_element_by_xpath(element_on_main.button_add).click()
        sleep(2)
        driver.find_element_by_xpath(element_on_main.category_stuff).click()
        sleep(5)
        driver.find_element_by_xpath(element_on_main.icon_photo).click()  # иконка фото
        driver.find_element_by_xpath(element_on_main.button_chose_from_gallery).click()
        if driver.find_element_by_xpath(
                    element_on_main.permission_images_allow).is_displayed():
             driver.find_element_by_xpath(element_on_main.permission_images_allow).click()
        driver.find_element_by_xpath(element_on_main.first_image_in_gallery).click()
        driver.find_element_by_xpath(element_on_main.button_apply_images).click()
        driver.find_element_by_xpath(element_on_main.field_header_ad).send_keys("%s" % (name))
        driver.find_element_by_xpath(element_on_main.field_cost).send_keys("500")
        driver.find_element_by_xpath(element_on_main.button_choose_category).click()
        driver.find_element_by_xpath(element_on_main.choose_subcategory % (category)).click()  # subcategory
        driver.find_element_by_xpath(element_on_main.choose_subcategory % (subcategory)).click()  # subcategory
        driver.find_element_by_xpath(element_on_main.button_done).click()
        sleep(3)
        driver.find_element_by_xpath(element_on_main.button_cancel_promotion).click()
        sleep(2)
        if driver.find_element_by_xpath(element_on_main.button_promo_swipe).is_displayed():#promo swipe screen
             driver.find_element_by_xpath(element_on_main.button_promo_swipe).click()
        driver.find_element_by_xpath(element_on_main.button_home).click()

    @staticmethod
    def promotion():
        driver.find_element_by_xpath(element_on_main.button_profile).click()
        sleep(5)
        driver.swipe(475, 1500, 475, 75, 750)
        sleep(1)
        for i in range(10):
            ad = driver.find_element_by_xpath(element_on_main.frame_ad)
            ad.find_element_by_xpath(element_on_main.relative_ad).click()
            try:
                driver.find_element_by_xpath(element_on_main.button_promo_swipe).click()
            except NoSuchElementException:
                sleep(0.1)
            sleep(1)
            try:
                driver.find_element_by_xpath(element_on_main.button_product_promotion).click()
                driver.find_element_by_xpath(element_on_main.button_promotion_premium).click()
                driver.find_element_by_xpath(element_on_main.button_promotion_x5).click()
                driver.find_element_by_xpath(element_on_main.button_promotion_pay).click()
                sleep(5)
                driver.find_element_by_xpath(element_on_main.button_webview_card_pay).click()
                sleep(5)
                driver.find_element_by_xpath(element_on_main.button_promotion_success).click()
                driver.find_element_by_xpath(element_on_main.button_profile_back).click()
                driver.swipe(475, 300, 475, 700, 500)
                sleep(0.5)
                driver.find_element_by_xpath(element_on_main.button_home).click()
                break
            except NoSuchElementException:
                driver.find_element_by_xpath(element_on_main.button_profile_back).click()
                sleep(1)
                driver.swipe(475, 700, 475, 300, 500)
                sleep(1)
        sleep(5)

    @staticmethod
    def starting_time(count_of_iterations):
        result_time = 0
        my_file = open("/Users/andrey.belyaev/Documents/some.txt", "r+")
        last_time = my_file.read()
        my_file.close()
        last_time = float(last_time)
        driver.implicitly_wait(0)
        for i in range(count_of_iterations):
            start_time = time.time()
            driver.launch_app()
            if desired_caps['appPackage'] == 'com.allgoritm.youla':
                for j in range(200):
                    try:
                        if driver.find_element_by_xpath(element_on_main.ad_on_main).is_displayed():
                            result_time += time.time() - start_time
                            break

                    except NoSuchElementException:
                        pass

            else:
                for j in range(200):
                    try:
                        if driver.find_element_by_xpath(element_on_main.avito_first_ad).is_displayed():
                            result_time += time.time() - start_time
                            break
                    except NoSuchElementException:
                        pass
        print(result_time/count_of_iterations)
        driver.implicitly_wait(5)
        if result_time/count_of_iterations < last_time:
            print('better on %f' % (last_time - result_time/count_of_iterations))
        else:
            print('worser on %f' % (result_time/count_of_iterations - last_time))
        my_file = open("/Users/andrey.belyaev/Documents/some.txt", "w+")
        my_file.write(str(result_time/count_of_iterations))
        my_file.close()

    def test_check_amru_version(self):
        Tests.test_login_known_nmbr(self, 9009879879)
        driver.find_element_by_xpath(element_on_main.button_profile).click()
        driver.find_element_by_xpath(element_on_settings.button_gear).click()
        for i in range(5):
            try:
                if driver.find_element_by_xpath(element_on_settings.version_nmbr).is_displayed():
                    break
            except:
                HelpMeths.swipe(driver)
        for i in range(5):
            driver.find_element_by_xpath(element_on_settings.version_nmbr).click()
        amru_version = driver.find_element_by_xpath(element_on_settings.version_nmbr)
        self.assertTrue(re.fullmatch(r'.*\sВерсия am.ru \d{1,2}(.\d{1,2})*', amru_version.text),"AmruVersion")

    @staticmethod
    def buy_BS():
        driver.launch_app()
        Tests.login_known_nmbr(9009879879)
        sleep(3)
        driver.find_element_by_xpath(element_on_main.button_filtres_linear).\
            find_element_by_xpath(element_on_main.button_filtres_text).click()
        driver.find_element_by_xpath(element_on_main.chbox_filter_BS).click()
        driver.find_element_by_xpath(element_on_main.chbox_filter_delivery).click()
        driver.find_element_by_xpath(element_on_main.button_filter_accept).click()
        sleep(3)
        ad = driver.find_element_by_xpath(element_on_main.ad_on_filter)
        for i in range(10):
            ad.find_element_by_xpath(element_on_main.linear_clickable_ad).click()
            sleep(2)
            if not HelpMeths.is_product_mine(driver):
                print("false")
                try:
                    BS_buy = driver.find_element_by_xpath(element_on_product.button_BS_buy)
                    break
                except:
                    sleep(2)
                    driver.find_element_by_xpath(element_on_product.button_back).click()
                    HelpMeths.swipe(driver)
            else:
                print("true")
                sleep(2)
                driver.find_element_by_xpath(element_on_product.button_back).click()
                HelpMeths.swipe(driver)
        assert BS_buy.text == "КУПИТЬ СЕЙЧАС"
        driver.find_element_by_xpath(element_on_product.button_BS_buy).click()
        sleep(5)
        driver.find_element_by_xpath(element_on_main.button_webview_card_pay).click()
        sleep(8)
        label_deal = driver.find_element_by_xpath(element_on_deal.header_deal_nmbr)
        assert re.fullmatch(r'Заказ №\d*', label_deal.text)
        times_1 = driver.find_element_by_xpath(element_on_deal.label_timer).text.split()
        sleep(2)
        times_2 = driver.find_element_by_xpath(element_on_deal.label_timer).text.split()
        assert times_2[2] < times_1[2]

if __name__ == '__main__':
    unittest.main()

some_tests = Tests()
# Tests.test_logout(some_tests)
# Tests.test_login_known_nmbr(some_tests, 9009879879)
# Tests.add_product(some_tests, "Кошечка", 2, 2)
# Tests.swipe(some_tests)
# Tests.HelpMethods.swipe(some_tests, driver)
# Tests.promotion(some_tests)
Tests.test_check_amru_version(some_tests)
# Tests.buy_BS(some_tests)
driver.quit()
