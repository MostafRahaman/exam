from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Login():
    def loginTest_001(self):
        driver = webdriver.Firefox(executable_path="D:\pythonProject\Automation\Drivers\geckodriver_0.31.0.exe")

        driver.get("http://dashboard.nexivent.com/login")
        time.sleep(3)

        # WebElements
        client_ID = driver.find_element(By.NAME, 'clientId')
        email = driver.find_element(By.NAME, 'email')
        password = driver.find_element(By.NAME, 'password')
        Login_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/div/div/div/div[1]/div/form/div[2]/button')


        # Login Action
        client_ID.send_keys('value')
        time.sleep(3)

        email.send_keys('value')
        time.sleep(3)

        password.send_keys('value')
        time.sleep(3)


        Login_btn.click()
        time.sleep(5)

        driver.close()


test_obj = Login()
test_obj.loginTest_001()

####Check if registration was successful or if it failed due to an existing user
if "registration successful" in driver.page_source.lower():
        print("Registration successful!")
    elif "user already exists" in driver.page_source.lower():
        print("Registration failed. User already exists.")
    else:
        print("Registration status unknown. Please check manually.")