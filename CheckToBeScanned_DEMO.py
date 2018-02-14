#Folder Checking Program
#
#Ther Purpose of this program is to go through certain
#folders inside school's share drive and print out the file names
#that needed to be processed.
#
#Updated 2/14/2018
#Version 1.2
#Written By Chia Che Chang
import os
import time

fileTypes = ['pdf', 'jpg', 'img', 'tif'] #List with potential file types

def selectFolder(path):
        if(os.path.exists(path)):
                if 'HS' in path:
                        docType = 'High School'
                elif 'Grade Change' in path:
                        docType = 'Grade Change'
                elif 'Registration Emails' in path:
                        docType = 'Registration Email'
                elif 'Transcript Info' in path:
                        docType = 'Transcript Info'

                #Check if it is Registration folder
                if docType == 'Registration Email':
                        for smallFolder in os.listdir(path)[0:3]:
                                newPath = os.path.join(path,smallFolder)
                                docType = 'Registration Emails ' + smallFolder
                                runFolder(newPath, docType)
                else:
                        runFolder(path,docType)
        else:
                print("Error! Folder path cannot be accessed")
                print("Program will close in 10 seconds")
                time.sleep(10)
                exit(1)


#The running part, taking the docType and the path
def runFolder(path, docType):
        docCount = 0
        print("*"* 5,end='')
        print("Checking " + docType, end='')
        print("*"*5)
        for filename in os.listdir(path):
                if os.path.isfile(os.path.join(path,filename)):
                    if filename[-3:].lower() in fileTypes:
                        docCount += 1
                        print(filename)
        print('*'*5, end='')
        print(" Total : [" + str(docCount) + "] " + docType + " Documents ", end='')
        print('*'*5)
        print('\n'*2)

        
#To main interface of the program
while True:
        print('='*80)
        selectFolder('PATH HERE')
        time.sleep(60)
        
