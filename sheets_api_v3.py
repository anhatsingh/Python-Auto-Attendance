from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from datetime import datetime

# The permissions google API requires are given in scopes.
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

class googleAPI:

    def __init__(self, sheetId, logger):
        self.sheetID = sheetId
        self.sheet = ""
        self.log = logger

    # ==================================================================================================================================
    # connectToGoogle() method returns <void>
    # This method connects to google using OAuth2.0, get the google sheet we need to work on.
    # Do not edit the things in this method, I copy-pasted from someone else's example, as I
    # did not want to open my code to security loopholes.
    # This method requires a credential.json file which is not provided in the repo, since it
    # is my personal account.
    # To get the file, follow the steps in pre-requisites at https://developers.google.com/sheets/api/quickstart/python    
    # ==================================================================================================================================

    def connectToGoogle(self):
        self.log.write("Connecting to Google Sheets")
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        self.sheet = service.spreadsheets() # this might give error in Visual Studio, ignore it, it works perfectly.

    # ==================================================================================================================================
    # updateSheet() method returns <int> "number of rows updated"
    # This method requires 2 parameters to call, "range" and "values".
    # This simply adds/updates cells of Range passed in "range" parameter, with values passed using "values" parameter.
    # ==================================================================================================================================
    def updateSheet(self, range, values):
        body = {
            'values': values       # this can have additional options to edit how data is being uploaded, I am using no special params
        }
        result = self.sheet.values().update(        # .update() method of Google API to update the sheets
                spreadsheetId = self.sheetID,       # the sheet ID being updated.
                range = range,                      # the range to update the values to
                valueInputOption = "USER_ENTERED",  # making this as "USER_ENTERED" updates the data as if it is being typed into the sheet itself.
                body = body                         # the things to upload to the sheet
            ).execute()                             # execute the request using Google Sheets API
        


        requestBody = {
            "requests": [
                {
                    "autoResizeDimensions": {
                        "dimensions": {
                        "sheetId": 0,
                        "dimension": "COLUMNS",
                        "startIndex": 0,
                        "endIndex": len(values[0])
                        }
                    },                
                }
            ]
        }
        response = self.sheet.batchUpdate(spreadsheetId=self.sheetID, body=requestBody).execute()

        rowsAffected = result.get('updatedCells')   # get the number of Rows affected, just to verify, that something has changed in sheets.
        return rowsAffected                         # return this number of rows back.

    # ==================================================================================================================================
    # getColumnToAddTo() method returns <string> "Columns To Add Data To"
    # The problem I faced while updating data, was that I could not find a direct method to get the last
    # row or column to update the data to. There were in-direct methods, but I was not fully satisfied with
    # the complexities they brought with them, so I created my own method.
    #
    # What I noticed was, that if the Sheet in Google is arranged like this:
    # ------------------------------------
    # | A1 | B1 | C1 | D1 | E1 | F1 | G1 |
    # ------------------------------------
    # | A2 | B2 | C2 | D2 | E2 | F2 | G2 |
    # ------------------------------------
    # | A3 | B3 | C3 | D3 | E3 | F3 | G3 |
    # ------------------------------------
    # | A4 | B4 | C4 | D4 | E4 | F4 | G4 |
    # ------------------------------------
    # | A5 | B5 | C5 | D5 | E5 | F5 | G5 |
    # ------------------------------------
    # 
    # then the .get() method of Sheets Api returns a list of lists, arranged like this:
    # [[A1, B1, C1, D1, E1, F1, G1], [A2, B2, C2, D2, E2, F2, G2], [A3, B3, C3, D3, E3, F3, G3], 
    #  [A4, B4, C4, D4, E4, F4, G4], [A5, B5, C5, D5, E5, F5, G5]]
    #
    # So, what I do is, get the length of first list (i.e. first row) to get my desired column to fill.
    # Now this length returns me a number, whereas google sheets is having columns as A,B,C.....AA,AB,AC......etc etc.
    # So, I convert the number to alphabets using some maths tricks.
    # 
    # The method I used:
    # 1. let us say, the length of first array is N, so we need to add new data into Nth column.
    # 2. We need to form "AABB...." as column name.
    # 3. I declare a list of alphabets [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
    # 4. I divide N by 26 (as there are 26 aplhabets in english), and get the integral part I only.    
    # 5. Now I get the I-1 index from my alphabets list (i.e 1-1 = 0 i.e "A" from the list) and this forms the first letter of the column.
    # 6. I again divide N by 26 and get the remainder R, and get the R-1 index from the list and this forms the 2nd letter of the column.
    # 7. So, our column is formed as "alphabet[I-1] + alphabet[R-1]"
    #
    # Example:
    # let N=28
    # Integral part I is 28/26 = 1.
    # R = 2, R-1 = 2-1 = 1 = "B"
    # Alphabet formed is "AB"
    # 
    # Limitation of above method:
    # I can only get two lettered columns max i.e. upto "ZZ" or upto N = 26*26 = 676
    # ==================================================================================================================================

    def getCoulumnToAddTo(self):        

        result = self.sheet.values().get(           # .get() method of sheets API gets the data from a certain range. Only non-empty rows and columns are returned
                spreadsheetId = self.sheetID,       # the sheet to get data from
                range = "Sheet1!A1:AB117"           # get All Data from a very large random range
            ).execute()                             # execute the request using Google Sheets API

        rows = result.get('values', [])             # get the result obtained as an list of lists
        
        if(len(rows) > 0):
            numberOfColumnsFilled = len(rows[0])        # get the first array from the list of lists
        else:
            numberOfColumnsFilled = 0

        emptyColumn = self.getLetter(numberOfColumnsFilled)
        self.log.write("Uploading data to column '" + emptyColumn + "'")

        return emptyColumn                          # return the column to be updated.
    

    def getLetter(self, number):        
        listOfAlphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")    # make a list of aplhabets.
        if(number >= 26):            
            theLetter = self.getLetter(int(number/26) - 1)
            number = int(number%26)
        else:
            theLetter = ""        
        theLetter = theLetter + listOfAlphabets[(number%26)]
        return theLetter

    
    def createSpreadsheet(self, title):
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = self.sheet.create(body=spreadsheet,fields='spreadsheetId').execute()
        return spreadsheet.get('spreadsheetId')


    def getAllData(self):        
        result = self.sheet.values().get(           # .get() method of sheets API gets the data from a certain range. Only non-empty rows and columns are returned
                spreadsheetId = self.sheetID,       # the sheet to get data from
                range = "Sheet1!A1:ZZ10000"           # get All Data from a very large random range
            ).execute()                             # execute the request using Google Sheets API

        rows = result.get('values', [])             # get the result obtained as an list of lists
        return rows