import json
from datetime import datetime
from os import listdir
from os.path import isfile, join
import os

class jsonHandler:

    def __init__(self, directory):
        self.directory = directory


    def prepLocalSave(self, inputData, values, meetData, tesseractData, prepdData, discrepancies):
        data = {}
        data["config"] = {            
            "values" : values
        }
        data["processedData"] = {
            "meet" : meetData,
            "tesseract" : tesseractData,
            "prepdData" : prepdData,
            "discrepancies" : discrepancies
        }
        
        with open(self.directory  + str(datetime.now().strftime("%Y%m%d%H%M%S")) + "__" + inputData["sheet_id"] + "___" + inputData["date"] + '.json', 'w') as outfile:
            json.dump(data, outfile)

    
    def getData(self, theDate, sheetId): 
        listOffiles = [f for f in listdir(self.directory) if isfile(join(self.directory, f))]
        theFile = [a for a in listOffiles if sheetId + "___" + theDate in a]        

        if(len(theFile) > 0 and os.path.isfile(self.directory + theFile[-1])):
            f = open(self.directory + theFile[-1],)
            data = json.load(f)
            f.close()
            return data["processedData"]["meet"], data["processedData"]["tesseract"], data["processedData"]["prepdData"], data["processedData"]["discrepancies"] 
        else:
            return None, None, None, None