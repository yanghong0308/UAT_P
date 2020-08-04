from selenium import webdriver
from selenium.webdriver.common.keys  import  Keys
import time
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True

def denglu():
    bs = webdriver.Ie()
    bs.implicitly_wait(10)
    bs.get("http://10.144.102.213:7060/itoa/index")
    bs.find_element_by_id("username").send_keys("zhoutao")
    bs.find_element_by_id("password").send_keys("vjsp2020!!!")
    bs.find_element_by_id("selflogin").send_keys(Keys.ENTER)
    time.sleep(3)
    bs.find_element_by_xpath(xpath="//a[contains(.,'总部立项批复')]").click()
    bs.find_element_by_xpath(xpath="//a[contains(.,'总部立项批复')]/following-sibling::div[1]/a").send_keys(Keys.ENTER)
    time.sleep(10)
    # bs.close()

denglu()
#def dakaimokuai():

import win32api