from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link="http://suninjuly.github.io/redirect_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
  browser = webdriver.Chrome()
  browser.get(link)
  browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary").click()
  new_window = browser.window_handles[1]
  browser.switch_to.window(new_window)
  x = browser.find_element(By.ID, "input_value").text
  y = calc(x)
  answer = browser.find_element(By.ID, "answer")
  answer.send_keys(y)
  browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


