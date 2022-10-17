#Implementation of Selenium WebDriver with Python using PyTest
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
import chromedriver_binary
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wd = wd.Chrome()
wd.implicitly_wait(10)

out_stock = "https://telfar.net/pages/rainbow-online-terms"
pre_order = "https://telfar.net/collections/hats-belts/products/black-logo-hat"
coming_soon = "https://telfar.net/collections/puff-red-a/products/puff-hoodie-red?variant=40104297136227"

#Could detect the state of item ^
# Can Pull From Telfar Twitter to see which items are coming out
#id="AddToCart"
wd.get(pre_order)


def get_by_id(id_param):
    wd.implicitly_wait(5)
    try:
        return wd.find_element(By.ID, id_param)
    except:
        print(f"An exception occurred Couldnt Find {id_param}")


def get_by_class_name(class_param):
    wd.implicitly_wait(5)
    try:
        return wd.find_element(By.CLASS_NAME, class_param)
    except:
        print(f"An exception occurred Couldnt Find {class_param}")


def get_by_name(class_param):
    wd.implicitly_wait(5)
    try:
        return wd.find_element(By.NAME, class_param)
    except:
        print(f"An exception occurred Couldnt Find {class_param}")


add_to_cart = get_by_id('AddToCart')
wd.implicitly_wait(5)
add_to_cart.click()


view_cart = get_by_id('view-cart')
wd.implicitly_wait(5)
view_cart.click()

checkout = get_by_class_name('cart-checkout-btn')
wd.implicitly_wait(5)
checkout.click()

checkout_email_form = get_by_id("checkout_email")
first_name_form = get_by_id("checkout_shipping_address_first_name")
last_name_form = get_by_id("checkout_shipping_address_last_name")
street_address_form = get_by_id("checkout_shipping_address_address1")
address_appartment_form = get_by_id("checkout_shipping_address_address2")
city_form = get_by_id("checkout_shipping_address_city")
state_form = get_by_id("checkout_shipping_address_province")
zip_code_form = get_by_id("checkout_shipping_address_zip")
phone_number_form = get_by_id("checkout_shipping_address_phone")
continue_button = get_by_id("continue_button")


def type_and_fill(form_id, message):
    form_id.clear()
    type(form_id)
    form_id.send_keys(message)


def type_and_fill_slow(form_id, message):
    form_id.clear()
    for character in message:
        type(form_id)
        time.sleep(1)
        form_id.send_keys(character)


type_and_fill(checkout_email_form, "MyGirlfriendLovesme@gmail.com")
type_and_fill(first_name_form, "Tech")
type_and_fill(last_name_form, "W/Ty")
type_and_fill(street_address_form, "1000 Tech way")
type_and_fill(address_appartment_form, "Apartment 1")
type_and_fill(city_form, "Los Angales")
type_and_fill(zip_code_form, "80020")
type_and_fill(phone_number_form, "678-999-8212")
Select(state_form).select_by_value("CO")
continue_button.click()


proceed_address = get_by_id("btn-proceed-address")
btn_accept_address = get_by_id("btn-accept-address")

try:
  proceed_address.click()
except:
  btn_accept_address.click()


continue_button = get_by_id("continue_button")
continue_button.click()

# google_ana = get_by_id("google-analytics-sandbox")
# card_number = get_by_id("card-fields-number-3y17te8joz000000-scope-telfar.net")

# wd.switch_to.frame(google_ana)
# wd.switch_to.frame(card_number)
# cc_number = get_by_id("number")


# cc_number = get_by_class_name("input-placeholder-color--lvl-22")
# cc_name = get_by_id("name")
# cc_expiry = get_by_id("expiry")
# cc_verification_value = get_by_id("verification_value")
wait = WebDriverWait(wd, 10)
card_num_tries = 0
# print(wd.find_elements(By.TAG_NAME, "iframe")[0])
def find_and_fill(num, field, data):
    wd.switch_to.default_content()
    wd.implicitly_wait(5)


    print(wd.find_elements(By.TAG_NAME, "iframe")[1])

    try:
       
        wd.switch_to.frame(wd.find_elements(By.TAG_NAME, "iframe")[num])
        temp_field = get_by_name(field)
        type_and_fill_slow(temp_field, data)
    except:
        if (num == 1 and card_num_tries < 5):
            find_and_fill(1, "number", "45329126")

        print(f"An exception occurred Couldnt Find iframe {num}")


print("Number of elements")
find_and_fill(1, "number", "45329126")
# find_and_fill(2, "name", "Neez Duts")
# find_and_fill(3, "expiry", "7/2027")
# find_and_fill(4, "verification_value", "723")




wd.switch_to.default_content()
same_as_shipping = get_by_id("checkout_different_billing_address_false")
wd.implicitly_wait(2)
same_as_shipping.click()
wd.implicitly_wait(2)
continue_button = get_by_id("continue_button")
continue_button.click()

#Confirm Buy Item
#Send Ourself  text message once its bought issue (twillio)
