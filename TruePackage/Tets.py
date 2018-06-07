import unittest
from TruePackage.ElemMain import ElemMain
from TruePackage import Elem_auth
from TruePackage import Elem_settings
from TruePackage import Elem_product
from TruePackage import Elem_deal
import time
import re
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from TruePackage.HelpMethods import HelpMeths


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'# '6.0'
desired_caps['deviceName'] = 'emulator'#'WKUWGAO7LV9HJFZH'
#desired_caps['app'] = '/Users/andrey.belyaev/Downloads/app-debug-2.13(250515d92)dev-am-2.1.7.2.apk'
desired_caps['appPackage'] = 'com.allgoritm.youla'#'com.avito.android'
desired_caps['appActivity'] = '.AppInitActivity'#'.home.HomeActivity'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['noReset'] = True
desired_caps['noSign'] = True
desired_caps['skipUnlock'] = True


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(7)
# driver.find_element_by_id(Elem_auth.button_choose_location).click()
# driver.find_element_by_xpath(Elem_auth.city_from_list_moscow).click()





def login_known_nmbr(phone):
    driver.find_element_by_xpath(ElemMain.button_profile).click()
    try:
        driver.find_element_by_xpath(Elem_auth.label_my_profile).is_displayed()
        driver.find_element_by_xpath(ElemMain.button_home).click()
    except NoSuchElementException:
        driver.find_element_by_xpath(Elem_auth.button_phone_auth).click()
        driver.find_element_by_xpath(Elem_auth.field_countrycode).send_keys('7')
        driver.find_element_by_xpath(Elem_auth.field_phone_nmbr).send_keys(str(phone))
        driver.find_element_by_xpath(Elem_auth.button_confirm_nmbr).click()
        driver.find_element_by_xpath(Elem_auth.field_sms_code).send_keys('1')
        #driver.press_keycode(10)
        driver.find_element_by_xpath(Elem_auth.button_success_auth).click()
        sold=driver.find_element_by_xpath(Elem_auth.label_sold)
        assert sold.text == "Продано"
        driver.find_element_by_xpath(ElemMain.button_home).click()

def logout():
    driver.launch_app()
    driver.find_element_by_xpath(ElemMain.button_profile).click()
    try:
        driver.find_element_by_xpath(Elem_auth.label_my_profile).is_displayed()
        driver.find_element_by_xpath(Elem_settings.button_gear).click()
        for i in range(5):
            try:
                if driver.find_element_by_xpath(Elem_settings.button_logout).is_displayed():
                    break
            except:
                HelpMeths.swipe(driver)
        driver.find_element_by_xpath(Elem_settings.button_logout).click()
        driver.find_element_by_xpath(Elem_settings.button_confirm_logout).click()
        driver.find_element_by_xpath(ElemMain.button_profile).click()
    except:
        pass
    finally:
        assert driver.find_element_by_xpath(Elem_auth.label_anon_header).text == 'Авторизуйтесь в приложении'





def add_ad(name="Test",category=0,subcategory=4):
    sleep(2)
    driver.find_element_by_xpath(ElemMain.button_add).click()
    sleep(2)
    driver.find_element_by_xpath(ElemMain.category_stuff).click()
    sleep(5)
    driver.find_element_by_xpath(ElemMain.icon_photo).click()  # иконка фото
    driver.find_element_by_xpath(ElemMain.button_chose_from_gallery).click()
    if driver.find_element_by_xpath(
                ElemMain.permission_images_allow).is_displayed():
         driver.find_element_by_xpath(ElemMain.permission_images_allow).click()
    driver.find_element_by_xpath(ElemMain.first_image_in_gallery).click()
    driver.find_element_by_xpath(ElemMain.button_apply_images).click()
    driver.find_element_by_xpath(ElemMain.field_header_ad).send_keys("%s" % (name))
    driver.find_element_by_xpath(ElemMain.field_cost).send_keys("500")
    driver.find_element_by_xpath(ElemMain.button_choose_category).click()
    driver.find_element_by_xpath(ElemMain.choose_subcategory % (category)).click()  # subcategory
    driver.find_element_by_xpath(ElemMain.choose_subcategory % (subcategory)).click()  # subcategory
    driver.find_element_by_xpath(ElemMain.button_done).click()
    sleep(3)
    driver.find_element_by_xpath(ElemMain.button_cancel_promotion).click()
    sleep(2)
    if driver.find_element_by_xpath(ElemMain.button_promo_swipe).is_displayed():#promo swipe screen
         driver.find_element_by_xpath(ElemMain.button_promo_swipe).click()
    driver.find_element_by_xpath(ElemMain.button_home).click()


