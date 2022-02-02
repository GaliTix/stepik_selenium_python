from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def test_01( ):
   try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys("Galina")
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input1.send_keys("Tikhomirova")
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input1.send_keys("tarakashka@bug.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

   finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

def test_02():
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys("Galina")
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input1.send_keys("Tikhomirova")
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input1.send_keys("tarakashka@bug.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!"== welcome_text
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

