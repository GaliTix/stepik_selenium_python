from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link="http://SunInJuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
  browser = webdriver.Chrome()
  browser.get(link)
  x = browser.find_element(By.ID, "input_value").text
  y = calc(x)
  browser.execute_script("window.scrollBy(0, 120);")
  answer=browser.find_element(By.ID, "answer")
  answer.send_keys(y)
  browser.find_element_by_css_selector("#robotCheckbox").click()
  browser.find_element_by_css_selector("#robotsRule").click()
  browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

