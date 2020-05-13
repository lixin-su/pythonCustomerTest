import csv
class ReadCSVFile :

    filePathPrefix = "C:/0A===/4. Testing and Software Improvement/PythonCustomer-master/PythonCustomer-master/resource/"

    def getFileData(self, directory,  fileName):
        fileData = []
        with open(self.filePathPrefix+ directory + fileName,'rt')as dataFile:
            fileReader = csv.reader(dataFile)
            for row in fileReader:
                fileData.append(row)
        return fileData

