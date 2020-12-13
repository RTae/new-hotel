from .model import TBL_CleaningRoomLineItem
from .helper import *
import datetime
from sqlalchemy import func

session = initDatabase()

class Cleaning():
    def create(self, employeeID, roomID, startDateTime, endDateTime):
        startDateTime = datetime.datetime.strptime(startDateTime, '%Y-%m-%d %H:%M')
        endDateTime = datetime.datetime.strptime(endDateTime, '%Y-%m-%d %H:%M')
        cleaning = TBL_CleaningRoomLineItem(employeeID=employeeID, roomID=roomID, startDateTime=startDateTime, endDateTime=endDateTime)
        session.add(cleaning)
        session.commit()
        log = {
            "result":"",
            "msg":"",
            "status":"1"
        }
        return log

    def read(self, employeeID, roomID):
        cleaning = session.query(TBL_CleaningRoomLineItem)
        cleaning = cleaning.filter(TBL_CleaningRoomLineItem.employeeID==employeeID, TBL_CleaningRoomLineItem.roomID==roomID)
        if cleaning.scalar() is not None :
            cleaning = self.serialize(cleaning.one())
            log = {
                "result":cleaning,
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

    def update(self, employeeID, roomID, startDateTime, endDateTime):
        startDateTime = datetime.datetime.strptime(startDateTime, '%Y-%m-%d %H:%M')
        endDateTime = datetime.datetime.strptime(endDateTime, '%Y-%m-%d %H:%M')
        cleaning = session.query(TBL_CleaningRoomLineItem)
        cleaning = cleaning.filter(TBL_CleaningRoomLineItem.employeeID==employeeID, TBL_CleaningRoomLineItem.roomID==roomID)
        if cleaning.scalar() is not None :
            cleaning = cleaning.one()
            cleaning.startDateTime = startDateTime
            cleaning.endDateTime = endDateTime
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

    def delete(self, employeeID, roomID):
        cleaning = session.query(TBL_CleaningRoomLineItem)
        cleaning = cleaning.filter(TBL_CleaningRoomLineItem.employeeID==employeeID, TBL_CleaningRoomLineItem.roomID==roomID)
        if cleaning.scalar() is not None :
            session.delete(cleaning.one())
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

    def getAllCleaning(self):
        cleanings = session.query(TBL_CleaningRoomLineItem).all()
        return [self.serialize(cleaning) for cleaning in cleanings]

    def getCleaningByEmployeeID(self, employeeID):
        cleanings = session.query(TBL_CleaningRoomLineItem)
        cleanings = cleanings.filter(TBL_CleaningRoomLineItem.employeeID==employeeID)
        cleanings = [self.serialize(cleaning) for cleaning in cleanings]
        log = {
            "result":cleanings,
            "msg":"",
            "status":"1"
        }
        return log
    
    def getCleaningByRoomID(self, roomID):
        cleanings = session.query(TBL_CleaningRoomLineItem)
        cleanings = cleanings.filter(TBL_CleaningRoomLineItem.roomID==roomID)
        cleanings = [self.serialize(cleaning) for cleaning in cleanings]
        log = {
            "result":cleanings,
            "msg":"",
            "status":"1"
        }
        return log

    def serialize(self, cleaning):
        return {
            'employeeID': cleaning.employeeID,
            'roomID': cleaning.roomID,
            'startDateTime': cleaning.startDateTime,
            'endDateTIme': cleaning.endDateTime,
        }
    