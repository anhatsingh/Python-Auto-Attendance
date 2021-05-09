from db import dbms
import PySimpleGUI as sg
from settingsWindow import settingsWindow as sw
from datetime import datetime
import mainFunc as func
import os
from logger import logging as logs

sg.theme("Dark2")
myDb = dbms()

class mainWindow:
    def __init__(self):
        self.tempDirectory = os.getcwd() + "\\temp"

    def styling(self):
        subjects = []
        for i in myDb.getFromSettings("type", "subject"):
            subjects.append(i[1])
        
        if len(subjects) == 0:
            subjects.append("Please insert a subject")

        finalLayout = [            
            [                
             sg.Text("Date: ", size=(15,1)), 
             sg.InputText(str(datetime.now().strftime("%d-%m-%Y")), key="dateToAdd", size=(65,1), enable_events=True)                
            ],
            
            [
                sg.Text("Subject:" , size=(15,1)), 
                sg.Combo(subjects, key="subject", size=(63,1), default_value=subjects[0])                
            ],            
            [
                sg.Text("Choose Method:\t",),
                sg.Radio(text="Image to text", group_id="method", key = "I", default = True, enable_events=True),
                sg.Radio(text="Meet", group_id="method", key = "M", enable_events=True),
                sg.Radio(text="Hybrid", group_id="method", key = "H", enable_events=True),
                sg.Radio(text="Upload data of " + str(datetime.now().strftime("%d-%m-%Y")), group_id="method", key = "U", enable_events=True)
            ],
            [
                sg.Text("", size=(15,1)),
                sg.Checkbox("Take Screenshots Automatically", enable_events=True, default = False, key="-SS-"),
                sg.Checkbox("Upload Data to google Sheets", key="uploadData", default=True)
            ],            
            #[
                #sg.Text("What to Do:\t"),
                #sg.Radio(text="Upload data To Google Sheets", group_id="method2", key = "uploadData", default = True),
                #sg.Radio(text="Save data locally", group_id="method2", key = "saveData", default = False)
            #],                
            [
                sg.Text("Meet Link:\t"), sg.InputText(disabled_readonly_background_color="#8f9c92", key="meetLink", size=(65,1), disabled=True)
            ],
            [
                sg.Text("Images Folder:\t", key="directoryText"), sg.In(self.tempDirectory, disabled_readonly_background_color="#8f9c92", size=(65, 1), enable_events=True, key="-FOLDER-"), sg.FolderBrowse(size=(11, 1))
            ],
         
                        
            [
                sg.Button("Begin", size=(85,1), key="beginOp"), 
                #sg.Button("Take SS Only", size=(27,1), key="ssOnlyButton", disabled=True),     
                #sg.Button("Download JSON Data Only", size=(27,1), key="jsonDownloadButton", disabled=True)
            ],
            #    sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        #        sg.FolderBrowse(),            
            [
                #sg.HorizontalSeparator(),
                sg.Text("")
            ],
            [
                sg.Text("Log Box:")
            ],
            [
                sg.Multiline(key="logbox", size=(96,20), autoscroll=True, disabled=True)
            ],
            [                
                sg.Text("", size=(60,1)),
                sg.Button("   Clear Logs   ", key="clearLog"),
                sg.Button("   Settings   ", key="settingsMenu")
            ]
            
        ]
        return finalLayout

    def createMainWindow(self):
        return sg.Window("Python Auto Attendance", [[self.styling()]]).Finalize()

    def main(self):
        window = self.createMainWindow()
        log = logs(window)
        while True:    
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            #logger.updateBox("Event " + str(i) + " " + event)
            
            if event == "beginOp":
                self.disableWindow(window,  True)
                log.write("Operation Begun, Please Wait...", textColor = "blue")
                func.main(values, log)
                self.disableWindow(window,  False)
                #init_op(values, logger).startOp()
                
            if (event == "dateToAdd"):
                if values["-SS-"] == True:
                    window['-FOLDER-'].update(os.getcwd() + "\\data\\images\\" + values["dateToAdd"])
                window['U'].update(text="Upload data of " + values["dateToAdd"])

            if values["U"] == True:
                window['directoryText'].update("JSON Folder:\t")
                window['uploadData'].update(value=True)
                #window['saveData'].update(disabled=True)
                window['uploadData'].update(disabled=True)                
                window['-SS-'].update(disabled=True)
                window['-FOLDER-'].update(os.getcwd() + "\\data\\ready_to_upload\\")
                window['-FOLDER-'].update(disabled=True)
                window['meetLink'].update(disabled=True)
            
            elif values["I"] == True:
                window['directoryText'].update("Images Folder:\t")        
                #window['saveData'].update(disabled=False)
                window['-SS-'].update(disabled=False)
                #window['meetLink'].update(disabled=False)
                #window['-FOLDER-'].update(self.tempDirectory)
                #window['-FOLDER-'].update(disabled=False)
                
                if values["-SS-"] == True:
                    #window.Refresh()
                    window['-FOLDER-'].update(os.getcwd() + "\\data\\images\\" + values["dateToAdd"])
                    window['-FOLDER-'].update(disabled=True)
                    window['meetLink'].update(disabled=False)        
                else:        
                    window['-FOLDER-'].update(self.tempDirectory)
                    window['-FOLDER-'].update(disabled=False)
                    window['meetLink'].update(disabled=True)
            
            elif values["M"] == True:
                window['directoryText'].update("Images Folder:\t")        
                #window['saveData'].update(disabled=False)
                window['uploadData'].update(disabled=False)
                window['-SS-'].update(disabled=True)
                window['meetLink'].update(disabled=False)
                window['-FOLDER-'].update("")
                window['-FOLDER-'].update(disabled = True)
                #window['-FOLDER-'].update(disabled=False)
            
            elif values["H"] == True:
                window['directoryText'].update("Images Folder:\t")        
                #window['saveData'].update(disabled=False)
                window['uploadData'].update(disabled=False)
                window['-SS-'].update(disabled=False)
                window['meetLink'].update(disabled=False)
                
                if values["-SS-"] == True:
                    #window.Refresh()
                    window['-FOLDER-'].update(os.getcwd() + "\\data\\images\\" + values["dateToAdd"])
                    window['-FOLDER-'].update(disabled=True)            
                else:        
                    window['-FOLDER-'].update(self.tempDirectory)
                    window['-FOLDER-'].update(disabled=False)            
            
            if event == "settingsMenu":
                window.close()
                sw().main()
                window = self.createMainWindow()

            if event == "clearLog":
                window["logbox"].update("")
                
        window.close()

    def disableWindow(self, window, whatToDo):
        obj = ["dateToAdd", "subject", "I", "M", "H", "U", "-SS-", "uploadData", "meetLink", "-FOLDER-", "beginOp", "clearLog", "settingsMenu"]
        for i in obj:
            window[i].update(disabled=whatToDo)        

mainWindow().main()