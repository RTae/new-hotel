from .model import TBL_Auth, TBL_Customers
from .helper import *
from .Customer import Customer
from sqlalchemy import func

session = initDatabase()

class Auth():
    def create(self, authID, customerID, password):
        auth = TBL_Auth(authID=authID, customerID=customerID, password=password)
        session.add(auth)
        session.commit()
        log = {
            "result":"",
            "msg":"",
            "status":"1"
        }
        return log

    def read(self, authID):
        auth = session.query(TBL_Auth)
        auth = auth.filter(TBL_Auth.authID==authID)
        if auth.scalar() is not None :
            auth = self.serialize(auth.one())
            log = {
                "result":auth,
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

    def update(self, authID, customerID, password):
        auth = session.query(TBL_Auth)
        auth = auth.filter(TBL_Auth.authID==authID)
        if auth.scalar() is not None :
            auth = auth.one()
            auth.customerID = customerID
            auth.password = password
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

    def delete(self, authID):
        auth = session.query(TBL_Auth)
        auth = auth.filter(TBL_Auth.authID==authID)
        if auth.scalar() is not None :
            session.delete(auth.one())
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
    
    def getAuthBycustomerID(self, customerID):
        auth = session.query(TBL_Auth)
        auth = auth.filter(TBL_Auth.customerID==customerID)
        if auth.scalar() is not None :
            auth = self.serialize(auth.one())
            log = {
                "result":auth,
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
    
    def login(self, email , password):
        C = Customer()
        result = C.getUserByEmail(email)
        if result['status'] == "1":
            customer = result['result']
            customerID = customer['customerID']
            result = self.getAuthBycustomerID(customerID)
            if result['status'] == "1":
                auth = result["result"]
                checkPassword = auth["password"]
                if password == checkPassword:
                    log = {
                        "result":auth["customerID"],
                        "msg":"",
                        "status":"1"
                    }
                    return log
                else:
                    log = {
                        "result":"",
                        "msg":"Passwrod is wrong",
                        "status":"100"
                    }
                    return log
            else:
                log = {
                    "result":"",
                    "msg":"User not found",
                    "status":"100"
                }
                return log
        else:
            log = {
                "result":"",
                "msg":"User not found",
                "status":"100"
            }
            return log
        
    def register(self, firstname, familyname, email, phoneNumber, creditCardNumber, point, password):
        C = Customer()
        result = C.getUserByEmail(email)
        if result['status'] != "1":
            maxCID = session.query(func.max(TBL_Customers.customerID)).one()
            maxAID = session.query(func.max(TBL_Auth.authID)).one()
            newCID = increaseID(maxCID[0], "c")
            newAID = increaseID(maxAID[0], "a")

            resultCus = C.create(newCID, firstname, familyname, email, phoneNumber, creditCardNumber, point)
            if resultCus["status"] == "1":
                resultAuth = self.create(newAID, newCID, password)
                if resultAuth["status"] == "1":
                    log = {
                        "result":newCID,
                        "msg":"",
                        "status":"1"
                    }
                    return log
                else :
                    log = {
                        "result":"",
                        "msg":"Can't create account (auth)",
                        "status":"100"
                    }
                    return log
            else :
                log = {
                    "result":"",
                    "msg":"Can't create account (customer)",
                    "status":"100"
                }
                return log
        else:
            log = {
                "result":"",
                "msg":"Email already exits",
                "status":"100"
            }
            return log
            

    def getAllAuth(self):
        auths = session.query(TBL_Auth).all()
        return [self.serialize(auth) for auth in auths]
    
    def serialize(self,auth):
        return {
            'authID': auth.authID,
            'customerID': auth.customerID,
            'password': auth.password,
        }
