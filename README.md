# Python-Auto-Attendance
Download PyTesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki)

## How to Run
1. Ensure you have credentials.json file \(To get the file, follow the steps in pre-requisites at [Google Sheets API](https://developers.google.com/sheets/api/quickstart/python)\)
2. Create a Google Sheet by going to [Google Sheets](https://docs.google.com/spreadsheets/)
3. Get the Sheet ID from https://docs.google.com/spreadsheets/d/<b>\<sheet_id_is_here\></b>/edit#gid=0
4. Paste the Sheet ID into google_api_interface.py
5. Change any "117" written in all files to number of students in your class + 1.
6. Prepare a list of your own class, and paste it into dataCompare.py

In Windows PowerShell, or CMD type:
<br />
<code> py main.py </code>

Arguments: <br />
<code> [optional] -d \<Date in dd-mm-yyyy format\></code>
  
## Todo
1. The tesseract method alone is not reliable enough to get the list of presentees, so still have to devise another method that will go in-hand with tesseract one.
2. The Google Sheet ID is hard-coded into the code, still have to devise a method to get the sheet id based on its name, if at all possible.
3. Screenshots still have to be provided to the python. Will add functionality to automatically take screenshots too.