def promotion():
    driver.find_element_by_xpath(ElemMain.button_profile).click()
    sleep(5)
    driver.swipe(475, 1500, 475, 75, 750)
    sleep(1)
    for i in range(10):
        ad = driver.find_element_by_xpath(ElemMain.frame_ad)
        ad.find_element_by_xpath(ElemMain.relative_ad).click()
        try:
            driver.find_element_by_xpath(ElemMain.button_promo_swipe).click()
        except NoSuchElementException:
            sleep(0.1)
        sleep(1)
        try:
            driver.find_element_by_xpath(ElemMain.button_product_promotion).click()
            driver.find_element_by_xpath(ElemMain.button_promotion_premium).click()
            driver.find_element_by_xpath(ElemMain.button_promotion_x5).click()
            driver.find_element_by_xpath(ElemMain.button_promotion_pay).click()
            sleep(5)
            driver.find_element_by_xpath(ElemMain.button_webview_card_pay).click()
            sleep(5)
            driver.find_element_by_xpath(ElemMain.button_promotion_success).click()
            driver.find_element_by_xpath(ElemMain.button_profile_back).click()
            driver.swipe(475, 300, 475, 700, 500)
            sleep(0.5)
            driver.find_element_by_xpath(ElemMain.button_home).click()
            break
        except NoSuchElementException:
            driver.find_element_by_xpath(ElemMain.button_profile_back).click()
            sleep(1)
            driver.swipe(475, 700, 475, 300, 500)
            sleep(1)
    sleep(5)

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
                    if driver.find_element_by_xpath(ElemMain.ad_on_main).is_displayed():
                        result_time += time.time() - start_time
                        break

                except NoSuchElementException:
                    pass

        else:
            for j in range(200):
                try:
                    if driver.find_element_by_xpath(ElemMain.avito_first_ad).is_displayed():
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

def check_amru_version():
    driver.launch_app()
    login_known_nmbr(9009879879)
    driver.find_element_by_xpath(ElemMain.button_profile).click()
    driver.find_element_by_xpath(Elem_settings.button_gear).click()
    for i in range(5):
        try:
            if driver.find_element_by_xpath(Elem_settings.version_nmbr).is_displayed():
                break
        except:
            HelpMeths.swipe(driver)
    for i in range(5):
        driver.find_element_by_xpath(Elem_settings.version_nmbr).click()
    amru_version = driver.find_element_by_xpath(Elem_settings.version_nmbr)
    assert re.fullmatch(r'.*\sВерсия am.ru \d{1,2}(.\d{1,2})*', amru_version.text)

def buy_BS():
    driver.launch_app()
    login_known_nmbr(9009879879)
    sleep(3)
    driver.find_element_by_xpath(ElemMain.button_filtres_linear).\
        find_element_by_xpath(ElemMain.button_filtres_text).click()
    driver.find_element_by_xpath(ElemMain.chbox_filter_BS).click()
    driver.find_element_by_xpath(ElemMain.chbox_filter_delivery).click()
    driver.find_element_by_xpath(ElemMain.button_filter_accept).click()
    sleep(3)
    ad = driver.find_element_by_xpath(ElemMain.ad_on_filter)
    for i in range(10):
        ad.find_element_by_xpath(ElemMain.linear_clickable_ad).click()
        sleep(2)
        if not HelpMeths.is_product_mine(driver):
            print("false")
            try:
                BS_buy = driver.find_element_by_xpath(Elem_product.button_BS_buy)
                break
            except:
                sleep(2)
                driver.find_element_by_xpath(Elem_product.button_back).click()
                HelpMeths.swipe(driver)
        else:
            print("true")
            sleep(2)
            driver.find_element_by_xpath(Elem_product.button_back).click()
            HelpMeths.swipe(driver)
    assert BS_buy.text == "КУПИТЬ СЕЙЧАС"
    driver.find_element_by_xpath(Elem_product.button_BS_buy).click()
    sleep(5)
    driver.find_element_by_xpath(ElemMain.button_webview_card_pay).click()
    sleep(5)
    label_deal = driver.find_element_by_xpath(Elem_deal.header_deal_nmbr)
    assert re.fullmatch(r'Заказ №\d*', label_deal.text)
    times_1 = driver.find_element_by_xpath(Elem_deal.label_timer).text.split()
    sleep(2)
    times_2 = driver.find_element_by_xpath(Elem_deal.label_timer).text.split()
    assert times_2[2] < times_1[2]


#first_test()
#find_nokia()
#h_m.swipe()
#login_known_nmbr(9009879879)
#add_ad("Кошечка", 2, 2)
#swipe()
#HelpMethods.swipe(driver)
#promotion()
#starting_time(100)
#logout()
# check_amru_version()
buy_BS()
driver.quit()
