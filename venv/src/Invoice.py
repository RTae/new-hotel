from .model import TBL_Invoices, TBL_InvoiceLineItem
from .helper import *
import datetime
from sqlalchemy import func

session = initDatabase()

class Invoice():
    def create(self, invoiceID, roomCatID, customerID, dateCreate, total, vat, checkIn, checkOut, numberOfRoom):
        
        # Convert datatype
        dateCreate = datetime.datetime.strptime(dateCreate, '%Y-%m-%d')
        checkIn = datetime.datetime.strptime(checkIn, '%Y-%m-%d')
        checkOut = datetime.datetime.strptime(checkOut, '%Y-%m-%d')
        periodOfStay = checkOut - checkIn
        total = float(total)
        vat = float(vat)
        amountDue = total + vat

        invoice = TBL_Invoices( invoiceID=invoiceID,
                                roomCatID=roomCatID,
                                customerID=customerID,
                                dateCreate=dateCreate.date(),
                                total=total,
                                vat=vat,
                                amountDue=amountDue,
                                periodOfStay=int(periodOfStay.days),
                                checkIn=checkIn.date(),
                                checkOut=checkOut.date(),
                                numberOfRoom=int(numberOfRoom)
                            )

        session.add(invoice)
        session.commit()
        log = {
            "result":"",
            "msg":"",
            "status":"1"
        }
        return log

    def read(self, invoiceID):
        invoice = session.query(TBL_Invoices)
        invoice = invoice.filter(TBL_Invoices.invoiceID==invoiceID)
        if invoice.scalar() is not None :
            invoice = self.serialize(invoice.one())
            log = {
                "result":invoice,
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

    def update(self, invoiceID, roomCatID, customerID, dateCreate, total, vat, checkIn, checkOut, numberOfRoom):
        invoice = session.query(TBL_Invoices)
        invoice = invoice.filter(TBL_Invoices.invoiceID==invoiceID)

        # Convert datatype
        dateCreate = datetime.datetime.strptime(dateCreate, '%Y-%m-%d')
        checkIn = datetime.datetime.strptime(checkIn, '%Y-%m-%d')
        checkOut = datetime.datetime.strptime(checkOut, '%Y-%m-%d')
        periodOfStay = checkOut - checkIn
        total = float(total)
        vat = float(vat)
        amountDue = total + vat

        if invoice.scalar() is not None :
            invoice = invoice.one()
            invoice.roomCatID = roomCatID
            invoice.customerID = customerID
            invoice.dateCreate = dateCreate.date()
            invoice.total = total
            invoice.vat = vat
            invoice.amountDue = amountDue
            invoice.periodOfStay = int(periodOfStay.days)
            invoice.checkIn = checkIn.date()
            invoice.checkOut = checkOut.date()
            invoice.numberOfRoom = int(numberOfRoom)
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

    def delete(self, invoiceID):
        invoice = session.query(TBL_Invoices)
        invoice = invoice.filter(TBL_Invoices.invoiceID==invoiceID)
        if invoice.scalar() is not None :
            session.delete(invoice.one())
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

    def getAllInvoice(self):
        invoices = session.query(TBL_Invoices).all()
        return [self.serialize(invoice) for invoice in invoices]


    def createInvoiceLine(self, invoiceID, roomID, remark):
        invoiceLine = TBL_InvoiceLineItem(invoiceID=invoiceID, roomID=roomID, remark=remark)
        session.add(invoiceLine)
        session.commit()
        log = {
            "result":"",
            "msg":"",
            "status":"1"
        }
        return log
    
    def readInvoiceLine(self, invoiceID, roomID):
        invoiceLine = session.query(TBL_InvoiceLineItem)
        invoiceLine = invoiceLine.filter(TBL_InvoiceLineItem.invoiceID==invoiceID, TBL_InvoiceLineItem.roomID==roomID)
        if invoiceLine.scalar() is not None :
            invoiceLine = self.serializeLine(invoiceLine.one())
            log = {
                "result":invoiceLine,
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

    def updateInvoiceLine(self, invoiceID, roomID, remark):
        invoiceLine = session.query(TBL_InvoiceLineItem)
        invoiceLine = invoiceLine.filter(TBL_InvoiceLineItem.invoiceID==invoiceID, TBL_InvoiceLineItem.roomID==roomID)

        if invoiceLine.scalar() is not None :
            invoiceLine = invoiceLine.one()
            invoiceLine.remark = remark
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

    def deleteInvoiceLine(self, invoiceID, roomID):
        invoiceLine = session.query(TBL_InvoiceLineItem)
        invoiceLine = invoiceLine.filter(TBL_InvoiceLineItem.invoiceID==invoiceID, TBL_InvoiceLineItem.roomID==roomID)
        if invoiceLine.scalar() is not None :
            session.delete(invoiceLine.one())
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
    
    def getAllInvoiceLine(self):
        invoiceLines = session.query(TBL_InvoiceLineItem).all()
        return [self.serializeLine(invoiceLine) for invoiceLine in invoiceLines]
    
    def createWithOutID(self, roomCatID, customerID, dateCreate, total, vat, checkIn, checkOut, numberOfRoom):
        maxIID = session.query(func.max(TBL_Invoices.invoiceID)).one()
        newIID = increaseID(maxIID[0], "i")
        log = self.create(newIID, roomCatID, customerID, dateCreate, total, vat, checkIn, checkOut, numberOfRoom)
        if (log["status"] == "1"):
            log = {
                "result":newIID,
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

    def readInvoiceLineByInvoiceID(self, invoiceID):
        invoiceLines = session.query(TBL_InvoiceLineItem)
        invoiceLines = invoiceLines.filter(TBL_InvoiceLineItem.invoiceID==invoiceID)
        invoiceLines = [self.serializeLine(invoiceLine) for invoiceLine in invoiceLines]
        log = {
            "result":invoiceLines,
            "msg":"",
            "status":"1"
        }
        return log

    def deleteInvoiceLineByInvoivceID(self, invoiceID):
        result = self.readInvoiceLineByInvoiceID(invoiceID)
        if len(result["result"]) != 0:
            delete_q = TBL_InvoiceLineItem.__table__.delete().where(TBL_InvoiceLineItem.invoiceID == invoiceID)
            session.execute(delete_q)
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

    def summaryInvoice(self):
        results = fetch('   SELECT  i."invoiceID", i."dateCreate", i."total", i."vat",                      \
		                            i."amountDue", i."periodOfStay", i."checkIn", i."checkOut",             \
		                            i."numberOfRoom", CONCAT(c."firstname",'+ "' '" +',c."familyname") as "name",   \
                                    rc.name                                                                 \
                            FROM "TBL_Invoices" i                                                           \
                            INNER JOIN "TBL_RoomCategorys" rc                                               \
                                ON i."roomCatID" = rc."roomCatID"                                           \
                            INNER JOIN "TBL_Customer" c                                                     \
                                ON i."customerID" =  c."customerID"' )
        invoices = []
        for result in results:
            tempDict = {}
            temp = cursortorow(result)
            tempDict ={
                "receiptID": temp[0],
                "name": temp[1],
                "dateCreate": temp[2],
                "paymentName": temp[3],
                "totalReceived": temp[4],
                "paymentRef": temp[5],
                "remark": temp[6],
            }
            invoices.append(tempDict)

        log = {
            "result":invoices,
            "msg":"",
            "status":"1"
        }
        return log

    def serialize(self,invoice):
        return {
            'roomCatID': invoice.roomCatID,
            'customerID': invoice.customerID,
            'dateCreate': str(invoice.dateCreate),
            'total': str(invoice.total),
            'vat': str(invoice.vat),
            'amountDue': str(invoice.amountDue),
            'periodOfStay': str(invoice.periodOfStay),
            'checkIn': str(invoice.checkIn),
            'checkOut': str(invoice.checkOut),
            'numberOfRoom': str(invoice.numberOfRoom),
        }

    def serializeLine(self,invoice):
        return {
            'invoiceID': invoice.invoiceID,
            'roomID': invoice.roomID,
            'remark': str(invoice.remark)
        }