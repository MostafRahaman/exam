from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Reg():

    def loginTest_001(self):
        driver = webdriver.Firefox(executable_path="D:\pythonProject\Automation\Drivers\geckodriver_0.31.0.exe")

        driver.get("http://dashboard.nexivent.com/register")
        time.sleep(3)

        # WebElements
        first_name = driver.find_element(By.NAME, 'firstName')
        last_name = driver.find_element(By.NAME, 'lastName')
        Username_field = driver.find_element(By.NAME, 'username')
        company= driver.find_element(By.NAME, 'company')
        local = driver.find_element(By.NAME, 'locale')
        email = driver.find_element(By.NAME, 'email')
        password = driver.find_element(By.XPATH, '//*[@id="exampleInputPassword"]')
        reset_password = driver.find_element(By.XPATH, '//*[@id="exampleRepeatPassword"]')
        Login_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/div/div/div/div[1]/div/form/div[2]/button')


        # Login Action
        first_name.send_keys('value')
        time.sleep(3)

        last_name.send_keys('value')
        time.sleep(3)

        Username_field.send_keys('value')
        time.sleep(3)

        company.send_keys('value')
        time.sleep(3)

        local.send_keys('value')
        time.sleep(3)

        email.send_keys('value')
        time.sleep(3)

        password.send_keys('value')
        time.sleep(3)

        reset_password.send_keys('value')
        time.sleep(3)


        Login_btn.click()
        time.sleep(5)

        driver.close()


test_obj = Reg()
test_obj.loginTest_001()