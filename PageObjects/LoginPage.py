from selenium.webdriver.common.by import By


class LoginPage:
    UserName_id='username'
    Password_id='password'
    login_button_xpath='//button[@id="login-button"]'
    logout_button_xpath=' /html/body/div/aside/ul/li[6]/a'

    def __init__(self,driver):
        self.driver=driver
    def setUserName(self,usr):
        self.driver.find_element(By.ID,self.UserName_id).clear()
        self.driver.find_element(By.ID, self.UserName_id).send_keys(usr)

    def setPassword(self, pwd):
        self.driver.find_element(By.ID, self.Password_id).clear()
        self.driver.find_element(By.ID, self.Password_id).send_keys(pwd)
    def ClickLogin(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def ClickLogout(self):
        self.driver.find_element(By.XPATH,self.logout_button_xpath).click()
