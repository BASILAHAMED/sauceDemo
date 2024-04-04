from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data.test_data import Data

class BasePage:
    def boot(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10,  2, ignored_exceptions= [NoSuchElementException])

    def click_button(self, value):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, value)))
        element.click()

    def enter_text(self, value, text):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, value)))
        element.send_keys(text)

    def fetch_text(self, value):
        element = self.wait.until(EC.text_to_be_present_in_element((By.XPATH, value)))
        return element.text

    def get_title(self):
        title = self.driver.title
        return title
    
    def get_url(self):
        current_url = self.driver.current_url
        return current_url