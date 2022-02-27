# all those import
# you only need pip install selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

##################### DIAL CODE #######################
def number_dial(section,number):
    # for numerical input yuo must use numpad and basic for loop
    for i in str(number):
        if i == "0":
            section.send_keys(Keys.NUMPAD0)
        if i == "1":
            section.send_keys(Keys.NUMPAD1)
        if i == "2":
            section.send_keys(Keys.NUMPAD2)
        if i == "3":
            section.send_keys(Keys.NUMPAD3)
        if i == "4":
            section.send_keys(Keys.NUMPAD4)
        if i == "5":
            section.send_keys(Keys.NUMPAD5)
        if i == "6":
            section.send_keys(Keys.NUMPAD6)
        if i == "7":
            section.send_keys(Keys.NUMPAD7)
        if i == "8":
            section.send_keys(Keys.NUMPAD8)
        if i == "9":
            section.send_keys(Keys.NUMPAD9)
    time.sleep(1)


##################### URLs #######################
REGISTER_PAGE = "https://www.trendyol.com/uyelik?cb=https%3A%2F%2Fwww.trendyol.com%2F"
WAIVER_AGREEMENT = "#login-register > div.lr-container > div.q-layout.register > form > div.personal-checkbox > div > " \
                   "div.ty-display-flex.ty-checkbox-wrapper > div > svg "
SIGN_UP_BUTTON = '#login-register > div.lr-container > div.q-layout.register > form > button'
CODE_CONFIRMATION_BUTTON = "#login-register > div.lr-container > div.q-layout.register > div > div > div > " \
                           "div.evm-form > form > div:nth-child(4) > " \
                           "button.ty-font-w-semi-bold.ty-button.ty-bordered.ty-transition.ty-input-small.ty-primary "






###################### CONFIRMATION PROCESS ###########################

def confirmation_process(driver):
    # get email code for confirmation code
    import email_code
    # create webdriver with chrome

    # always use try except block if you are waiting something to load up
    try:
        # it is looking for element for 10 secs if it finds it will continue
        # element name is "code"
        confirmation_code = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"code"))
        )

        # send your code
        # always wait for page to fully load
        time.sleep(10)
        # call external func to get code from email
        code=email_code.get_code()
        # let wait 3 secs to make sure it gets it  right
        time.sleep(3)
        # always click first and type second
        confirmation_code.click()
        time.sleep(1)

        # for numerical input yuo must use numpad and basic for loop
        number_dial(confirmation_code, code)


        # get the confirmation button
        confirmation_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, CODE_CONFIRMATION_BUTTON))
        )
        # click the confirmation button
        confirmation_button.click()


    except  Exception as err:
        print("Couldn't get the confirmation email", err)




# register func
def register_page(man_email,man_password):

    # create webdriver with chrome
    driver = webdriver.Chrome()
    # get the register page
    driver.get(REGISTER_PAGE)
    # it is just making sure it is fully loaded
    driver.implicitly_wait(10)

    try:
        # get the email
        email = driver.find_element(By.ID, "register-email")
        # get the password
        password = driver.find_element(By.ID, "register-password-input")
        # get the waiver agreement
        waiver_agreement = driver.find_element(By.CSS_SELECTOR, WAIVER_AGREEMENT)
        # get the sign up button
        signUp = driver.find_element(By.CSS_SELECTOR, SIGN_UP_BUTTON)
        # always click first and type second
        email.click()
        # send the email
        email.send_keys(man_email)

        # always click first and type second
        password.click()
        # send the password
        password.send_keys(man_password)
        # agree with waiver stuff
        waiver_agreement.click()
        # then sign up for it
        time.sleep(2)
        signUp.click()
    except Exception as err:
        print("fail to register first step",err)
        raise ValueError('fail to register first step')


    ################## CONFIRMATION PROCESS ############
    confirmation_process(driver)

    return driver

if __name__ == '__main__':
    register_page("avvv@nusaybinli.com","zackme1224")