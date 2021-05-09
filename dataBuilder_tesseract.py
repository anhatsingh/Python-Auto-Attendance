from cv2 import cv2
import pytesseract
import re
from os import listdir
import os
from os.path import isfile, join
from datetime import datetime

# location of tesseract CMD

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class tesseract:

    def __init__(self, logger):
        self.log = logger

    # ==================================================================================================================================
    # getTextFromImg() method return <list> "text extracted from images"
    # This method is used to extract text from images.
    # This method takes 1 arguement, the directory to look into, for images.    
    # ==================================================================================================================================

    def load_images_from_folder(self, folder):
        images = []
        for filename in os.listdir(folder):
            img = cv2.imread(os.path.join(folder,filename))
            if img is not None:
                images.append(filename)
        return images

    def getTextFromImg(self, directory):        

        self.log.write("Extracting text from images")

        #images = [f for f in listdir(directory) if isfile(join(directory, f))]      # get a list of all images in the given directory
        images = self.load_images_from_folder(directory)        
        extractedText = []

        for i in images:    
            eachImg = cv2.imread(directory + i)                                     # read each image using python's library.
            eachText = pytesseract.image_to_string(eachImg)                    # convert each image to text using tesseract
            singleImageSplittedToEachWord = eachText.lower().split()           # convert all text to lowercase and convert to a list.
            
            for a in singleImageSplittedToEachWord:                                 # add all elements to the extractedText[] list for each image
                extractedText.append(a)
        
        unwantedElements = {'\\', 'ns', '<', '—', '(', ')', '&', 'ee', 'g', 'ee', 'a', 'b'}
        extractedText = [element for element in extractedText if element not in unwantedElements]   # this simply removes all the unwanted elements from the extractedText[] list.

        finalList = []
        for i in extractedText:                                                     # this removes all the non-alpha-numeric characters from each element
            pattern = re.compile(r'[\W_]+')
            finalList.append(pattern.sub('', i))
        
        return finalList                                                            # return this final processed list