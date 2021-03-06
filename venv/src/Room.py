from .model import TBL_Rooms, TBL_RoomCategorys
from .helper import *
from sqlalchemy import func

session = initDatabase()

class Room():
    def create(self, roomID, roomCatID, status, cleanStatus):
        room = TBL_Rooms(roomID=roomID, roomCatID=roomCatID, status=(status=="1"), cleanStatus=(cleanStatus=="1"))
        session.add(room)
        session.commit()
        log = {
            "result":"",
            "msg":"",
            "status":"1"
        }
        return log

    def read(self, roomID):
        room = session.query(TBL_Rooms)
        room = room.filter(TBL_Rooms.roomID==roomID)
        if room.scalar() is not None :
            room = self.serialize(room.one())
            log = {
                "result":room,
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

    def update(self, roomID, roomCatID, status, cleanStatus):
        room = session.query(TBL_Rooms)
        room = room.filter(TBL_Rooms.roomID==roomID)
        if room.scalar() is not None :
            room = room.one()
            room.roomCatID = roomCatID
            room.status = status=="1"
            room.cleanStatus = cleanStatus=="1"
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

    def delete(self, roomID):
        room = session.query(TBL_Rooms)
        room = room.filter(TBL_Rooms.roomID==roomID)
        if room.scalar() is not None :
            session.delete(room.one())
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

    def getAllRoom(self):
        rooms = session.query(TBL_Rooms).all()
        return [self.serialize(room) for room in rooms]
    

    def createRoomCat(self, roomCatID, name, bedType, numberBed, guestRoom, fare):
        roomCat = TBL_RoomCategorys(roomCatID=roomCatID, name=name, bedType=bedType, numberBed=int(numberBed), guestRoom=(guestRoom=="1"), fare=float(fare))
        session.add(roomCat)
        session.commit()
        log = {
            "result":"",
            "msg":"",
            "status":"1"
        }
        return log

    def readRoomCat(self, roomCatID):
        roomCat = session.query(TBL_RoomCategorys)
        roomCat = roomCat.filter(TBL_RoomCategorys.roomCatID==roomCatID)
        if roomCat.scalar() is not None :
            roomCat = self.serializeRoomCat(roomCat.one())
            log = {
                "result":roomCat,
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

    def updateRoomCat(self, roomCatID, name, bedType, numberBed, guestRoom, fare):
        roomCat = session.query(TBL_RoomCategorys)
        roomCat = roomCat.filter(TBL_RoomCategorys.roomCatID==roomCatID)
        if roomCat.scalar() is not None :
            roomCat = roomCat.one()
            roomCat.name = name
            roomCat.bedType = bedType
            roomCat.numberBed = int(numberBed)
            roomCat.guestRoom = guestRoom=="1"
            roomCat.fare = float(fare)

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

    def deleteRoomCat(self, roomCatID):
        roomCat = session.query(TBL_RoomCategorys)
        roomCat = roomCat.filter(TBL_RoomCategorys.roomCatID==roomCatID)
        if roomCat.scalar() is not None :
            session.delete(roomCat.one())
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

    def getAllRoomCat(self):
        roomCats = session.query(TBL_RoomCategorys).all()
        return [self.serializeRoomCat(roomCat) for roomCat in roomCats]

    def getRoomFreeByRoomCat(self, roomCatID, limit=None):
        if limit != None:
            rooms = session.query(TBL_Rooms).filter(TBL_Rooms.roomCatID==roomCatID, TBL_Rooms.status==(1==1)).order_by(func.random()).limit(int(limit)).all()
            rooms = [self.serialize(room) for room in rooms]
            return rooms
        else:
            rooms = session.query(TBL_Rooms).filter(TBL_Rooms.roomCatID==roomCatID, TBL_Rooms.status==(1==1)).order_by(func.random()).all()
            rooms = [self.serialize(room) for room in rooms]
            return rooms
    
    def roomSummaryByRoomCat(self):
        results = fetch('   SELECT rc."name", COUNT(*)              \
                            FROM "TBL_Rooms" r                      \
                            INNER JOIN "TBL_RoomCategorys" rc       \
	                            ON r."roomCatID" = rc."roomCatID"   \
                            WHERE "status" = TRUE                   \
                            GROUP BY rc."name"')
        rooms = []
        for result in results:
            tempDict = {}
            temp = cursortorow(result)
            tempDict ={
                "name": temp[0],
                "count": temp[1],
            }
            rooms.append(tempDict)
        
        log = {
            "result":rooms,
            "msg":"",
            "status":"1"
        }
        return log
    
    def roomSummary(self):
        results = fetch('   SELECT  r."roomID", rc."name", rc."bedType",            \
		                            rc."numberBed", rc."guestRoom", rc."fare",      \
		                            r."status", r."cleanStatus"                     \
                            FROM "TBL_Rooms" r                                      \
                            INNER JOIN "TBL_RoomCategorys" rc                       \
	                        ON r."roomCatID" = rc."roomCatID"')
        rooms = []
        for result in results:
            tempDict = {}
            temp = cursortorow(result)
            tempDict ={
                "roomID": temp[0],
                "roomType": temp[1],
                "bedType": temp[2],
                "numberBed": temp[3],
                "guestRoom": temp[4],
                "fare": temp[5],
                "status": temp[6],
                "cleanStatus": temp[7],
            }
            rooms.append(tempDict)
        
        log = {
            "result":rooms,
            "msg":"",
            "status":"1"
        }
        return log 
    
    def createWithOutID(self, roomCatID, status, cleanStatus):
        maxRID = session.query(func.max(TBL_Rooms.roomID)).one()
        newRID = increaseID(maxRID[0], "r")
        log = self.create(newRID, roomCatID, status, cleanStatus)
        if (log["status"] == "1"):
            log = {
                "result":newRID,
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

    def serialize(self,room):
        return {
            'roomID': room.roomID,
            'roomCatID': room.roomCatID,
            'status': room.status,
            'cleanStatus': room.cleanStatus,
        }

    def serializeRoomCat(self,roomCat):
        return {
            'roomCatID': roomCat.roomCatID,
            'name': roomCat.name,
            'bedType': roomCat.bedType,
            'numberBed': roomCat.numberBed,
            'guestRoom': roomCat.guestRoom,
            'fare': roomCat.fare,
        }
