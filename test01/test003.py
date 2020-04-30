import selenium.webdriver

import win32api,win32con


def zhucebiao():
    key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,
                              'Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BROWSER_EMULATION',
                              0, win32con.KEY_ALL_ACCESS)
    print(key)
    a=win32api.RegQueryValue(key, '')
    print(a)



def Iejierong():
    Ieb = selenium.webdriver.Ie()
    mate = 'meta http-equiv="X-UA-Compatible" content="IE=9"'
    Ieb.get("ww.baid.com")
    Ieb.execute_script(mate)

zhucebiao()