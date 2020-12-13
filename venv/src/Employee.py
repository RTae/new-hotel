from .model import TBL_Employees, TBL_EmployeeTypes
from .helper import *
import datetime
from sqlalchemy import func

session = initDatabase()

class Employee():
    def create(self, employeeID, employeeTypeID, firstname, familyname, email, phoneNumber, accepteDate):
        accepteDate = datetime.datetime.strptime(accepteDate, '%Y-%m-%d')
        employee = TBL_Employees(employeeID=employeeID, employeeTypeID=employeeTypeID, firstname=firstname, familyname=familyname, email=email, phoneNumber=phoneNumber, accepteDate=accepteDate.date())
        session.add(employee)
        session.commit()
        log = {
            "result":"",
            "msg":"",
            "status":"1"
        }
        return log

    def read(self, employeeID):
        employee = session.query(TBL_Employees)
        employee = employee.filter(TBL_Employees.employeeID==employeeID)
        if employee.scalar() is not None :
            employee = self.serialize(employee.one())
            log = {
                "result":employee,
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

    def update(self, employeeID, employeeTypeID, firstname, familyname, email, phoneNumber, accepteDate):
        accepteDate = datetime.datetime.strptime(accepteDate, '%Y-%m-%d')
        employee = session.query(TBL_Employees)
        employee = employee.filter(TBL_Employees.employeeID==employeeID)
        if employee.scalar() is not None :
            employee = employee.one()
            employee.employeeTypeID = employeeTypeID
            employee.firstname = firstname
            employee.familyname = familyname
            employee.email = email
            employee.phoneNumber = phoneNumber
            employee.accepteDate = accepteDate.date()
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

    def delete(self, employeeID):
        employee = session.query(TBL_Employees)
        employee = employee.filter(TBL_Employees.employeeID==employeeID)
        if employee.scalar() is not None :
            session.delete(employee.one())
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

    def getAllEmployee(self):
        employees = session.query(TBL_Employees).all()
        return [self.serialize(employee) for employee in employees]

    def createWithOutID(self, employeeTypeID, firstname, familyname, email, phoneNumber, accepteDate):
        maxEID = session.query(func.max(TBL_Employees.employeeID)).one()
        newEID = increaseID(maxEID[0], "e")
        log = self.create(newEID, employeeTypeID, firstname, familyname, email, phoneNumber, accepteDate)
        if (log["status"] == "1"):
            log = {
                "result":newEID,
                "msg":"",
                "status":"1"
            }
            return log
        else:
            log = {
                "result":"",
                "msg":"Error",
                "status":"100"
            }
            return log

    def createEmployeeType(self, employeeTypeID, name, salary):
        employeeType = TBL_EmployeeTypes(employeeTypeID=employeeTypeID, name=name, salary=salary)
        session.add(employeeType)
        session.commit()
        log = {
            "result":"",
            "msg":"",
            "status":"1"
        }
        return log

    def readEmployeeType(self, employeeTypeID):
        employeeType = session.query(TBL_EmployeeTypes)
        employeeType = employeeType.filter(TBL_EmployeeTypes.employeeTypeID==employeeTypeID)
        if employeeType.scalar() is not None :
            employeeType = self.serializeEmployeeType(employeeType.one())
            log = {
                "result":employeeType,
                "msg":"",
                "status":"1"
            }
            return log
        else:
            log = {
                "result":"",
                "msg":"Not found",
                "status":"100"
            }
            return log

    def updateEmployeeType(self, employeeTypeID, name, salary):
        employeeType = session.query(TBL_EmployeeTypes)
        employeeType = employeeType.filter(TBL_EmployeeTypes.employeeTypeID==employeeTypeID)
        if employeeType.scalar() is not None :
            employeeType = employeeType.one()
            employeeType.name = name
            employeeType.salary = salary
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
                "msg":"Not found",
                "status":"100"
            }
            return log

    def deleteEmployeeType(self, employeeTypeID):
        employeeType = session.query(TBL_EmployeeTypes)
        employeeType = employeeType.filter(TBL_EmployeeTypes.employeeTypeID==employeeTypeID)
        if employeeType.scalar() is not None :
            session.delete(employeeType.one())
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
                "msg":"Not found",
                "status":"100"
            }
            return log

    def getAllEmployeeType(self):
        employeeTypes = session.query(TBL_EmployeeTypes).all()
        return [self.serializeEmployeeType(employeeType) for employeeType in employeeTypes]

    def serialize(self, employee):
        return {
            'employeeID': employee.employeeID,
            'employeeTypeID': employee.employeeTypeID,
            'firstname': employee.firstname,
            'familyname': employee.familyname,
            'email': employee.email,
            'phoneNumber': employee.phoneNumber,
            'accepteDate': employee.accepteDate
        }
    
    def serializeEmployeeType(self, employeeType):
        return {
            'employeeTypeID': employeeType.employeeTypeID,
            'name': employeeType.name,
            'salary': employeeType.salary,
        }