import csv
import time
from pattern import *
class fileCSV():
    fileName = ""

    def __init__(self, fileName):
        self.fileName = fileName

    def insert(self, head, note):
        countMax = 0
        with open(self.fileName, encoding='utf-8') as r_file:
            read_file = csv.DictReader(r_file, delimiter = delimiter)
            for row in read_file:
                if int(row[pattern[0]]) > countMax:
                    countMax = int(row[pattern[0]])

        with open(self.fileName, mode="a", encoding='utf-8') as w_file:
            write_file = csv.DictWriter(w_file, delimiter=delimiter, lineterminator="\r", fieldnames=pattern)
            write_file.writerow({pattern[0]: str(countMax+1), pattern[1]: head, pattern[2]: note, pattern[3]: str(round(time.time())), pattern[4]:'0' })

    def read(self, id):
        result = self.readCSVFile()
        if self.verificationNote(result, id):
            for row in result:
                if row[pattern[0]] == id:
                    return result[num]
        else:
            return 0

    def readAll(self):
        result = self.readCSVFile()
        return result

    def update(self, id, head, note):
        result = self.readCSVFile()
        if self.verificationNote(result, id):
            for item in range(0, len(result)):
                if result[item][pattern[0]] == id:
                    result[item][pattern[1]] = head
                    result[item][pattern[2]] = note
                    result[item][pattern[4]] = str(round(time.time()))
            with open(self.fileName, mode="w", encoding='utf-8') as w_file:
                write_file = csv.DictWriter(w_file, delimiter=delimiter, lineterminator="\r", fieldnames=pattern)
                write_file.writeheader()
                for item in result:
                    print(item)
                    write_file.writerow(item)
            return True
        else:
            return False

    def verificationNote(self, array, id):
        for item in array:
            if item[pattern[0]] == id:
                return True
        return False
    def delete(self, id):
        result = self.readCSVFile()
        if self.verificationNote(result, id):
            for item in range(0, len(result)-1):
                if result[item][pattern[0]] == id:
                    del result[item]
            with open(self.fileName, mode="w", encoding='utf-8') as w_file:
                write_file = csv.DictWriter(w_file, delimiter=delimiter, lineterminator="\r", fieldnames=pattern)
                write_file.writeheader()
                for item in result:
                    write_file.writerow(item)
            return True
        else:
            return False

    def readCSVFile(self):
        result = []
        with open(self.fileName, encoding='utf-8') as r_file:
            read_file = csv.DictReader(r_file, delimiter = delimiter)
            for row in read_file:
                result.append(row)
        return result