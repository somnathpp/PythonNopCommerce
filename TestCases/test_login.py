import time
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen
import pytest
class Test_001_Login:
    base_url = Readconfig.getAppUrl()
    user_name = Readconfig.getUserEmail()
    password = Readconfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info('*********** Test_001_Login Started **********')
        self.logger.info('*********** Verifying homePageTitle **********')

        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        act_title=self.driver.title
        if act_title=='Automation Practice Store. Login':
            self.logger.info('*********** homePageTitle Test is Passed **********')
            assert True
        else:
            self.driver.save_screenshot('.\\ScreenShots\\test_homePageTitle.png')
            self.logger.error('*********** homePageTitle Test is Failed **********')

            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info('*********** Verifying LoginFunctionality **********')
        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        lp=LoginPage(self.driver)
        lp.setUserName(self.user_name)
        lp.setPassword(self.password)
        lp.ClickLogin()
        time.sleep(3)
        act_title=self.driver.title
        if act_title=='Dashboard - Automation Practice Store':
            self.logger.info('*********** Login Functionality Test is Passed **********')
            assert True
        else:
            self.logger.error('*********** Login Functionality Test is Failed **********')
            self.driver.save_screenshot('.\\ScreenShots\\test_login.png')
            assert False
