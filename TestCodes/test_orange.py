"""
test_orange.py

Program : POM main executing file
"""

from TestLocators.orange_locators import OrangeHRM_Locators
from TestData.orange_data import OrangeHRM_Data
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchWindowException
import pytest

class Test_OrangeHRM:

    @pytest.fixture
    # Booting function for running all the Python tests
    def booting_function(self):
        firefox_options = Options()
        firefox_options.add_argument('--incognito')
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        yield
        self.driver.close()

    # Method for user login
    def user_login(self):
        try:

            self.driver.get(OrangeHRM_Data.url)

            username_box = self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRM_Locators().username)))
            username_box.send_keys(OrangeHRM_Data.admin_username)

            password_box = self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRM_Locators().password)))
            password_box.send_keys(OrangeHRM_Data.positive_password)

            submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators().submit_button)))
            submit_button.click()

            pim_button = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locators.pim_button)))
            pim_button.click()

            return True

        except [NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotVisibleException, WebDriverException] as error:
            print('Error:', error)

    # Test Case for positive login data in the webpage
    def test_positive_login(self,booting_function):
        try:

            self.driver.get(OrangeHRM_Data.url)

            username_box = self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRM_Locators().username)))
            username_box.send_keys(OrangeHRM_Data.admin_username)

            password_box = self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRM_Locators().password)))
            password_box.send_keys(OrangeHRM_Data.positive_password)

            submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators().submit_button)))
            submit_button.click()

            assert OrangeHRM_Data().dashboard_url == self.driver.current_url
            print("SUCCESS : Login with Username {a} & Password {b}".format(a=OrangeHRM_Data.admin_username, b=OrangeHRM_Data.positive_password))


        except [NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotVisibleException, NoSuchWindowException, WebDriverException] as error:
            print('Error:', error)

    # Test Case for negative login data in the webpage
    def test_negative_login(self, booting_function):
        try:

            self.driver.get(OrangeHRM_Data().url)

            username_box = self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRM_Locators().username)))
            username_box.send_keys(OrangeHRM_Data.admin_username)

            password_box = self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRM_Locators().password)))
            password_box.send_keys(OrangeHRM_Data.negative_password)

            submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators().submit_button)))
            submit_button.click()

            self.wait.until(EC.visibility_of_element_located((By.XPATH, OrangeHRM_Locators.invalid_login_message)))
            assert self.driver.find_element(By.XPATH,OrangeHRM_Locators.invalid_login_message).text == OrangeHRM_Data.invalid_message

            print("SUCCESS : Invalid Login with Username {a} & Password {b}: Invalid Message Visible".format(a=OrangeHRM_Data.admin_username,b=OrangeHRM_Data.negative_password))


        except [NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotVisibleException, NoSuchWindowException, WebDriverException] as error:
            print('Error:', error)

    # Test Case to add new employee information
    def test_add_employee(self, booting_function):
        try:

            if self.user_login():

                add_employee_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators.add_employee_button)))
                add_employee_button.click()

                first_name_input = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locators.first_name_box)))
                first_name_input.send_keys(OrangeHRM_Data.employee_first_name)

                last_name_input = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locators.last_name_box)))
                last_name_input.send_keys(OrangeHRM_Data.employee_last_name)

                save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators.save_button_add)))
                save_button.click()

                # Notification pop-up for details added
                self.wait.until(EC.visibility_of_element_located((By.XPATH, OrangeHRM_Locators.error_toast_saved)))
                error_text = self.driver.find_element(by=By.XPATH, value=OrangeHRM_Locators.error_toast_saved).text
                assert error_text == OrangeHRM_Data.toast_message_saved

                print("SUCCESS : Employee Details Successfully Added")

        except [NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotVisibleException, NoSuchWindowException, WebDriverException] as error:
            print('Error:', error)

    # Test Case to edit existing employee information
    def test_edit_employee(self, booting_function):
        try:

            if self.user_login():

                employee_name_box = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locators.employee_name)))
                employee_name_box.send_keys(OrangeHRM_Data.employee_name)

                search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators.search_button)))
                search_button.click()

                edit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators.edit_button)))
                edit_button.click()

                driver_license_edit = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locators.driver_license_box)))
                driver_license_edit.send_keys(OrangeHRM_Data.employee_driver_license)

                save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators.save_button_edit)))
                save_button.click()

                # Notification pop-up for details edited
                self.wait.until(EC.visibility_of_element_located((By.XPATH, OrangeHRM_Locators.error_toast_saved)))
                error_text = self.driver.find_element(by=By.XPATH, value=OrangeHRM_Locators.error_toast_saved).text
                assert error_text == OrangeHRM_Data.toast_message_edited

                print("SUCCESS : Employee Details Successfully Edited")

        except [NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotVisibleException, NoSuchWindowException, WebDriverException] as error:
            print('Error:', error)

    # Test Case to delete employee information
    def test_delete_employee(self, booting_function):
        try:

            if self.user_login():

                employee_name_box = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locators.employee_name)))
                employee_name_box.send_keys(OrangeHRM_Data.employee_name)

                search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators.search_button)))
                search_button.click()

                delete_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators.delete_button)))
                delete_button.click()

                confirmation_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators.yes_button)))
                confirmation_button.click()

                # Notification pop-up for details deleted
                self.wait.until(EC.visibility_of_element_located((By.XPATH, OrangeHRM_Locators.error_toast_saved)))
                error_text = self.driver.find_element(by=By.XPATH, value=OrangeHRM_Locators.error_toast_saved).text
                assert error_text == OrangeHRM_Data.toast_message_deleted

                print("SUCCESS : Employee Details Successfully Deleted")

        except [NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotVisibleException, NoSuchWindowException, WebDriverException] as error:
            print('Error:', error)


