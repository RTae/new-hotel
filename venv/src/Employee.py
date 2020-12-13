from .model import TBL_Employees
from .helper import *

session = initDatabase()

class Employee():
    def create(self, customerID, firstname, familyname, email, phoneNumber, creditCardNumber, point):
        customer = TBL_Customers(customerID=customerID, firstname=firstname, email=email, familyname=familyname, phoneNumber=phoneNumber, creditCardNumber=creditCardNumber, point=int(point))
        session.add(customer)
        session.commit()
        log = {
            "result":"",
            "msg":"",
            "status":"1"
        }
        return log

    def read(self, customerID):
        customer = session.query(TBL_Customers)
        customer = customer.filter(TBL_Customers.customerID==customerID)
        if customer.scalar() is not None :
            customer = self.serialize(customer.one())
            log = {
                "result":customer,
                "msg":"",
                "status":"1"
            }
            return log
        else:
            log = {
                "result":"",
                "msg":"User not found",
                "status":"100"
            }
            return log

    def update(self, customerID, firstname, familyname, email, phoneNumber, creditCardNumber, point):
        customer = session.query(TBL_Customers)
        customer = customer.filter(TBL_Customers.customerID==customerID)
        if customer.scalar() is not None :
            customer = customer.one()
            customer.firstname = firstname
            customer.familyname = familyname
            customer.email = email
            customer.phoneNumber = phoneNumber
            customer.creditCardNumber = creditCardNumber
            customer.firstname = firstname
            customer.point = int(point)
            session.commit()
            log = {
                "result":"",
                "msg":"",
                "status":"1"
            }
            return log
        else:
            log = {
                "result":"",
                "msg":"User not found",
                "status":"100"
            }
            return log

    def delete(self, customerID):
        customer = session.query(TBL_Customers)
        customer = customer.filter(TBL_Customers.customerID==customerID)
        if customer.scalar() is not None :
            session.delete(customer.one())
            session.commit()
            log = {
                "result":"",
                "msg":"",
                "status":"1"
            }
            return log
        else:
            log = {
                "result":"",
                "msg":"User not found",
                "status":"100"
            }
            return log

    def getAllCustomer(self):
        customers = session.query(TBL_Customers).all()
        return [self.serialize(customer) for customer in customers]
    
    def getUserByEmail(self, email):
        customer = session.query(TBL_Customers)
        customer = customer.filter(TBL_Customers.email==email)
        if customer.scalar() is not None :
            customer = self.serialize(customer.one())
            log = {
                "result":customer,
                "msg":"",
                "status":"1"
            }
            return log
        else:
            log = {
                "result":"",
                "msg":"User not found",
                "status":"100"
            }
            return log
    
    def serialize(self,customer):
        return {
            'customerID': customer.customerID,
            'firstname': customer.firstname,
            'familyname': customer.familyname,
            'email': customer.email,
            'phoneNumber': customer.phoneNumber,
            'creditCardNumber': customer.creditCardNumber,
            'point': customer.point
        }