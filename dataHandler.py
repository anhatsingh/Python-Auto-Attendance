import time
from datetime import datetime
from meet import meetHandler
from img_to_text import tesseract
from init_selenium import seleniumControl
tesseract = tesseract()
import pyscreenshot as ImageGrab
import pygetwindow as gw
import pyautogui
import math
import os

class dataHandler:

    def __init__(self, cfg):
        self.cfg = cfg

    #change this method to get data dynamically from google sheets only, and remove the hard-coded version here.
        self.classmates = {
            "karanjot" :    {"rollno" : 301,"name" : "Karanjot Singh Bhoon"},
            "1033" :        {"rollno" : 302,"name" : "Anmolpreet Singh"},
            "akhil":        {"rollno" : 303,"name" : "Akhil Aggarwal"},
            "abhinoor":     {"rollno" : 304,"name" : "Abhinoor Singh Anand"},
            "lohitaksh":    {"rollno" : 305,"name" : "Lohitaksh Devgan"},
            "harsimran":    {"rollno" : 306,"name" : "Harsimran Kaur"},
            "anhat":        {"rollno" : 307,"name" : "Anhat Singh"},
            "gurjot":       {"rollno" : 308,"name" : "Gurjot Singh"},
            "gurparteek":   {"rollno" : 309,"name" : "Gurparteek Singh"},
            "druphat":      {"rollno" : 310,"name" : "Druphat"},
            "abhay":        {"rollno" : 311,"name" : "Abhay Mahajan"},
            "harnoor":      {"rollno" : 312,"name" : "Harnoor Kaur"},
            "himanshu":     {"rollno" : 313,"name" : "Himanshu Mahajan"},
            "anu":          {"rollno" : 314,"name" : "Anu Sharma"},
            "aryan":        {"rollno" : 315,"name" : "Aryan Garg"},    
            "2254" :        {"rollno" : 316,"name" : "Ankit Dhingra"},
            "gurkirat":     {"rollno" : 317,"name" : "Gurkirat Singh"},
            "2297":         {"rollno" : 318,"name" : "Lovish Arora"},
            "bhawana":      {"rollno" : 319,"name" : "Bhawana"},
            "2574":         {"rollno" : 320,"name" : "Jaskaran Singh"},
            "aneesh":       {"rollno" : 321,"name" : "Aneesh Pawa"},
            "harmandeep":   {"rollno" : 322,"name" : "Harmandeep Singh"},
            "2804" :        {"rollno" : 323,"name" : "Anmolpreet Kaur"},
            "eknoor":       {"rollno" : 324,"name" : "Eknoor Singh"},
            "3412" :        {"rollno" : 325,"name" : "Arshdeep Singh"},
            "jasmine":      {"rollno" : 326,"name" : "Jasmine Gupta"},  
            "1564" :        {"rollno" : 327,"name" : "Akash"},
            "3585":         {"rollno" : 328,"name" : "Gurpreet Kaur"},  
            "daman":        {"rollno" : 329,"name" : "Damandeep Kaur"},
            "komalpreet":   {"rollno" : 330,"name" : "Komalpreet Kaur"},
            "ishpreet":     {"rollno" : 331,"name" : "Ishpreet Singh"},
            "akshay":       {"rollno" : 332,"name" : "Akshay Sharma"},
            "dinesh":       {"rollno" : 333,"name" : "Dinesh Kumar"},
            "koushal":      {"rollno" : 334,"name" : "Koushal Kumar"},
            "davinder":     {"rollno" : 335,"name" : "Davinder Kumar"},
            "5106" :        {"rollno" : 336,"name" : "Gagandeep Singh"},
            "harleen":      {"rollno" : 337,"name" : "Harleen Kaur"},
            "gurkirtan":    {"rollno" : 338,"name" : "Gurkirtan Singh"},
            "ajoy":         {"rollno" : 339,"name" : "Ajoy Bhat"},
            "gursavikar":   {"rollno" : 340,"name" : "Gursavikar Singh"},
            "anjali":       {"rollno" : 341,"name" : "Anjali Sharma"},
            "guramanat":    {"rollno" : 342,"name" : "Guramanat Singh"},
            "jasleen":      {"rollno" : 343,"name" : "Jasleen Kaur Cheema"},
            "lakshay":      {"rollno" : 344,"name" : "Lakshay Dhawan"},
            "chandanpreet": {"rollno" : 345,"name" : "Chandanpreet Kaur"},
            "brijesh":      {"rollno" : 346,"name" : "Brijesh Devgan"},
            "amandeep":     {"rollno" : 347,"name" : "Amandeep Kaur"},
            "6385" :        {"rollno" : 348,"name" : "Anmolpreet Singh"},
            "prabhakar":    {"rollno" : 349,"name" : "Lovish Prabhakar"},    
            "harishta":     {"rollno" : 350,"name" : "Harishta"},
            "dhruv":        {"rollno" : 351,"name" : "Dhruv Prabhal"},   
            "7113":         {"rollno" : 352,"name" : "Hapreet Singh Nagi"},
            "bhandari":     {"rollno" : 353,"name" : "Lovish Bhandari"},
            "gauri":        {"rollno" : 354,"name" : "Gauri Kaushal"},
            "kulpreet":     {"rollno" : 355,"name" : "Kulpreet Singh"},
            "7648" :        {"rollno" : 356,"name" : "Arshdeep Kaur"},
            "abhinav":      {"rollno" : 357,"name" : "Abhinav Kumar Setia"},
            "goutam":       {"rollno" : 358,"name" : "Goutam"},
            "arshmeet":     {"rollno" : 359,"name" : "Arshmeet Kaur"},
            "anureet":      {"rollno" : 360,"name" : "Anureet Kaur"},
            "jaspreet":     {"rollno" : 361,"name" : "Jaspreet Kaur"},
            "arshpreet":    {"rollno" : 362,"name" : "Arshpreet Kaur"},
            "archit":       {"rollno" : 363,"name" : "Archit Sehgal"},
            "inderpreet":   {"rollno" : 364,"name" : "Inderpreet Singh"},
            "8508":         {"rollno" : 365,"name" : "Harshpreet Singh"},
            "8639" :        {"rollno" : 366,"name" : "Aditya Sharma"},
            "367" :         {"rollno" : 367,"name" : "Gaurav Garg"},
            "aarushin":     {"rollno" : 368,"name" : "Aarushin Katoch"},
            "0740":         {"rollno" : 369,"name" : "Inderpal Kaur"},
            "divyansh":     {"rollno" : 370,"name" : "Divyansh"},
            "kritika":      {"rollno" : 371,"name" : "Kritika Mehra"},
            "harkeerat":    {"rollno" : 372,"name" : "Harkeerat Kaur"},
            "divya":        {"rollno" : 373,"name" : "Divya Singla"},
            "gurneet":      {"rollno" : 374,"name" : "Gurneet Singh"},
            "keerat":       {"rollno" : 375,"name" : "Keerat Singh"},
            "avinaash":     {"rollno" : 376,"name" : "Avinaash Kumar"},
            "harkirat":     {"rollno" : 377,"name" : "Harkirat Singh"},
            "akant":        {"rollno" : 378,"name" : "Akant Salaria"},
            "aniket":       {"rollno" : 379,"name" : "Aniket Behal"},
            "bhavy":        {"rollno" : 380,"name" : "Bhavy Dhir"},
            "2775" :        {"rollno" : 381,"name" : "Gourav Goyal"},
            "3375" :        {"rollno" : 382,"name" : "Gagandeep"},
            "ashok":        {"rollno" : 383,"name" : "Ashok Palwa"},
            "karandeep":    {"rollno" : 384,"name" : "Karandeep Singh"},
            "bhupinder":    {"rollno" : 385,"name" : "Bhupinder Kaur"},
            "gurman":       {"rollno" : 386,"name" : "Gurman Singh Marahar"},
            "armaandeep":   {"rollno" : 387,"name" : "Armaandeep Singh"},
            "atul":         {"rollno" : 388,"name" : "Atul Kumar"},
            "anushka":      {"rollno" : 389,"name" : "Anushka"},
            "jaskarandeep": {"rollno" : 390,"name" : "Jaskarandeep Singh"},
            "deepak":       {"rollno" : 391,"name" : "Deepak Arora"},
            "sethi":        {"rollno" : 392,"name" : "Ankit Sethi"},
            "soni":         {"rollno" : 393,"name" : "Anchal Soni"},
            "kalia":        {"rollno" : 394,"name" : "Dhruv Kalia"},
            "abhishek":     {"rollno" : 395,"name" : "Abhishek"},
            "dupinder":     {"rollno" : 396,"name" : "Dupinder Kour"},
            "kavya":        {"rollno" : 397,"name" : "Kavya"},
            "gunjan":       {"rollno" : 398,"name" : "Gunjan Zutshi"},
            "heman":        {"rollno" : 399,"name" : "Heman Sharma"},
            "krishnam":     {"rollno" : 400,"name" : "Krishnam Jandyal"},
            "hriday":       {"rollno" : 401,"name" : "Hriday Sareen"},
            "kriti":        {"rollno" : 402,"name" : "Kriti Rana"},
            "ishveen":      {"rollno" : 403,"name" : "Ishveen Kour"},
            "7112" :        {"rollno" : 404,"name" : "Aditya"},
            "divit":        {"rollno" : 405,"name" : "Divit Gupta"},
            "harman":       {"rollno" : 406,"name" : "Harman Singh Saini"},
            "harpreet":     {"rollno" : 407,"name" : "Hapreet Kaur"}, ######change this identifier later 5809
            "1007" :        {"rollno" : 408,"name" : "Gaganpreet Singh"},
            "kartik":       {"rollno" : 409,"name" : "Kartik Bhardwaj"},
            "koul" :        {"rollno" : 410,"name" : "Akash Koul"},
            "8112" :        {"rollno" : 411,"name" : "Kumar Aryan"},
            "eshan":        {"rollno" : 412,"name" : "Eshan Sengupta"},
            "marina":       {"rollno" : 413,"name" : "Marina Barakzai"},
            "asakzai":      {"rollno" : 414,"name" : "Asakzai Khan Karimi"},
            "mansoor":      {"rollno" : 415,"name" : "Mansoor Hejran"},
            "7295" :        {"rollno" : 416,"name" : "Aditya Sharma"}
        }

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
        print(str(datetime.now()) + ": Data: making absentees list")

        # from "presentees", make a new list of students that are not present in presentees but are in classmates
        absentees = [a for a in self.classmates if a not in presentees]
        prepdData = []

        print(str(datetime.now()) + ": Data: preparing final list to upload to sheets")
        for i in self.classmates:           # Iterate through "classmates"
            count = 0
            for j in absentees:             # Iterate through "Absentees"
                if(i == j):
                    count += 1              # If student is in Absentees, count++
            
            sampleList = ["Present"] if count == 0 else ["Absent"]    # mark Absent, if student is in Absentees else Present
            prepdData.append(sampleList)    # add this to prepdData[] in-order, to update to sheet
        
        print(str(datetime.now()) + ": Data: list prepared")
        return prepdData                

    
    
    def getHybridPreparedData(self, imgToText_Presentees, meet_Presentees):
        list1 = self.getPreparedData(imgToText_Presentees)
        list2 = self.getPreparedData(meet_Presentees)       

        discrepancies = []

        for i in range(len(list1)):
            if(list1[i] != list2[i]):
                discrepancies.append(i+301)

        return list1, discrepancies

 
 
    def dataCollector(self, ss, method, meetLink):        
        theMeetData = []
        theTesseractData = []        

        if(ss == "Y"):
            driver,action,keys = seleniumControl.igniteSelenium(0)
            meet = meetHandler(driver, action, keys)
            doLogin = meet.login(self.cfg["google"]["username"], self.cfg["google"]["password"])  # attempt to login to google using username and password
            if(doLogin):        
                meet.joinMeet("https://meet.google.com/" + meetLink)
                time.sleep(3)
                ############take ss here
                imgDirectory = self.takeSS(driver, meetLink)
                #imgDirectory = ""

                if(method == "M"):
                    theMeetData = meet.getDataFromMeet(meetLink)
                elif(method == "I"):
                    theTesseractData = tesseract.getTextFromImg(imgDirectory)
                else:
                    theMeetData = meet.getDataFromMeet(meetLink)
                    theTesseractData = tesseract.getTextFromImg(imgDirectory)
        else:
            if(method == "M"):
                driver,action,keys = seleniumControl.igniteSelenium(0)
                meet = meetHandler(driver, action, keys)
                doLogin = meet.login(self.cfg["google"]["username"], self.cfg["google"]["password"])  # attempt to login to google using username and password
                if(doLogin):        
                    meet.joinMeet("https://meet.google.com/" + meetLink)
                    time.sleep(5)
                    theMeetData = meet.getDataFromMeet(meetLink)
            elif(method == "I"):
                theTesseractData = tesseract.getTextFromImg("images/")
            else:                
                theTesseractData = tesseract.getTextFromImg("images/")
                driver,action,keys = seleniumControl.igniteSelenium(0)
                meet = meetHandler(driver, action, keys)
                doLogin = meet.login(self.cfg["google"]["username"], self.cfg["google"]["password"])  # attempt to login to google using username and password
                if(doLogin):        
                    meet.joinMeet("https://meet.google.com/" + meetLink)
                    time.sleep(5)
                    theMeetData = meet.getDataFromMeet(meetLink)                    
                
        return theMeetData, theTesseractData

    def takeSS(self, driver, meetLink):
        meetWindow = gw.getWindowsWithTitle(meetLink + " - Google Chrome")[0]        
        meetWindow.activate()
        meetWindow.resizeTo(1366, 768)
        meetWindow.moveTo(0,0)
        #pyautogui.click(1340, 90)
        #time.sleep(10)
        pyautogui.click(1050, 100)
        time.sleep(3)
        numOfParticipants = driver.find_element_by_class_name('rua5Nb').text        
        brackets = ["(", ")"]
        for x in numOfParticipants:
            if x in brackets:
                numOfParticipants = numOfParticipants.replace(x, "")  
        dir = "autoImg/" + str(datetime.now().strftime("%d-%m-%Y")) + "/"
        os.mkdir(dir)

        if(int(numOfParticipants) > 7):
            numOfScrolls = (int(numOfParticipants)/7.5)
            #pyautogui.moveTo(1360, 640)
            eachDrag = (640-190)/numOfScrolls            
            pyautogui.click(1360, 190)
            for i in range(1, math.ceil(numOfScrolls) + 1):
                pyautogui.click(1360, 205 + (eachDrag*(i - 1)))
                time.sleep(1)
                im = ImageGrab.grab(bbox=(1010, 190, 1330, 640))  # X1,Y1,X2,Y2
                im.save(dir + "image"+str(i)+".png")         
        pyautogui.click(1340, 90)
        return dir

#dataHandler("abcd").takeSS("jkp-pkpv-awa")