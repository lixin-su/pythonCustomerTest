import unittest
from DatabaseGetDataStub import DatabaseGetDataStub
from DatabaseGetDataFake import DatabaseGetDataFake
from DatabaseGetData import DatabaseGetData
from unittest.mock import MagicMock
from CustomerDatabaseMapping import CustomerDatabaseMapping


class CustomerTests(unittest.TestCase):

    customer = CustomerDatabaseMapping()

    # Mock test
    def test_getCustomerDataMock(self):
        self.customer.getCustomerData = MagicMock(return_value=["test_table", "test_field"])
        request = self.customer.getCustomerData()
        self.assertEqual(request,["test_table", "test_field"])


    # Stub test
    def test_getCustomerDataStub(self):
        self.customer.dataSource = DatabaseGetDataStub()
        name = self.customer.getCustomerData()
        self.assertEqual(name, ["test_table", "test_field"])

    # Fake test
    def test_getCustomerDataFake(self):
        self.customer.dataSource = DatabaseGetDataFake()
        customerData = self.customer.getCustomerData()
        self.assertEqual(customerData,['emailAddress', 'firstName', 'lastName', 'password'])



def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()