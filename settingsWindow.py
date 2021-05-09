import PySimpleGUI as sg
from db import dbms
from init_selenium import seleniumControl
from meet import meetHandler
import os.path
from sheets_api_v1 import googleAPI
from logger import logging

sg.theme("Dark2")
myDb = dbms()
log = logging()

class settingsWindow:
    def __init__(self):
        pass

    def styling(self):
        col1 = [
            [sg.Text("Subject:")]
        ]
        col2 = [
            [sg.Text("Google Sheets ID:")]
        ]
        col3 = [
            [sg.Text("Action:")]
        ]

        data = myDb.getFromSettings("type", "subject")
        
        if len(data) != 0:            
            for row in data:
                col3.append([
                    sg.Button("  Update  ", key="edit_" + str(row[0]), button_color="blue"), 
                    sg.Button(" Delete ", key="delete_" + str(row[0]), button_color="red"),
                    sg.Button(" Open Sheet", key="open_" + str(row[2]))                
                    ])            

                col1.append([sg.InputText(row[1], size=(55,1), key="subName_" + str(row[0]))])
                col2.append([sg.Text(row[2], size=(55,1), key="subValue_" + str(row[0]))])

        google = myDb.getFromSettings("type", "google")
        username = google[0][2] if len(google) !=0 else "Insert google username here"
        password = google[1][2] if len(google) !=0 else ""

        s_id = myDb.getFromSettings("type", "unique_sheet")
        unique_sheet = s_id[0][2] if len(s_id) > 0 else ""

        mainLayout = [
            [sg.Text("Google:")],
            [
                sg.Column([[sg.Text("Username: ")], [sg.InputText(username, key="usrname", size=(55,1))]]), 
                sg.Column([[sg.Text("Password: ")], [sg.InputText(password, key="pass", size=(55,1), password_char='*')]]),
                sg.Column([[sg.Text("          ")], [sg.Button(" Update ", key="updateGoogleButton")]])
            ],
            [
                sg.Column([[sg.Text("Students Data Sheet: ")], [sg.InputText(unique_sheet, key="studentData", size=(55,1))]]),                 
                sg.Column([[sg.Text("          ")], [sg.Button(" Update ", key="updateUniqueButton")]])
            ],
            [sg.HorizontalSeparator()],
            [
                sg.Column(col1),
                sg.Column(col2),
                sg.Column(col3)
            ],
            [sg.HorizontalSeparator()],
            [sg.Text("Add New Subject")],
            [sg.Column([[sg.InputText("Name of Subject", size=(55,1), key="addSubName")]]), 
            sg.Column([[sg.Checkbox("Create Google Sheet Automatically", key="createSheet", default=True, enable_events=True)]]),
            sg.Column([[sg.InputText("Paste Google-Sheets Sheet-ID Here", size=(55,1), key="addSubValue", visible=False)]])
            ],
            [sg.Button("Add subject", key="addSubButton")],          
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
                print(deleteId)
                myDb.deleteFromSettings(deleteId)                
                settingsWindow.close()
                settingsWindow = self.createSettingsWindow()                
                    
            elif setEvent == "addSubButton":
                if setValues["addSubName"] != "":
                    if(setValues["createSheet"]):
                        api = googleAPI("NoSheet", log)
                        api.connectToGoogle()
                        sheetId = api.createSpreadsheet(setValues["addSubName"])
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
                    settingsWindow['addSubValue'].update(visible=False)
                else:
                    settingsWindow['addSubValue'].update(visible=True)
            
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