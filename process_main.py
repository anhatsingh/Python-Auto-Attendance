import PySimpleGUI as sg
from db import dbms
from sheets_api_v3 import googleAPI

from dataBuilder_main import dataHandler
from dataBuilder_json import jsonHandler

myDb = dbms()

def build_Data(values, log):
    myDate = values["dateToAdd"]
    loginData = myDb.getFromSettings("type", "google")
    sheet = myDb.getFromSettings("name", values["subject"])

    if(len(myDb.getFromSettings("type", "subject")) <= 0):
        log.write("Operation stopped: An error occured", textColor="red")
        sg.Popup('No Class/Subject added, exiting.', keep_on_top=True)
        exit()
   
    compiledData = {
        "date": values["dateToAdd"],
        "credentials": {
            "username" : loginData[0][2] if len(loginData) > 0 else "not_found_in_db",
            "password" : loginData[1][2] if len(loginData) > 0 else "not_found_in_db"
            },
        "sheet_id": sheet[0][2] if len(sheet) > 0 else "not_found_in_db",
        "method": "I" if values["I"] else ("M" if values["M"] else ("H" if values["H"] else "U")),
        "whatToDo": "remote" if values["uploadData"] else "local",
        "takeSS": "Y" if values["-SS-"] else "N",
        "meetLink": values["meetLink"],
        "folder": values["-FOLDER-"]
    }

    #log.write("------------------------------------------------------------------------------ Config -------------------------------------------------------------------------------")
    #log.write("Date: " + compiledData["date"])
    #log.write("Subject: " + values["subject"])
    #log.write("Sheet ID: " + compiledData["sheet_id"])
    #log.write("Method: " + compiledData["method"])
    #log.write("Save at : " + compiledData["whatToDo"])
    #log.write("Take Screenshot? " + compiledData["takeSS"])
    #log.write("Folder: " + compiledData["folder"])
    #log.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    return compiledData

def main(values, log):
    inputData = build_Data(values, log)

    if(inputData["method"] != "U"):
        data = dataHandler(inputData["credentials"]["username"], inputData["credentials"]["password"], log)
        meetData, tesseractData = data.dataCollector(inputData["takeSS"], inputData["method"], inputData["meetLink"], inputData["folder"])
        prepdData, discrepancies = data.getPresentAbsentData(inputData["method"], tesseractData, meetData)
        prepdData.insert(0, [inputData["date"]])
    else:
        meetData, tesseractData, prepdData, discrepancies = jsonHandler("data\\ready_to_upload\\").getData(inputData["date"], inputData["sheet_id"])
    
    if(meetData != None):   
            
        log.write("Re-check the following roll numbers for attendance: ", textColor="blue")    
        log.write(discrepancies, textColor="blue")    

        if(inputData["whatToDo"] == "remote"):
            API = googleAPI(inputData["sheet_id"], log)
            API.connectToGoogle()
            emptyColumn = API.getCoulumnToAddTo()
            
            prepdData.extend([
                [""], 
                ['=CONCATENATE(COUNTIF('+emptyColumn+'2:'+emptyColumn+'117, "Present"), "/116")'], 
                ['=CONCATENATE(COUNTIF('+emptyColumn+'2:'+emptyColumn+'117, "Absent"), "/116")']
            ])

            log.write("Uploading data")
            cellsAffected = API.updateSheet("Sheet1!" + emptyColumn + "1:" + emptyColumn + str(len(prepdData)), prepdData)
            log.write(str(cellsAffected) + " cells updated")
            jsonHandler('data\\logs\\').prepLocalSave(inputData, values, meetData, tesseractData, prepdData, discrepancies)

        elif(inputData["whatToDo"] == "local"):
            log.write("Saving Data Locally")
            jsonHandler('data\\ready_to_upload\\').prepLocalSave(inputData, values, meetData, tesseractData, prepdData, discrepancies)
        
        log.write("Everything Done", textColor="green")

    else:
        log.write("No saved data found for: " + inputData["date"] + ", Subject: " + values["subject"], textColor="white", backgroundColor="red")       
    #log.write("---------------------------------------------------------------------------------------------------------------------------------------")