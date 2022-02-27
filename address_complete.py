from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from register i need dial_number func to send numberr dial to phone input
from register import number_dial



def login(man_email,man_password):
    # set chrome driver
    driver = webdriver.Chrome()
    # request login page
    driver.get("https://www.trendyol.com/giris?cb=https%3A%2F%2Fwww.trendyol.com%2FLogin")
    # make sure it isfully loaded
    driver.implicitly_wait(10)
    # login func
    signIn_path = '#login-register > div.lr-container > div.q-layout.login > form > button'
    try:

        email = driver.find_element(By.ID, "login-email")
        password = driver.find_element(By.ID, "login-password-input")
        signIn = driver.find_element(By.CSS_SELECTOR, signIn_path)
        email.click()
        email.send_keys(man_email)
        password.click()
        password.send_keys(man_password)
        signIn.click()
        time.sleep(5)
        # add data
        add_address()
    except Exception as err:
        print("fail to login ", err)

def add_address(driver,**data):
    driver.get("https://www.trendyol.com/Hesabim/AdresBilgileri")
    info = data["data"]

    d_name = info["name"]
    d_last = info["last"]
    d_phone = info["phone"]
    d_province = info["province"]
    d_district = info["district"]
    d_street = info["street"]
    d_address = info["address"]
    d_address_name = info["address_name"]

    add_address_path = "#addresses-page-container > div > div.ty-display-flex.addresses-page-header > a"
    il_scrollbar_path = "#address-popup-container > div > div.ty-display-flex.ty-modal.ty-bordered.ty-transition" \
                        "-appear-enter-done > div > div.modal-wrapper > div > div > form > div:nth-child(2) > " \
                        "div:nth-child(2) > div:nth-child(2) > div > span "
    il_name_scrollbar_path = "#address-popup-container > div > div.ty-display-flex.ty-modal.ty-bordered.ty-transition" \
                             "-appear-enter-done > div > div.modal-wrapper > div > div > form > div:nth-child(2) > " \
                             "div:nth-child(2) > div:nth-child(2) > div > div > div:nth-child(57) "
    ilce_scrollbar_path = "#address-popup-container > div > div.ty-display-flex.ty-modal.ty-bordered.ty-transition" \
                          "-appear-enter-done > div > div.modal-wrapper > div > div > form > div:nth-child(3) > " \
                          "div:nth-child(1) > div:nth-child(2) > div > span "
    ilce__name_scrollbar_path = "#address-popup-container > div > " \
                                "div.ty-display-flex.ty-modal.ty-bordered.ty-transition-appear-enter-done > div > " \
                                "div.modal-wrapper > div > div > form > div:nth-child(3) > div:nth-child(1) > " \
                                "div:nth-child(2) > div > div > div:nth-child(7) "
    mahalle_scrollbar_path = "#address-popup-container > div > div.ty-display-flex.ty-modal.ty-bordered.ty-transition" \
                             "-appear-enter-done > div > div.modal-wrapper > div > div > form > div:nth-child(3) > " \
                             "div:nth-child(2) > div:nth-child(2) > div > span "
    mahalle__name_scrollbar_path = "#address-popup-container > div > " \
                                   "div.ty-display-flex.ty-modal.ty-bordered.ty-transition-appear-enter-done > div > " \
                                   "div.modal-wrapper > div > div > form > div:nth-child(3) > div:nth-child(2) > " \
                                   "div:nth-child(2) > div > div > div:nth-child(64) "

    save_button_path = "#address-popup-container > div > div.ty-display-flex.ty-modal.ty-bordered.ty-transition" \
                       "-appear-enter-done > div > div.modal-wrapper > div > div > form > div:nth-child(6) > button "

    # click the add address button
    try:
        # add_address = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.CSS_SELECTOR, add_address_path))
        # )
        # add_address.click()
        address_button = driver.find_element(By.CSS_SELECTOR,add_address_path)
        driver.execute_script("arguments[0].click();", address_button)
    except Exception as err :
        print("fail to click the add address button",err)
        raise Exception(err)

    # find the name and last name
    try:
        name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"name"))
        )
        # make dinamic name
        name.send_keys(d_name)
        surname = driver.find_element(By.NAME, "surname")
        # make dinamic lastname
        surname.send_keys(d_last)
        #try to find phone number
        #add number after 05 "465601620"
        try:
            phone = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "phone"))
            )
            phone.click()
            number_dial(phone, d_phone)
        except:
            print("fail to add phone number")
            raise ValueError('fail to add phone')



        il_scrollbar = driver.find_element(By.CSS_SELECTOR, il_scrollbar_path )
        ##AFTER YOU CLICK THE ILSCROLLBAR
        il_scrollbar.click()
        time.sleep(2)
        il__name_scrollbar = driver.find_element(By.CSS_SELECTOR, il_name_scrollbar_path)
        il__name_scrollbar.click()
        time.sleep(2)

        try:
            ilce_1 = driver.find_element(By.CSS_SELECTOR,ilce_scrollbar_path)
            ilce_2 = driver.find_element(By.CSS_SELECTOR, ilce__name_scrollbar_path)

            driver.execute_script("arguments[0].click();",ilce_1)
            driver.execute_script("arguments[0].click();",ilce_2)

            time.sleep(2)
        except:
            print("fail to pick ilce")
            raise ValueError('fail to pick ilce')
        try:


            mah_1 = driver.find_element(By.CSS_SELECTOR,mahalle_scrollbar_path)
            # mah_2 = driver.find_element(By.CSS_SELECTOR, mahalle__name_scrollbar_path)
            mah_2 = driver.find_element(By.XPATH, f"// div[contains(text(),'{d_street}')]")

            driver.execute_script("arguments[0].click();",mah_1)
            driver.execute_script("arguments[0].click();",mah_2)
        except:
            print("fail to pick mahalle")
            raise ValueError('fail to pick mahalle')

        # ilce_scrollbar = driver.find_element(By.CSS_SELECTOR, ilce_scrollbar_path)
        # time.sleep(2)
        # ilce_scrollbar.click()
        # try:
        #     ilce__name_scrollbar = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.CSS_SELECTOR,ilce__name_scrollbar_path))
        #     )
        #     ilce__name_scrollbar.click()
        #     time.sleep(2)
        # except Exception as err:
        #     print("fail to pick ilce",err)
        #
        #
        # mahalle_scrollbar = driver.find_element(By.CSS_SELECTOR, mahalle_scrollbar_path)
        # mahalle_scrollbar.click()
        # try:
        #     mahalle__name_scrollbar = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.CSS_SELECTOR,mahalle__name_scrollbar_path))
        #     )
        #
        #     mahalle__name_scrollbar.click()
        #     time.sleep(2)
        # except Exception as err:
        #     print("fail to pick mahalle")



        addressLine = driver.find_element(By.NAME,"addressLine")
        addressLine.send_keys(d_address)

        addressName = driver.find_element(By.NAME,"addressName")
        addressName.send_keys(d_address_name)

        save_button = driver.find_element(By.CSS_SELECTOR, save_button_path)
        save_button.click()

        driver.quit()

    except  Exception as err:
        print(err)


