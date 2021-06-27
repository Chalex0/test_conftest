from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_see_button_add_to_basket(browser):
    wait = WebDriverWait(browser, 5) 
    browser.get(link)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "btn-add-to-basket")]')))
    assert button.get_attribute('type') == 'submit', 'Кнопка отсутствует на странице'
    button.click()
 
