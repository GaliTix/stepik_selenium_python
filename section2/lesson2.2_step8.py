from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Enter first name']")
    input1.send_keys("Galina")
    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']")
    input1.send_keys("Tikhomirova")
    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Enter email']")
    input1.send_keys("tarakashka@bug.ru")
    element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname('lesson2.2_step8.py'))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
