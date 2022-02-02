import pytest
from selenium import webdriver
#lesson3.5_step3
#для запуска тестов содержащих одновременно  метки smoke и win10 pytest -s -v -m "smoke and win10" test_fixture81.py
#файл pytest.ini служит для описания меток
link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("Test smoke")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("Test smoke and win10")