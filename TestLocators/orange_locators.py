"""
orange_locators.py

Program : File containing the Locators for OrangeHRM
"""


class OrangeHRM_Locators:

   username = "username"
   password = "password"
   submit_button = "//button[@type='submit']"
   invalid_login_message = "//div[@class='oxd-alert-content oxd-alert-content--error']//p"
   pim_button = "//span[text()='PIM']"
   add_employee_button = "//a[text()= 'Add Employee']"
   first_name_box = "//input[@name='firstName']"
   last_name_box = "//input[@name='lastName']"
   driver_license_box = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input"
   employee_id_box = "//input[@class='oxd-input oxd-input--focus']"
   save_button_add = "//div[@class='oxd-form-actions']//button[2]"
   employee_name = "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"
   search_button = "//div[@class='oxd-form-actions']//button[2]"
   edit_button = "//i[@class='oxd-icon bi-pencil-fill']"
   save_button_edit = "//form[@class='oxd-form']//div[4]//button"
   delete_button = "//i[@class='oxd-icon bi-trash']"
   yes_button = "//div[@class='orangehrm-modal-footer']//button[2]"
   error_toast_saved = "//div[@class='oxd-toast-content oxd-toast-content--success']//p[2]"


