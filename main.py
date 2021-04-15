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
from google_api_interface import googleAPI
from img_to_text import tesseract
from dataCompare import dataHandler

# ===========================================================================================================================
# This is Argument Parser.
# This allows to pass extra argument of "date" to add into sheets. If this argument is not givem, default is today's date.
# To use it, run in CMD/Powershell as:
# py main.py -d 15-04-2021
# ===========================================================================================================================
parser = argparse.ArgumentParser(description='MathsAttendanceMarker')
parser.add_argument('-d', metavar='date',nargs='?', type=str, help='Date to add (default = '+ str(datetime.now().strftime("%d-%m-%Y")) +' sec)', default=datetime.now().strftime("%d-%m-%Y"))
theDateToAdd = str(parser.parse_args().d)

# ===========================================================================================================================
# Instantiate all the Classes and connect to google sheets
# ===========================================================================================================================
API = googleAPI()
tesseract = tesseract()
data = dataHandler()
API.connectToGoogle()

# ===========================================================================================================================
# get the text from images in the directory "images/"
# ===========================================================================================================================
getTextFromImg = tesseract.getTextFromImg("images/")

# ===========================================================================================================================
# get data already prepared to be uploaded to sheets.
# ===========================================================================================================================
prepdData = data.getPreparedData(getTextFromImg)
#print(getTextFromImg)

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
        print("Text Found From Images:")
        print(getTextFromImg)
        print("Final Prepared Data:")
        print(prepdData)

    # ===========================================================================================================================
    # Give final messages and time taken to do everything
    # ===========================================================================================================================    
    endTime = datetime.now()
    print("Script took " + str(endTime - startTime) + " seconds to complete")
    print(str(datetime.now()) + ": EVERYTHING DONE :) ")
    uploadTheData = input("Upload Data? (Y/N/exit) ").upper()
    if(uploadTheData == "EXIT"):
        isExit = 1
        break

if(isExit != 1):
    print(str(datetime.now()) + ": Sheets API: uploading data")
    cellsAffected = API.updateSheet("Sheet1!" + emptyColumn + "1:" + emptyColumn + str(len(prepdData)), prepdData)

    print(str(datetime.now()) + ": Sheets API: " + str(cellsAffected) + " cells updated")
    endTime = datetime.now()
    print("Script took " + str(endTime - startTime) + " seconds to complete")
    print(str(datetime.now()) + ": EVERYTHING DONE :) ")