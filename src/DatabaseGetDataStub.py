from DataSourceInterface import DataSourceInterface

class DatabaseGetDataStub(DataSourceInterface):

    def getData(self,tableName,fieldNames):
        return ["test_table", "test_field"]

