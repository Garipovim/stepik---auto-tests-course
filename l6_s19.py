from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_id("book")
    buttonclick = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()    


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)    
    button = browser.find_element_by_id("solve")
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    print(addToClipBoard)
    pyperclip.copy(addToClipBoard)
          
finally:
    time.sleep(10)
    browser.quit()
