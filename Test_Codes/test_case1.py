import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data.test_data import Data
from Test_Pages.basepage import BasePage
from Test_Locators.test_locators import Locators 

class TestGuvi:
 
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Data.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10,  2, ignored_exceptions= [NoSuchElementException])
        yield
        self.driver.close()
    
    def test_title(self, booting_function):
        # asserting expected vs actual title
        assert BasePage.get_title(self) == "Swag Labs"
        print("SUCCESS, Title is valid")
    
    def test_login(self, booting_function):
        # enter username
        BasePage.enter_text(self, Locators.xpath_username, Data.username)

        # enter password
        BasePage.enter_text(self, Locators.xpath_password, Data.password)

        # click login button
        BasePage.click_button(self, Locators.xpath_login)

        assert BasePage.get_url(self) == Data.expected_url
        print("SUCCESS, Logged in")
 


