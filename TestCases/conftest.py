from pygments.styles import default
from selenium import webdriver
import pytest

from Utilities.readProperties import config


@pytest.fixture()
def setup(request):
    browser=request.config.getoption('--browser').lower()
    if browser=="edge":
        driver=webdriver.Edge()
        print('launching edge browser')
    elif browser=='chrome':
        driver=webdriver.Chrome()
        print('launching chrome browser')
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print('launching Firefox browser')


    # return driver
    yield driver
    driver.quit()
def pytest_addoption(parser):
    parser.addoption('--browser',action='store',default='edge')

#################  pytest html report #############
#it is hook for adding environment info to html report
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
        metadata['Project Name']='nop commerce'
        metadata['Module Name']='Customer'
        metadata['Tester Name']='Somnath'
        metadata.pop('JAVA_HOME', None)
        metadata.pop('Plugins', None)


