class logging:    
    def __init__(self, window = ""):
        self.window = window

    def write(self, valuesToUpdate, textColor = "black", backgroundColor="white"):    
        #initial.append(valuesToUpdate)
        #window.Refresh()
        #theStr = ""
        #for a in initial:
            #theStr = theStr + str(a) + "\n"
        if(self.window != ""):
            self.window['logbox'].print(valuesToUpdate, text_color=textColor, background_color=backgroundColor)
            self.window.Refresh()
        else:
            #print(valuesToUpdate)
            pass
