from .model import *
from .helper import *

class Customer():
    def getAllCustomer(self):
        session = initDatabase()
        customers = session.query(TBL_Customer).all()
        return [self.serialize(customer) for customer in customers]
    
    def serialize(self,customer):
        return {
            'customerID': customer.customerID,
            'firstname': customer.firstname,
            'email': customer.email,
            'phoneNumber': customer.phoneNumber,
            'creditCardNumber': customer.creditCardNumber,
            'point': customer.point
        }