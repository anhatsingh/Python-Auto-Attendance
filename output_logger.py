class logging:    
    def __init__(self, window = ""):
        self.window = window

    def write(self, valuesToUpdate, textColor = "black", backgroundColor="white"):            
        if(self.window != ""):
            self.window['logbox'].print(valuesToUpdate, text_color=textColor, background_color=backgroundColor)
            self.window.Refresh()
        else:
            print(valuesToUpdate)            
