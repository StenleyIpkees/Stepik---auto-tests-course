from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    imrobot = browser.find_element_by_id("robotCheckbox")
    imrobot.click()
    robotsrule = browser.find_element_by_id("robotsRule")
    robotsrule.click()
    button = browser.find_element_by_xpath("//*[@type='submit']")
    button.click()

    print(y)

    time.sleep(1)
    
finally:
    time.sleep(10)
    browser.quit()
