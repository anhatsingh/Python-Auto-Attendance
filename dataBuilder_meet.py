import time, pyautogui, urllib
import pygetwindow as gw
from datetime import datetime

class meetHandler:

    def __init__(self, driver, action, keys, logger):
        self.driver = driver
        self.action = action
        self.keys = keys
        self.log = logger

    def login(self, username, passwd, redirect_url = "https://google.com"):
        redirect_url = urllib.parse.quote(redirect_url, safe='')
        self.log.write("Google: Signing-in, please wait")
        try:            
            self.driver.get(r'https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue='+ redirect_url+'&_ga=2.2277811.2089757821.1617366170-1054544264.1617366170&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
            self.driver.implicitly_wait(15)

            
            loginBox = self.driver.find_element_by_xpath('//*[@id ="identifierId"]')
            loginBox.send_keys(username)
            self.log.write("Google: username ********** filled")
            
            nextButton = self.driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
            nextButton[0].click()
                    
            passWordBox = self.driver.find_element_by_xpath(
                '//*[@id ="password"]/div[1]/div / div[1]/input')
            passWordBox.send_keys(passwd)
            self.log.write("Google: password ********** filled")
        
            nextButton = self.driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
            nextButton[0].click()

            time.sleep(5)
            self.log.write("Google: login successful")
            return 1            
        except:
            self.log.write("Google: login failed")
            return 0


    def joinMeet(self, meetLink):
        self.log.write("Meet: initiating meeting")

        self.driver.get(meetLink)        
        self.driver.implicitly_wait(100)

            
        self.driver.find_element_by_css_selector('body').send_keys(self.keys.CONTROL + 'd')
        self.log.write("Meet: mic turned off")
        self.driver.find_element_by_css_selector('body').send_keys(self.keys.CONTROL + 'e')
        self.log.write("Meet: camera turned off")

        time.sleep(3)
        self.log.write("Meet: joining now")
        self.driver.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
        self.log.write("Meet: waiting to join")

        waitingToJoin = 1
        while(waitingToJoin):
            try:                
                if(self.driver.find_element_by_css_selector('span.wnPUne.N0PJ8e')):
                    waitingToJoin = 0
                    self.log.write("Meet: joining successful")
            except:
                self.log.write("Meet: waiting to join")



    def doLogout(self):
        self.driver.close()        
        self.log.write("Meet: exit successful")

    def getDataFromMeet(self, meetLink):
        self.log.write("Getting Data from Meet: " + meetLink + ", Please wait")
        time.sleep(3)

        meetWindow = gw.getWindowsWithTitle("Google Chrome")[0]        
        meetWindow.activate()
        meetWindow.resizeTo(1366, 768)
        meetWindow.moveTo(0,0)
        pyautogui.click(1050, 100)
        #self.driver.find_element_by_css_selector('div[jsname="VyLmyb"]').click()        
        time.sleep(2)                
        participants = self.driver.find_elements_by_class_name("ZjFb7c")

        prepdList = []
        self.log.write("Preparing final data")
        for i in participants:
            eachName = i.get_attribute("innerText").lower().split()
            for a in eachName:
                prepdList.append(a)
        
        self.log.write("Data successfully obtained from Google Meet")
        return prepdList
        
            