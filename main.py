# ======================================== Meet-Auto-Attendance ====================================================================================================================================================================
# Version: 1.6
# Last Date Updated: 15 April 2021
#
# Requirements:
# 1. Python 3.6+
# 2. tesseract.exe (included in the repo)
# 3. Google OAuth credentials.json file (To get the file, follow the steps in pre-requisites at https://developers.google.com/sheets/api/quickstart/python)
# 4. Python Libraries:
#    - argparse
#    - google_api_interface
#    - pytesseract
#    - cv2
#
# To contribute, contact anhatsingh2001@gmail.com
# ==================================================================================================================================================================================================================================


from datetime import datetime
import time
startTime = datetime.now()
import argparse
import yaml

from google_api_interface import googleAPI
from dataHandler import dataHandler



# ===========================================================================================================================
# This is Argument Parser.
# This allows to pass extra argument of "date" to add into sheets. If this argument is not givem, default is today's date.
# To use it, run in CMD/Powershell as:
# py main.py -d 15-04-2021
# ===========================================================================================================================
parser = argparse.ArgumentParser(description='MathsAttendanceMarker')
parser.add_argument('-d', metavar='date',nargs='?', type=str, help='Date to add (default = '+ str(datetime.now().strftime("%d-%m-%Y")) +' sec)', default=datetime.now().strftime("%d-%m-%Y"))
theDateToAdd = str(parser.parse_args().d)

with open("config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

# ===========================================================================================================================
# Instantiate all the Classes and connect to google sheets
# ===========================================================================================================================
API = googleAPI(cfg)
data = dataHandler(cfg)

API.connectToGoogle()

# ===========================================================================================================================

getMethod = input("Which method to use: [Image to Text(I), Get data by joining meet(M), Hybrid of both methods (H)]: ").upper()

discrepancies = []

if(getMethod == "M"):    
    meetLink = input("Enter Google Meet Link: ")
    meetData, tesseractData = data.dataCollector("N", "M", meetLink)
    prepdData = data.getPreparedData(meetData)

elif(getMethod == "I"):    
    ssOrNot = input("Take Screenshots automatically (Y/N): ").upper()
    meetLink = input("Enter Google Meet Link: ") if ssOrNot == "Y" else ""

    meetData, tesseractData = data.dataCollector(ssOrNot, "I", meetLink)
    prepdData = data.getPreparedData(tesseractData)

else:
    ssOrNot = input("Take Screenshots automatically (Y/N): ")
    meetLink = input("Enter Google Meet Link: ")    
    meetData, tesseractData = data.dataCollector(ssOrNot, "H", meetLink)
    prepdData, discrepancies = data.getHybridPreparedData(tesseractData, meetData)


# ===========================================================================================================================

# ===========================================================================================================================
# get the empty column to update the data to, in google sheets
# ===========================================================================================================================
emptyColumn = API.getCoulumnToAddTo()

# ===========================================================================================================================
# add Today's date or the date given in -d argument to the first index of data
# add some extra functions to cell 119 and 120 of sheet.
# and ask the user whether to upload data or not upload the data to google sheets and do what is asked
# if not uploading data, ask if to view the data and do what is asked.
# ===========================================================================================================================
prepdData.insert(0, [theDateToAdd])
prepdData.extend([[""], ['=CONCATENATE(COUNTIF('+emptyColumn+'2:'+emptyColumn+'117, "Present"), "/116")'], ['=CONCATENATE(COUNTIF('+emptyColumn+'2:'+emptyColumn+'117, "Absent"), "/116")']])

uploadTheData = input("Upload Data? (Y/N) ").upper()
isExit = 0
while(uploadTheData != "Y" and isExit != 1):    
    print(str(datetime.now()) + ": Upload Cancelled")

    viewTheData = input("View Data? (Y/N) ").upper()
    if(viewTheData == "Y"):        
        print(" ")    
        print("Image to Text Data: ")
        print(" ")        
        for n in tesseractData:
            print(n)
            
        print(" ")    
        print("Meet Data: ")
        print(" ")
        for m in meetData:
            print(m)

    # ===========================================================================================================================
    # Give final messages and time taken to do everything
    # ===========================================================================================================================    
    endTime = datetime.now()   
    uploadTheData = input("Upload Data? (Y/N/exit) ").upper()
    if(uploadTheData == "EXIT"):
        isExit = 1
        break

if(isExit != 1):
    print(str(datetime.now()) + ": Sheets API: uploading data")
    cellsAffected = API.updateSheet("Sheet1!" + emptyColumn + "1:" + emptyColumn + str(len(prepdData)), prepdData)
    print(str(datetime.now()) + ": Sheets API: " + str(cellsAffected) + " cells updated")

if(getMethod == "H"):
    print(" ")
    print("Discrepancies: ")
    if(len(discrepancies) > 0):
        print(discrepancies)
    else:
        print("None")
    print(" ")

endTime = datetime.now()
print(str(datetime.now()) + ": EVERYTHING DONE :) ")
print("Script took " + str(endTime - startTime) + " seconds to complete")