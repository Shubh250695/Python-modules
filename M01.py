# write a Python program to read data from a file which has text containing emails,
# write only the emails from the file into another file.
# You can use 're' module to extract emails from the text file.

import re

fileToRead = 'Sample01.txt'
fileToWrite = 'Output01.txt'

delimiterInFile = [',', ';']

def validateEmail(strEmail):
    # .* Zero or more characters of any type. 
    if re.match("(.*)@(.*).(.*)", strEmail):
        return True
    return False

def writeFile(listData):
    file = open(fileToWrite, 'w+')
    strData = ""
    for item in listData:
        strData = strData+item+'\n'
    file.write(strData)

listEmail = []
file = open(fileToRead, 'r') 
listLine = file.readlines()

for itemLine in listLine:
    item =str(itemLine)
    for delimeter in delimiterInFile:
        item = item.replace(str(delimeter),' ')
    
    wordList = item.split()
    for word in wordList:
        if(validateEmail(word)):
            listEmail.append(word)

if listEmail:
    print(len(listEmail),"emails collected and you get it in Output01.txt.")
    print("\n")
    print(listEmail)
    writeFile(listEmail)
else:
    print("No email found.")