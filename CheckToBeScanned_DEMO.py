import os
userInput = ''


def selectFolder(path):
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


#The running part, taking the docType and the path
def runFolder(path, docType):
        docCount = 0
        print("*"* 5,end='')
        print("Checking " + docType, end='')
        print("*"*5)
        for filename in os.listdir(path):
                if os.path.isfile(os.path.join(path,filename)):
                    if filename.endswith('.pdf') or filename.endswith('.jpg') :
                        docCount += 1
                        print(filename)
        print('*'*5, end='')
        print(" Total : [" + str(docCount) + "] " + docType + " Documents ", end='')
        print('*'*5)
        print('\n'*2)

        
#To main interface of the program
while userInput != 'q':
        selectFolder('Z:\HS Transcripts\To be scanned')
        selectFolder('Z:\Records Scan Docs\To be scanned\BSID - Grade Change')
        selectFolder('Z:\Records Scan Docs\To be scanned\BSID - Registration Emails')
        selectFolder('Z:\Records Scan Docs\To be scanned\BSID - Transcript Info')
        userInput = input('Press enter to refresh, q to quit: ')
