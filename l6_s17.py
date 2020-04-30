from selenium import webdriver
import time
import math
import pyperclip
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()




    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    #print(x)

    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    print(addToClipBoard)
    pyperclip.copy(addToClipBoard)
          
finally:
    time.sleep(10)
    browser.quit()
