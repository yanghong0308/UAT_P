import winreg as wg
def xiugaiIe(xx):
    key_test = wg.OpenKey(wg.HKEY_LOCAL_MACHINE,r'SOFTWARE\Wow6432Node\Microsoft\Internet Explorer\MAIN\FeatureControl\FEATURE_BROWSER_EMULATION',0,wg.KEY_ALL_ACCESS)
    wg.SetValueEx(key_test,"iexplore.exe",'',wg.REG_DWORD,xx)
    wg.CloseKey(key_test)

if __name__ == "__main__":
    xiugaiIe(11000)