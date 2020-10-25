# created by Mestafa Kamal

import sys
import os
import shutil
import argparse
import csv
import text_cleaning as tc

fileName="../corrected/Azalntayri.pdf.txt"

vocabulary = open("result.txt", "wt", encoding="utf-8")
with open(fileName, "rt", encoding="utf-8") as originalFile:
    i = 0
    for row in originalFile:
        sentence = row.replace("\n", "")
        cleanedSentence = tc.cleanSentence(sentence)
        print("S :", sentence)
        print("CS:", cleanedSentence)
        vocabulary.write(cleanedSentence + "\n")        

originalFile.close()
vocabulary.close()
