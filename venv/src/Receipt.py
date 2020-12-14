from .model import TBL_Receipts, TBL_ReceiptsLineItem
from .helper import *
import datetime
from sqlalchemy import func

session = initDatabase()

class Receipt():
    def create(self, receiptID, customerID, paymentMedId, cuponID, dateCreate, paymentRef, totalReceived, remark):
        
        # Convert datatype
        dateCreate = datetime.datetime.strptime(dateCreate, '%Y-%m-%d')
        totalReceived = float(totalReceived)

        receipt = TBL_Receipts( receiptID=receiptID,
                                customerID=customerID,
                                paymentMedId=paymentMedId,
                                cuponID=cuponID,
                                dateCreate=dateCreate.date(),
                                paymentRef=paymentRef,
                                totalReceived=totalReceived,
                                remark=remark
                            )

        session.add(receipt)
        session.commit()
        log = {
            "result":"",
            "msg":"",
            "status":"1"
        }
        return log

    def read(self, receiptID):
        receipt = session.query(TBL_Receipts)
        receipt = receipt.filter(TBL_Receipts.receiptID==receiptID)
        if receipt.scalar() is not None :
            receipt = self.serialize(receipt.one())
            log = {
                "result":receipt,
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

    def update(self, receiptID, customerID, paymentMedId, cuponID, dateCreate, paymentRef, totalReceived, remark):
        receipt = session.query(TBL_Receipts)
        receipt = receipt.filter(TBL_Receipts.receiptID==receiptID)

        # Convert datatype
        dateCreate = datetime.datetime.strptime(dateCreate, '%Y-%m-%d')
        totalReceived = float(totalReceived)

        if receipt.scalar() is not None :
            receipt = receipt.one()
            receipt.customerID = customerID
            receipt.paymentMedId = paymentMedId
            receipt.cuponID = cuponID
            receipt.dateCreate = dateCreate.date()
            receipt.paymentRef = paymentRef
            receipt.totalReceived = totalReceived
            receipt.remark = remark
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

    def delete(self, receiptID):
        receipt = session.query(TBL_Receipts)
        receipt = receipt.filter(TBL_Receipts.receiptID==receiptID)
        if receipt.scalar() is not None :
            session.delete(receipt.one())
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

    def getAllReceipt(self):
        receipts = session.query(TBL_Receipts).all()
        return [self.serialize(receipt) for receipt in receipts]


    def createReceiptLine(self, receiptID, invoiceID, remark):
        receiptLine = TBL_ReceiptsLineItem(receiptID=receiptID, invoiceID=invoiceID, remark=remark)
        session.add(receiptLine)
        session.commit()
        log = {
            "result":"",
            "msg":"",
            "status":"1"
        }
        return log
    
    def readReceiptLine(self, receiptID, invoiceID):
        receiptLine = session.query(TBL_ReceiptsLineItem)
        receiptLine = receiptLine.filter(TBL_ReceiptsLineItem.receiptID==receiptID, TBL_ReceiptsLineItem.invoiceID==invoiceID)
        if receiptLine.scalar() is not None :
            receiptLine = self.serializeLine(receiptLine.one())
            log = {
                "result":receiptLine,
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

    def updateReceiptLine(self, receiptID, invoiceID, remark):
        receiptLine = session.query(TBL_ReceiptsLineItem)
        receiptLine = receiptLine.filter(TBL_ReceiptsLineItem.receiptID==receiptID, TBL_ReceiptsLineItem.invoiceID==invoiceID)

        if receiptLine.scalar() is not None :
            receiptLine = receiptLine.one()
            receiptLine.remark = remark
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

    def deleteReceiptLine(self, receiptID, invoiceID):
        receiptLine = session.query(TBL_ReceiptsLineItem)
        receiptLine = receiptLine.filter(TBL_ReceiptsLineItem.receiptID==receiptID, TBL_ReceiptsLineItem.invoiceID==invoiceID)
        if receiptLine.scalar() is not None :
            session.delete(receiptLine.one())
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
    
    def getAllReceiptLine(self):
        receiptLines = session.query(TBL_ReceiptsLineItem).all()
        return [self.serializeLine(receiptLine) for receiptLine in receiptLines]
    
    def createWithOutID(self, customerID, paymentMedId, cuponID, dateCreate, paymentRef, totalReceived, remark):
        maxRID = session.query(func.max(TBL_Receipts.receiptID)).one()
        newRID = increaseID(maxRID[0], "re")
        log = self.create(newRID, customerID, paymentMedId, cuponID, dateCreate, paymentRef, totalReceived, remark)

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

    def readReceiptLineByReceiptID(self, receiptID):
        receiptLines = session.query(TBL_ReceiptsLineItem)
        receiptLines = receiptLines.filter(TBL_ReceiptsLineItem.receiptID==receiptID)
        receiptLines = [self.serializeLine(receiptLine) for receiptLine in receiptLines]
        log = {
            "result":receiptLines,
            "msg":"",
            "status":"1"
        }
        return log

    def showReceiptReportByReceiptID(self, receiptID):
        receipt = []
        receiptID = "'"+receiptID+"'"
        results = fetch('   SELECT  r."receiptID", r."dateCreate", r."totalReceived",    \
		                            r."remark", r."paymentRef", c."firstname",           \
		                            c."familyname", c."email", c."phoneNumber"           \
                            FROM "TBL_Receipts" r                                        \
                            INNER JOIN "TBL_Customer" c                                  \
                                ON r."customerID" = c."customerID"                       \
                            WHERE r."receiptID" = {}'.format(receiptID))
        for result in results:
            tempDict = {}
            temp = cursortorow(result)
            tempDict = {
                "receiptID": temp[0],
                "dateCreate": temp[1],
                "totalReceived": temp[2],
                "remark": temp[3],
                "paymentRef": temp[4],
                "firstname": temp[5],
                "familyname": temp[6],
                "email": temp[7],
                "phoneNumber": temp[8],
            }
            receipt.append(tempDict)
        log = {
            "result":receipt,
            "msg":"",
            "status":"1"
        }
        return log
    
    def showReceiptReportByReceiptIDLine(self, receiptID):
        receiptID = "'"+receiptID+"'"
        results = fetch('   SELECT re."receiptID", rc."name", rc."fare", i."checkIn",  \
		                        i."checkOut", i."numberOfRoom", i."periodOfStay",   \
		                        i."amountDue"                                       \
                            FROM "TBL_ReceiptsLineItem" re                      \
                            INNER JOIN "TBL_Invoices" i                         \
                                ON re."invoiceID" = i."invoiceID"               \
                            INNER JOIN "TBL_Customer" c                         \
                                ON i."customerID" = c."customerID"              \
                            INNER JOIN "TBL_RoomCategorys" rc                   \
                                ON i."roomCatID" = rc."roomCatID"               \
                            WHERE re."receiptID" = {}'.format(receiptID))
        receipt = []
        for result in results:
            tempDict = {}
            temp = cursortorow(result)
            tempDict ={
                "receiptID": temp[0],
                "roomType": temp[1],
                "fare": temp[2],
                "checkIn": temp[3],
                "checkOut": temp[4],
                "numberOfRoom": temp[5],
                "periodOfStay": temp[6],
                "amountDue": temp[7],
            }
            receipt.append(tempDict)
        
        log = {
            "result":receipt,
            "msg":"",
            "status":"1"
        }
        return log

    def serialize(self,receipt):
        return {
            'receiptID': receipt.receiptID,
            'customerID': receipt.customerID,
            'paymentMedId': receipt.paymentMedId,
            'cuponID': receipt.cuponID,
            'dateCreate': str(receipt.dateCreate),
            'paymentRef': receipt.paymentRef,
            'totalReceived': str(receipt.totalReceived),
            'remark': receipt.remark,
        }

    def serializeLine(self,receiptLine):
        return {
            'receiptID': receiptLine.receiptID,
            'invoiceID': receiptLine.invoiceID,
            'remark': str(receiptLine.remark)
        }