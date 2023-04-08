import time
import datetime
from pattern import *
def viewNote(var):
    print(f'{pattern[0]}: {var[pattern[0]]}\n{pattern[1]}: {var[pattern[1]]}\n{pattern[2]}: {var[pattern[2]]}\n{pattern[3]}: {formatDateTime(var[pattern[3]])}\n{pattern[4]}: {formatDateTime(var[pattern[4]])}\n')

def formatDateTime(a):
    var = float(a)
    result = datetime.datetime.fromtimestamp(var).strftime("%d-%m-%Y %H:%M:%S")
    return result