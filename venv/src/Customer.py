from .model import *
from .helper import *

class Customer():
    def getAllCustomer(self):
        session = initDatabase()
        for customer in session.query(TBL_Customer).order_by(TBL_Customer.customerID):
            print(customer.customerID)
        return "Done"