class WriteToFile:
    # Here will be the instance stored.
    file = ""
    filePath = "C:/0A===/4. Testing and Software Improvement/PythonCustomer-master/PythonCustomer-master/resource/UserActions/"
    fileName = "inputLog.csv"

    def __init__(self,fileName):
        self.fileName = fileName


    def writeToFile(self,logItem):
        if self.file == "":
            self.file = open(self.filePath + self.fileName,"w")
        self.file.write(str(logItem) + "\n")
