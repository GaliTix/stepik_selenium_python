from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

link="http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
  browser = webdriver.Chrome()
  browser.get(link)
# говорим Selenium проверять в течение 12 секунд, пока цена дома не уменьшится до 100
  WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
  browser.find_element(By.ID, "book").click()
  x = browser.find_element(By.ID, "input_value").text
  y = calc(x)
  answer = browser.find_element(By.ID, "answer")
  answer.send_keys(y)
  browser.find_element(By.ID, "solve").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
