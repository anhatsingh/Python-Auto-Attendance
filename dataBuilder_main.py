import time, math, os, pyautogui
import pyscreenshot as ImageGrab
import pygetwindow as gw
import PySimpleGUI as sg
from datetime import datetime

from chromedriver import seleniumControl
from db import dbms

from dataBuilder_meet import meetHandler
import dataBuilder_tesseract
from dataBuilder_json import jsonHandler

myDb = dbms()


class dataHandler:

    def __init__(self, username, password, logger):
        self.username = username
        self.password = password
        self.log = logger    

        finalData = dict([])
        dbData = myDb.getEverythingFromUnique()
    
        if len(dbData) > 0:
            for i in dbData:            
                finalData[i[3]] = {"rollno" : i[1], "name": i[2]}
        else:
            unique_sheet_id = myDb.getFromSettings("type", "unique_sheet")
            if len(unique_sheet_id) == 0:
                sg.Popup('No data sheet set in settings, please set sheet. \n\nTerminating Program', keep_on_top=True)
                exit()
        
        self.classmates = finalData

    # ==================================================================================================================================
    # getPreparedData() method returns <list<list>> "absent or present"
    #
    # This method takes in the text converted from images/ directory (presentees) and:
    # 1. Compare it with the "classmates" to get list of people present in "classmates" but not in "presentees".
    # 2. Mark Absent or Present order-wise against "classmates".
    # 3. Return this list
    #
    # TODO: This method does not validate if the present or absent is marking against the right person, it just marks
    # the attendence order-wise. Change this method later to verify the person it is marking attendance for.


    def getPreparedData(self, presentees):
        self.log.write("Making absentees list")

        # from "presentees", make a new list of students that are not present in presentees but are in classmates
        absentees = [a for a in self.classmates if a not in presentees]
        prepdData = []
        
        for i in self.classmates:           # Iterate through "classmates"
            count = 0
            for j in absentees:             # Iterate through "Absentees"
                if(i == j):
                    count += 1              # If student is in Absentees, count++
            
            sampleList = ["Present"] if count == 0 else ["Absent"]    # mark Absent, if student is in Absentees else Present
            prepdData.append(sampleList)    # add this to prepdData[] in-order, to update to sheet
        
        return prepdData                

    
    
    def getPresentAbsentData(self, method, imgToText_Presentees, meet_Presentees):
        if(method == "M"):        
            list1 = self.getPreparedData(meet_Presentees)
            discrepancies = ["only available for hybrid method"]

        elif(method == "I"):        
            list1 = self.getPreparedData(imgToText_Presentees)
            discrepancies = ["only available for hybrid method"]

        elif(method == "H"):                    
            list1 = self.getPreparedData(imgToText_Presentees)
            list2 = self.getPreparedData(meet_Presentees)       

            discrepancies = []

            for i in range(len(list1)):
                if(list1[i] != list2[i]):
                    discrepancies.append(i+301)

        return list1, discrepancies

 
 
    def dataCollector(self, ss, method, meetLink, folder):        
        theMeetData = []
        theTesseractData = []
        tesseract = dataBuilder_tesseract.tesseract(self.log)

        if(ss == "Y"):
            driver,action,keys = seleniumControl(0, self.log).igniteSelenium()
            meet = meetHandler(driver, action, keys, self.log)
            doLogin = meet.login(self.username, self.password)  # attempt to login to google using username and password
            if(doLogin):        
                meet.joinMeet("https://meet.google.com/" + meetLink)
                time.sleep(3)
                ############take ss here
                imgDirectory = self.takeSS(driver, meetLink, folder)
                #imgDirectory = ""

                if(method == "M"):
                    theMeetData = meet.getDataFromMeet(meetLink)                    
                elif(method == "I"):
                    theTesseractData = tesseract.getTextFromImg(imgDirectory)
                else:
                    theMeetData = meet.getDataFromMeet(meetLink)
                    theTesseractData = tesseract.getTextFromImg(imgDirectory)
                meet.doLogout()
        else:
            if(method == "M"):
                driver,action,keys = seleniumControl(0, self.log).igniteSelenium()
                meet = meetHandler(driver, action, keys, self.log)
                doLogin = meet.login(self.username, self.password)  # attempt to login to google using username and password
                if(doLogin):        
                    meet.joinMeet("https://meet.google.com/" + meetLink)
                    time.sleep(5)
                    theMeetData = meet.getDataFromMeet(meetLink)
                    meet.doLogout()
            elif(method == "I"):
                theTesseractData = tesseract.getTextFromImg(folder + "\\")

            else:
                theTesseractData = tesseract.getTextFromImg(folder + "\\")
                
                driver,action,keys = seleniumControl(0, self.log).igniteSelenium()
                meet = meetHandler(driver, action, keys, self.log)
                doLogin = meet.login(self.username, self.password)  # attempt to login to google using username and password
                if(doLogin):        
                    meet.joinMeet("https://meet.google.com/" + meetLink)
                    time.sleep(5)
                    theMeetData = meet.getDataFromMeet(meetLink)
                    meet.doLogout()
                
        return theMeetData, theTesseractData

    def takeSS(self, driver, meetLink, folder):
        #meetWindow = gw.getWindowsWithTitle(meetLink + " - Google Chrome")[0]

        self.log.write("Taking Screenshots from Meet")

        meetWindow = gw.getWindowsWithTitle("Google Chrome")[0]
        meetWindow.activate()
        meetWindow.maximize()
        max_X, max_Y = pyautogui.size()          

        #PW=> participants Window
        dimensioning = {
            "show_PW_Button": {
                "X": (1050/1366)*max_X, 
                "Y": (100/768)*max_Y
            },
            "PW_StartPosition": {      
                "X": (1010/1366)*max_X, 
                "Y": (190/768)*max_Y
            },
            "PW_EndPosition": {
                "X": (1330/1366)*max_X, 
                "Y": (640/768)*max_Y
            },
            "scroll_each_Position": {
                "X": (1360/1366)*max_X, 
                "Y": (205/768)*max_Y
            },
            "scroll_first_click": {
                "X": (1360/1366)*max_X,
                "Y": (190/768)*max_Y
            },
            "close_PW_Button": {
                "X": (1340/1366)*max_X, 
                "Y": (90/768)*max_Y
            }
        }

        #meetWindow.resizeTo(1366, 768)
        #meetWindow.moveTo(0,0)

        #pyautogui.click(1340, 90)
        #time.sleep(10)
        time.sleep(2)
        driver.find_element_by_class_name(".uArJ5e.UQuaGc.kCyAyd.QU4Gid.foXzLb.IeuGXd.M9Bg4d").click()
        #pyautogui.click(dimensioning["show_PW_Button"]["X"], dimensioning["show_PW_Button"]["Y"])
        time.sleep(2)

        self.log.write("Getting Number of Participants")
        numOfParticipants = driver.find_element_by_class_name('rua5Nb').text        
        brackets = ["(", ")"]
        for x in numOfParticipants:
            if x in brackets:
                numOfParticipants = numOfParticipants.replace(x, "")  
        
        self.log.write(numOfParticipants + " people found")
        if(os.path.isdir(folder) == False):
            os.mkdir(folder)       

        if(int(numOfParticipants) > 7):
            numOfScrolls = (int(numOfParticipants)/7.5)            
            #pyautogui.moveTo(1360, 640)
            eachDrag = (dimensioning["PW_EndPosition"]["Y"]-dimensioning["PW_StartPosition"]["Y"])/numOfScrolls            
            pyautogui.click(dimensioning["scroll_first_click"]["X"], dimensioning["scroll_first_click"]["Y"])            
            
            for i in range(1, math.ceil(numOfScrolls) + 1):
                self.log.write("Taking Screenshot " + str(i) + " / " + str(math.ceil(numOfScrolls)))

                pyautogui.click(dimensioning["scroll_each_Position"]["X"], dimensioning["scroll_each_Position"]["Y"] + (eachDrag*(i - 1)))                
                time.sleep(1)

                im = ImageGrab.grab(bbox=(int(dimensioning["PW_StartPosition"]["X"]), int(dimensioning["PW_StartPosition"]["Y"]), int(dimensioning["PW_EndPosition"]["X"]), int(dimensioning["PW_EndPosition"]["Y"])))  # X1,Y1,X2,Y2
                im.save(folder + "\\image"+str(i)+".png")

            self.log.write(str(math.ceil(numOfScrolls)) + " Screenshots taken")

        pyautogui.click(dimensioning["close_PW_Button"]["X"], dimensioning["close_PW_Button"]["Y"])
        return folder + "\\"