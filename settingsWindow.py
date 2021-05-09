import PySimpleGUI as sg
from db import dbms
from init_selenium import seleniumControl
from meet import meetHandler
import os.path
from sheets_api_v3 import googleAPI
from logger import logging

sg.theme("Dark2")
myDb = dbms()
log = logging()

class settingsWindow:
    def __init__(self):
        pass

    def styling(self):
        data = myDb.getFromSettings("type", "subject")
        google = myDb.getFromSettings("type", "google")
        s_id = myDb.getFromSettings("type", "unique_sheet")
        
        username = google[0][2] if len(google) !=0 else "Insert google username here"
        password = google[1][2] if len(google) !=0 else ""       
        unique_sheet = s_id[0][2] if len(s_id) > 0 else ""

        sheetsData = []
        sheetsButton = []

        if len(data) != 0:
            a = 1            
            for row in data:
                sheetsData.append([
                    sg.Button(" Sheet " + str(a) + " ", key="open_" + str(row[2])),
                    sg.Text(": ", size=(6,1)),
                    sg.InputText(str(row[2]), key="subValue_" + str(row[0]), visible=False),
                    sg.InputText(row[1], size=(55,1), key="subName_" + str(row[0])),                                  
                    ])
                sheetsButton.append([
                    sg.Button(" Update ", key="edit_" + str(row[0])), 
                    sg.Button(" Delete ", key="delete_" + str(row[0]), button_color="red"),                      
                ])
                a += 1
        else:
            sheetsData.append([
                sg.Text("No class/subject added", size=(55,1), text_color="red")
            ])

        mainLayout = [
            [sg.Text("Google:")],
            [
                sg.Column([
                    [sg.Text("Username: ", size=(15,1)), sg.InputText(username, key="usrname", size=(55,1))],
                    [sg.Text("Password: ", size=(15,1)), sg.InputText(password, key="pass", size=(55,1), password_char='*')] ,
                ]),
                sg.Column([
                    [sg.Button(" Update ", key="updateGoogleButton", size=(15,1))]
                ])
            ],


            [sg.Text(" ")],
            [sg.Text("Student Data:")],
            [
                sg.Column([
                    [sg.Text("Sheet ID: ", size=(15,1)), sg.InputText(unique_sheet, key="studentData", size=(55,1))],                    
                ]),
                sg.Column([
                    [sg.Button(" Update ", key="updateUniqueButton", size=(15,1))]
                ])
            ],

            [sg.Text(" ")],
            [sg.Text("Class/Subject Sheets:")],
            [
                sg.Column(sheetsData),
                sg.Column(sheetsButton)
            ],
            [sg.Text(" ")],
            [sg.HorizontalSeparator()],
            [sg.Text(" ")],
            [sg.Text("Add Class/Subject:")],
            [
                sg.Column([
                    [sg.Text("Name of Subject: ", size=(15,1)), sg.InputText("", key="addSubName", size=(55,1))],
                    [sg.Text(" ", size=(15,1)), sg.Checkbox("Create Google Sheet Automatically", key="createSheet", default=True, enable_events=True)],
                    [sg.Text("Google-Sheets ID: ", size=(15,1)), sg.InputText("", size=(55,1), key="addSubValue", disabled_readonly_background_color="#8f9c92", disabled=True)]
                ]),
                sg.Column([
                    [sg.Button(" Add ", key="addSubButton", size=(15,1))]
                ])
            ],
         
        ]
        return mainLayout



    def createSettingsWindow(self):
        return sg.Window("Settings", [[self.styling()]]).Finalize()



    def main(self):
        settingsWindow = self.createSettingsWindow()
        #window.close()        
        while True:    
            setEvent, setValues = settingsWindow.read()
            
            if setEvent == "Exit" or setEvent == sg.WIN_CLOSED:
                #window = createMainWindow()
                break
                    
            if setEvent == "updateGoogleButton":
                if setValues["usrname"] != "" and setValues["pass"] != "":
                    
                    if len(myDb.getFromSettings("type", "google")) > 0:                        
                        myDb.updateSettings("name", ("username", setValues["usrname"], "google", "username"))
                        myDb.updateSettings("name", ("password", setValues["pass"], "google", "password"))
                    else:
                        dataToAdd = [("username", setValues["usrname"], "google"), ("password", setValues["pass"], "google")]
                        myDb.insertToSettings(dataToAdd) 

                    if os.path.exists('token.json'):
                        os.remove('token.json')
                    api = googleAPI("NoSheet", log)
                    api.connectToGoogle()
                    sg.Popup('Google login information updated', keep_on_top=True)

            elif "edit" in setEvent:
                editId = int(setEvent[5:])
                myDb.updateSettings("id", (setValues["subName_" + str(editId)], setValues["subValue_" + str(editId)], "subject", editId))
                sg.Popup('Subject information updated', keep_on_top=True)
                    
            elif "delete" in setEvent:
                deleteId = int(setEvent[7:])                
                myDb.deleteFromSettings(deleteId)                
                settingsWindow.close()
                settingsWindow = self.createSettingsWindow()                
                    
            elif setEvent == "addSubButton":
                if setValues["addSubName"] != "":
                    if(setValues["createSheet"]):
                        api = googleAPI("NoSheet", log)
                        api.connectToGoogle()
                        sheetId = api.createSpreadsheet(setValues["addSubName"])

                        un_Data = myDb.getEverythingFromUnique()
                        finalData = [["Roll Number", "Name"]]

                        if (len(un_Data) > 0):
                            for i in un_Data:
                                finalData.append([i[1], i[2]])
                        api2 = googleAPI(sheetId, log)
                        api2.connectToGoogle()                        
                        colAffected = api2.updateSheet("Sheet1!A1:B" + str(len(finalData)), finalData)

                    else:
                        sheetId = setValues["addSubValue"]
                    dataToAdd = [(setValues["addSubName"], sheetId, "subject")]
                    myDb.insertToSettings(dataToAdd)                   
                    settingsWindow.close()
                    settingsWindow = self.createSettingsWindow()     

            elif "open" in setEvent:
                sheetId = str(setEvent[5:])
                theUsername = myDb.getFromSettings("type", "google")[0][2]
                thePassword = myDb.getFromSettings("type", "google")[1][2]
                driver,action,keys = seleniumControl(1, log).igniteSelenium()
                doLogin = meetHandler(driver, action, keys, log).login(theUsername, thePassword, redirect_url = 'https://docs.google.com/spreadsheets/d/'+sheetId+'/edit')                
                    
            elif setEvent == "createSheet":
                if(setValues["createSheet"]):
                    settingsWindow['addSubValue'].update(disabled=True)
                else:
                    settingsWindow['addSubValue'].update(disabled=False)
            
            elif setEvent == "updateUniqueButton":
                if setValues["studentData"] != "":
                    
                    if len(myDb.getFromSettings("type", "unique_sheet")) > 0:                        
                        myDb.updateSettings("type", ("Sheet1", setValues["studentData"], "unique_sheet", "unique_sheet"))                        
                    else:
                        dataToAdd = [("Sheet1", setValues["studentData"], "unique_sheet")]
                        myDb.insertToSettings(dataToAdd) 

                    api = googleAPI(setValues["studentData"], log)
                    api.connectToGoogle()
                    entireData = api.getAllData()

                    testData = myDb.getFromUnique("id", "0")
                    if(len(testData) > 0):
                        myDb.dropUnique()

                    for i in range(1, len(entireData)):
                        dataToAdd = [(entireData[i][0], entireData[i][1], entireData[i][2])]
                        myDb.insertToUnique(dataToAdd)

                    sg.Popup('Done', keep_on_top=True)