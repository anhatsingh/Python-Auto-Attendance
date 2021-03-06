from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options

class seleniumControl:
    def __init__(self, instanceNumber, logger):
        self.instanceNumber = instanceNumber 
        self.log = logger               

    def igniteSelenium(self):        
        opt = Options()
        opt.add_argument("--disable-infobars")
        opt.add_argument("start-maximized")
        opt.add_argument("--disable-extensions")        
        # Pass the argument 1 to allow and 2 to block

        self.log.write("Opening Chrome browser")
        opt.add_experimental_option("prefs", { \
            "profile.default_content_setting_values.media_stream_mic": 1, 
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 0, 
            "profile.default_content_setting_values.notifications": 1,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        opt.add_experimental_option('excludeSwitches', ['enable-logging', "enable-automation"])
        opt.add_experimental_option("useAutomationExtension", False)
        

        #driver = webdriver.Chrome(chrome_options=opt, executable_path=r'C:\Utility\BrowserDrivers\chromedriver.exe')        
        driver = webdriver.Chrome(chrome_options = opt, executable_path=r'chromedriver.exe')
        action = ActionChains(driver)
        self.log.write("Browser Opened")
        
        return(driver,action, Keys)
