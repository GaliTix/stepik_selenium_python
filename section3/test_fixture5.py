import pytest
from selenium import webdriver
#lesson3.5_step2
#для запуска используйте команду pytest -s -v -m smoke test_fixture5.py
#для запуска тестов с разными метками smoke и regression используйте команду pytest -s -v -m "smoke or regression" test_fixture5.py
#для запуска тестов не отмеченных как smoke используйте команду pytest -s -v -m "not smoke" test_fixture5.py
#файл pytest.ini служит для описания меток
link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("Test smoke")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("Test regression")
