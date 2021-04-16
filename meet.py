import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pygetwindow as gw
import pyautogui

class meetHandler:

    def __init__(self, driver, action, keys):
        self.driver = driver
        self.action = action
        self.keys = keys

    def login(self, username, passwd):
        print(str(datetime.now()) + ": Google: initiating login")
        try:            
            self.driver.get(r'https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&_ga=2.2277811.2089757821.1617366170-1054544264.1617366170&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
            self.driver.implicitly_wait(15)

            
            loginBox = self.driver.find_element_by_xpath('//*[@id ="identifierId"]')
            loginBox.send_keys(username)
            print(str(datetime.now()) + ": Google: username ********** filled")
            
            nextButton = self.driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
            nextButton[0].click()
                    
            passWordBox = self.driver.find_element_by_xpath(
                '//*[@id ="password"]/div[1]/div / div[1]/input')
            passWordBox.send_keys(passwd)
            print(str(datetime.now()) + ": Google: password ********** filled")
        
            nextButton = self.driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
            nextButton[0].click()

            time.sleep(5)
            print(str(datetime.now()) + ": Google: login successful")
            return 1            
        except:
            print(str(datetime.now()) + ": Google: login failed")
            return 0


    def joinMeet(self, meetLink):
        print(str(datetime.now()) + ": Meet: initiating meeting")

        self.driver.get(meetLink)        
        self.driver.implicitly_wait(100)

            
        self.driver.find_element_by_css_selector('body').send_keys(self.keys.CONTROL + 'd')
        print(str(datetime.now()) + ": Meet: mic turned off")
        self.driver.find_element_by_css_selector('body').send_keys(self.keys.CONTROL + 'e')
        print(str(datetime.now()) + ": Meet: camera turned off")

        time.sleep(3)
        print(str(datetime.now()) + ": Meet: joining now")
        self.driver.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
        print(str(datetime.now()) + ": Meet: waiting to join")

        waitingToJoin = 1
        while(waitingToJoin):
            try:                
                if(self.driver.find_element_by_css_selector('span.wnPUne.N0PJ8e')):
                    waitingToJoin = 0
                    print(str(datetime.now()) + ": Meet: joining successful")
            except:
                print(str(datetime.now()) + ": Meet: waiting to join")



    def doLogout(self):
        self.driver.close()        
        print(str(datetime.now()) + ": Meet: exit successful")

    def getDataFromMeet(self, meetLink):
        time.sleep(3)
        meetWindow = gw.getWindowsWithTitle(meetLink + " - Google Chrome")[0]        
        meetWindow.activate()
        meetWindow.resizeTo(1366, 768)
        meetWindow.moveTo(0,0)
        pyautogui.click(1050, 100)
        #self.driver.find_element_by_css_selector('div[jsname="VyLmyb"]').click()        
        time.sleep(2)        
        print("getting elements")
        participants = self.driver.find_elements_by_class_name("ZjFb7c")
        prepdList = []
        for i in participants:
            eachName = i.get_attribute("innerText").lower().split()
            for a in eachName:
                prepdList.append(a)

        return prepdList
        
            