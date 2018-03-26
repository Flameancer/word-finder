#!/usr/bin/python3

import sys
import re

def main():
#takes an argument and reads it into a file
    file = sys.argv[1]
    wordList = {}

    #opens the file then closes it after the loop is over
    with open(file, 'r', encoding="utf-8") as wordFile:
        '''
        Takes a file and for every line in the file it removes the /n. Then for every line it
        it creates a list of words from the words on the line and splits on the space. Each word
        has all puncuation removed and set to lowercase. It then checks the dictionary if the 
        word is in there. If the word is in the dictionary it updates the value of the word by one. 
        If not it adds it to the list.
        '''
        for line in wordFile:
            line = line.strip()
            #print (line)
            wordOList = line.split(" ")
            #print (wordOList)
            for word in wordOList:
                newWord = re.sub('[^A-Za-z0-9]+', '', word)
                newWord = newWord.lower()
                #print (newWord)
                if newWord in wordList:
                    wordList[newWord] = wordList.get(newWord) + 1
        
                else:
                    wordList[newWord] = 1
    
    print (wordList)
    wordCount = (len(wordList))
    countStr = f"There are {wordCount} individual 'words' in the List of words!"
    print (countStr)
    comWord = (max(wordList.keys(), key=(lambda k: wordList[k])))
    numWord = wordList[comWord]
    countStr2 = f"The most common word is '{comWord}' which appears {numWord} times!"
    print (countStr2)
 
main()
