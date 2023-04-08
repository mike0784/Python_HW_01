from workingWithFile import fileCSV
from pattern import *
from view import *
class menu(fileCSV):
    def __init__(self, fileName):
        super().__init__(fileName)
    def run(self):
        com = ""
        while com != "EXIT":
            enter = input("Enter action: ").upper().split(" ")
            if enter[0] == "ADD" or enter[0] == "INSERT":
                self.add()
            elif enter[0] == "DELETE" or enter[0] == "DEL":
                self.deleteFile(enter)
            elif enter[0] == "UPDATE":
                self.updateFile(enter)
            elif enter[0] == "READ":
                self.readFile(enter)
            elif enter[0] == "READALL":
                self.readAllFile(enter)
            elif enter[0] == "EXIT":
                com = "EXIT"
            else:
                print("The entered action does not exist")
            print("==============================================================================================")

    def add(self):
        headerNote = input("Enter the title of the note: ")
        note = input("Enter the text of the note: ")
        self.insert(headerNote, note)

    def deleteFile(self, command):
        if len(command) == 1:
            id = input("Enter the ID of the record to delete: ")
        else:
            id = command[1]
        if self.delete(id):
            print("The record was successfully deleted")
        else:
            print(f"The entry in the entered id={id} does not exist")

    def updateFile(self, command):
        if len(command) == 1:
            id = input("Enter the entry number: ")
        else:
            id = command[1]
        headerNote = input("Enter the title of the note: ")
        note = input("Enter the text of the note: ")
        if self.update(id, headerNote, note):
            print("The record update was successful")
        else:
            print(f"The entry in the entered id={id} does not exist")

    def readAllFile(self, command):
        result = self.readAll()
        if len(command) > 1:
            if command[1] == "-D" or command[1] == "DATE":
                if command[2] == ">" or command[2] == "UP":
                    temp = {}
                    for i in range(0, len(result)):
                        for j in range(0, len(result)-1-i):
                            if result[j][pattern[3]] > result[j+1][pattern[3]]:
                                temp = result[j]
                                result[j] = result[j+1]
                                result[j+1] = temp
                if command[2] == "<" or command[2] == "DOWN":
                    temp = {}
                    for i in range(0, len(result)):
                        for j in range(0, len(result)-1-i):
                            if result[j][pattern[3]] < result[j+1][pattern[3]]:
                                temp = result[j+1]
                                result[j+1] = result[j]
                                result[j] = temp
        for item in result:
            viewNote(item)

    def readFile(self, command):
        if len(command) == 1:
            id = input("Enter the entry number: ")
        else:
            id = command[1]
        result = self.read(id)
        if result != 0:
            viewNote(result)
        else:
            print(f"The entry in the entered id={id} does not exist")