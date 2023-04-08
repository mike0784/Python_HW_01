import csv
import os.path
from workingWithFile import fileCSV
from pattern import *
from menu import *
import datetime
import time
fileName = "D:/Mike/py/message.csv"

def verificationFile(ff):
    if not os.path.exists(ff):
        with open(ff, mode="w", encoding='utf-8') as w_file:
            f = csv.writer(w_file, delimiter = delimiter, lineterminator = "\r")
            f.writerow(pattern)

verificationFile(fileName)
obj = fileCSV(fileName)
obj.readAll()

o = menu(fileName)
o.run()