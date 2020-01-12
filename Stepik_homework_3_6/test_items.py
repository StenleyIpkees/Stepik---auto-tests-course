from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_item_has_add_to_cart_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket")))
    button = browser.find_element_by_class_name("btn-add-to-basket")
    assert button, f"There is no button {button}"