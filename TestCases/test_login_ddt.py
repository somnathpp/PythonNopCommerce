import time
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils
import pytest
class Test_002_DDT_Login:
    base_url = Readconfig.getAppUrl()
    path='.\\TestData\\LoginData.xlsx'
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info('*********** Test_002_DDT_Login **********')
        self.logger.info('*********** Verifying Login DDT test **********')
        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        rows=XLUtils.getRowCount(self.path,'Sheet1')
        print(rows)
        lst_status = []
        for r in range(2,rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.pwd=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.pwd)
            self.lp.ClickLogin()
            time.sleep(3)
            act_title=self.driver.title
            exp_title='Dashboard - Automation Practice Store'
            if act_title==exp_title:
                if self.exp=='Pass':
                    self.logger.info('***********   Passed **********')
                    self.lp.ClickLogout()
                    lst_status.append('pass')

                elif self.exp=='Fail':
                    self.logger.info('***********  Failed **********')
                    self.lp.ClickLogout()
                    lst_status.append('fail')

            elif act_title!=exp_title:
                if self.exp == 'Fail':
                    self.logger.info('***********  Passed **********')
                    lst_status.append('pass')
                elif self.exp == 'Pass':
                    self.logger.info('***********  Failed **********')
                    lst_status.append('fail')

        if 'fail' not in lst_status:
            self.logger.info('*********** test_login_ddt is Passed **********')
            self.driver.close()
            assert True
        else:
            self.logger.info('*********** test_login_ddt is Failed **********')
            self.driver.close()
            assert False
        self.logger.info('*********** End Of Login DDT Test**********')
        self.logger.info('*********** Completed Test_002_DDT_Login **********')


