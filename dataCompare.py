import time
from datetime import datetime

class dataHandler:

    def __init__(self):

    #change this method to get data dynamically from google sheets only, and remove the hard-coded version here.
        self.classmates = {
            "karanjot" :    {"rollno" : 301,"name" : "Karanjot Singh Bhoon"},
            "1033" :        {"rollno" : 302,"name" : "Anmolpreet Singh"},
            "akhil":        {"rollno" : 303,"name" : "Akhil Aggarwal"},
            "abhinoor":     {"rollno" : 304,"name" : "Abhinoor Singh Anand"},
            "lohitaksh":    {"rollno" : 305,"name" : "Lohitaksh Devgan"},
            "harsimran":    {"rollno" : 306,"name" : "Harsimran Kaur"},
            "anhat":        {"rollno" : 307,"name" : "Anhat Singh"},
            "gurjot":       {"rollno" : 308,"name" : "Gurjot Singh"},
            "gurparteek":   {"rollno" : 309,"name" : "Gurparteek Singh"},
            "druphat":      {"rollno" : 310,"name" : "Druphat"},
            "abhay":        {"rollno" : 311,"name" : "Abhay Mahajan"},
            "harnoor":      {"rollno" : 312,"name" : "Harnoor Kaur"},
            "himanshu":     {"rollno" : 313,"name" : "Himanshu Mahajan"},
            "anu":          {"rollno" : 314,"name" : "Anu Sharma"},
            "aryan":        {"rollno" : 315,"name" : "Aryan Garg"},    
            "2254" :        {"rollno" : 316,"name" : "Ankit Dhingra"},
            "gurkirat":     {"rollno" : 317,"name" : "Gurkirat Singh"},
            "2297":         {"rollno" : 318,"name" : "Lovish Arora"},
            "bhawana":      {"rollno" : 319,"name" : "Bhawana"},
            "2574":         {"rollno" : 320,"name" : "Jaskaran Singh"},
            "aneesh":       {"rollno" : 321,"name" : "Aneesh Pawa"},
            "harmandeep":   {"rollno" : 322,"name" : "Harmandeep Singh"},
            "2804" :        {"rollno" : 323,"name" : "Anmolpreet Kaur"},
            "eknoor":       {"rollno" : 324,"name" : "Eknoor Singh"},
            "3412" :        {"rollno" : 325,"name" : "Arshdeep Singh"},
            "jasmine":      {"rollno" : 326,"name" : "Jasmine Gupta"},  
            "1564" :        {"rollno" : 327,"name" : "Akash"},
            "3585":         {"rollno" : 328,"name" : "Gurpreet Kaur"},  
            "daman":        {"rollno" : 329,"name" : "Damandeep Kaur"},
            "komalpreet":   {"rollno" : 330,"name" : "Komalpreet Kaur"},
            "ishpreet":     {"rollno" : 331,"name" : "Ishpreet Singh"},
            "akshay":       {"rollno" : 332,"name" : "Akshay Sharma"},
            "dinesh":       {"rollno" : 333,"name" : "Dinesh Kumar"},
            "koushal":      {"rollno" : 334,"name" : "Koushal Kumar"},
            "davinder":     {"rollno" : 335,"name" : "Davinder Kumar"},
            "5106" :        {"rollno" : 336,"name" : "Gagandeep Singh"},
            "harleen":      {"rollno" : 337,"name" : "Harleen Kaur"},
            "gurkirtan":    {"rollno" : 338,"name" : "Gurkirtan Singh"},
            "ajoy":         {"rollno" : 339,"name" : "Ajoy Bhat"},
            "gursavikar":   {"rollno" : 340,"name" : "Gursavikar Singh"},
            "anjali":       {"rollno" : 341,"name" : "Anjali Sharma"},
            "guramanat":    {"rollno" : 342,"name" : "Guramanat Singh"},
            "jasleen":      {"rollno" : 343,"name" : "Jasleen Kaur Cheema"},
            "lakshay":      {"rollno" : 344,"name" : "Lakshay Dhawan"},
            "chandanpreet": {"rollno" : 345,"name" : "Chandanpreet Kaur"},
            "brijesh":      {"rollno" : 346,"name" : "Brijesh Devgan"},
            "amandeep":     {"rollno" : 347,"name" : "Amandeep Kaur"},
            "6385" :        {"rollno" : 348,"name" : "Anmolpreet Singh"},
            "prabhakar":    {"rollno" : 349,"name" : "Lovish Prabhakar"},    
            "harishta":     {"rollno" : 350,"name" : "Harishta"},
            "dhruv":        {"rollno" : 351,"name" : "Dhruv Prabhal"},   
            "7113":         {"rollno" : 352,"name" : "Hapreet Singh Nagi"},
            "bhandari":     {"rollno" : 353,"name" : "Lovish Bhandari"},
            "gauri":        {"rollno" : 354,"name" : "Gauri Kaushal"},
            "kulpreet":     {"rollno" : 355,"name" : "Kulpreet Singh"},
            "7648" :        {"rollno" : 356,"name" : "Arshdeep Kaur"},
            "abhinav":      {"rollno" : 357,"name" : "Abhinav Kumar Setia"},
            "goutam":       {"rollno" : 358,"name" : "Goutam"},
            "arshmeet":     {"rollno" : 359,"name" : "Arshmeet Kaur"},
            "anureet":      {"rollno" : 360,"name" : "Anureet Kaur"},
            "jaspreet":     {"rollno" : 361,"name" : "Jaspreet Kaur"},
            "arshpreet":    {"rollno" : 362,"name" : "Arshpreet Kaur"},
            "archit":       {"rollno" : 363,"name" : "Archit Sehgal"},
            "inderpreet":   {"rollno" : 364,"name" : "Inderpreet Singh"},
            "8508":         {"rollno" : 365,"name" : "Harshpreet Singh"},
            "8639" :        {"rollno" : 366,"name" : "Aditya Sharma"},
            "367" :         {"rollno" : 367,"name" : "Gaurav Garg"},
            "aarushin":     {"rollno" : 368,"name" : "Aarushin Katoch"},
            "0740":         {"rollno" : 369,"name" : "Inderpal Kaur"},
            "divyansh":     {"rollno" : 370,"name" : "Divyansh"},
            "kritika":      {"rollno" : 371,"name" : "Kritika Mehra"},
            "harkeerat":    {"rollno" : 372,"name" : "Harkeerat Kaur"},
            "divya":        {"rollno" : 373,"name" : "Divya Singla"},
            "gurneet":      {"rollno" : 374,"name" : "Gurneet Singh"},
            "keerat":       {"rollno" : 375,"name" : "Keerat Singh"},
            "avinaash":     {"rollno" : 376,"name" : "Avinaash Kumar"},
            "harkirat":     {"rollno" : 377,"name" : "Harkirat Singh"},
            "akant":        {"rollno" : 378,"name" : "Akant Salaria"},
            "aniket":       {"rollno" : 379,"name" : "Aniket Behal"},
            "bhavy":        {"rollno" : 380,"name" : "Bhavy Dhir"},
            "2775" :        {"rollno" : 381,"name" : "Gourav Goyal"},
            "3375" :        {"rollno" : 382,"name" : "Gagandeep"},
            "ashok":        {"rollno" : 383,"name" : "Ashok Palwa"},
            "karandeep":    {"rollno" : 384,"name" : "Karandeep Singh"},
            "bhupinder":    {"rollno" : 385,"name" : "Bhupinder Kaur"},
            "gurman":       {"rollno" : 386,"name" : "Gurman Singh Marahar"},
            "armaandeep":   {"rollno" : 387,"name" : "Armaandeep Singh"},
            "atul":         {"rollno" : 388,"name" : "Atul Kumar"},
            "anushka":      {"rollno" : 389,"name" : "Anushka"},
            "jaskarandeep": {"rollno" : 390,"name" : "Jaskarandeep Singh"},
            "deepak":       {"rollno" : 391,"name" : "Deepak Arora"},
            "sethi":        {"rollno" : 392,"name" : "Ankit Sethi"},
            "soni":         {"rollno" : 393,"name" : "Anchal Soni"},
            "kalia":        {"rollno" : 394,"name" : "Dhruv Kalia"},
            "abhishek":     {"rollno" : 395,"name" : "Abhishek"},
            "dupinder":     {"rollno" : 396,"name" : "Dupinder Kour"},
            "kavya":        {"rollno" : 397,"name" : "Kavya"},
            "gunjan":       {"rollno" : 398,"name" : "Gunjan Zutshi"},
            "heman":        {"rollno" : 399,"name" : "Heman Sharma"},
            "krishnam":     {"rollno" : 400,"name" : "Krishnam Jandyal"},
            "hriday":       {"rollno" : 401,"name" : "Hriday Sareen"},
            "kriti":        {"rollno" : 402,"name" : "Kriti Rana"},
            "ishveen":      {"rollno" : 403,"name" : "Ishveen Kour"},
            "7112" :        {"rollno" : 404,"name" : "Aditya"},
            "divit":        {"rollno" : 405,"name" : "Divit Gupta"},
            "harman":       {"rollno" : 406,"name" : "Harman Singh Saini"},
            "harpreet":     {"rollno" : 407,"name" : "Hapreet Kaur"}, ######change this identifier later 5809
            "1007" :        {"rollno" : 408,"name" : "Gaganpreet Singh"},
            "kartik":       {"rollno" : 409,"name" : "Kartik Bhardwaj"},
            "koul" :        {"rollno" : 410,"name" : "Akash Koul"},
            "8112" :        {"rollno" : 411,"name" : "Kumar Aryan"},
            "eshan":        {"rollno" : 412,"name" : "Eshan Sengupta"},
            "marina":       {"rollno" : 413,"name" : "Marina Barakzai"},
            "asakzai":      {"rollno" : 414,"name" : "Asakzai Khan Karimi"},
            "mansoor":      {"rollno" : 415,"name" : "Mansoor Hejran"},
            "7295" :        {"rollno" : 416,"name" : "Aditya Sharma"}
        }

    # ==================================================================================================================================
    # getPreparedData() method returns <list<list>> "absent or present"
    #
    # This method takes in the text converted from images/ directory (presentees) and:
    # 1. Compare it with the "classmates" to get list of people present in "classmates" but not in "presentees".
    # 2. Mark Absent or Present order-wise against "classmates".
    # 3. Return this list
    #
    # TODO: This method does not validate if the present or absent is marking against the right person, it just marks
    # the attendence order-wise. Change this method later to verify the person it is marking attendance for.


    def getPreparedData(self, presentees):
        print(str(datetime.now()) + ": Data: making absentees list")

        # from "presentees", make a new list of students that are not present in presentees but are in classmates
        absentees = [a for a in self.classmates if a not in presentees]
        prepdData = []

        print(str(datetime.now()) + ": Data: preparing final list to upload to sheets")
        for i in self.classmates:           # Iterate through "classmates"
            count = 0
            for j in absentees:             # Iterate through "Absentees"
                if(i == j):
                    count += 1              # If student is in Absentees, count++
            
            sampleList = ["Present"] if count == 0 else ["Absent"]    # mark Absent, if student is in Absentees else Present
            prepdData.append(sampleList)    # add this to prepdData[] in-order, to update to sheet
        
        print(str(datetime.now()) + ": Data: list prepared")
        return prepdData                
