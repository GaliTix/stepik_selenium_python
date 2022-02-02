import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_guest_should_see_button_basket(browser):
    browser.get(link)
    actual_result = browser.find_element_by_css_selector("#add_to_basket_form")
    expected_result = "add_to_basket_form"
    assert expected_result == actual_result.get_attribute("id"), f"expected {expected_result}, got {actual_result.get_attribute('id')}"
    time.sleep(10)