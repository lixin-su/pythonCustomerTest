from DataSourceInterface import DataSourceInterface

class DatabaseGetDataFake(DataSourceInterface):

    def getData(self,tableName,fieldNames):
        if tableName == "test_table":
            fieldNames = ['emailAddress', 'firstName', 'lastName', 'password']

        return fieldNames
