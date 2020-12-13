from .model import TBL_Invoices
from .helper import *
import datetime

session = initDatabase()

class Invoice():
    def create(self, invoiceID, roomCatID, customerID, dateCreate, total, vat, amountDue, checkIn, checkOut, numberOfRoom):
        
        # Convert datatype
        dateCreate = datetime.datetime.strptime(dateCreate, '%Y-%m-%d')
        checkIn = datetime.datetime.strptime(checkIn, '%Y-%m-%d')
        checkOut = datetime.datetime.strptime(checkOut, '%Y-%m-%d')
        periodOfStay = checkOut - checkIn
        print('Date Create:', dateCreate.date())
        print('Date checkIn:', checkIn.date())
        print('Date checkOut:', checkOut.date())
        print('Delta:', int(periodOfStay.days))

        invoice = TBL_Invoices(invoiceID=invoiceID, roomCatID=roomCatID, customerID=customerID, dateCreate=dateCreate.date(), total=float(total), vat=float(vat), amountDue=float(amountDue), periodOfStay=int(periodOfStay.days), checkIn=checkIn.date(), checkOut=checkOut.date(), numberOfRoom=int(numberOfRoom))
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
                "msg":"User not found",
                "status":"100"
            }
            return log

    def update(self, invoiceID, roomCatID, customerID, dateCreate, total, vat, amountDue, checkIn, checkOut, numberOfRoom):
        invoice = session.query(TBL_Invoices)
        invoice = invoice.filter(TBL_Invoices.invoiceID==invoiceID)

        # Convert datatype
        dateCreate = datetime.datetime.strptime(dateCreate, '%Y-%m-%d')
        checkIn = datetime.datetime.strptime(checkIn, '%Y-%m-%d')
        checkOut = datetime.datetime.strptime(checkOut, '%Y-%m-%d')
        periodOfStay = checkOut - checkIn
        print('Date Create:', dateCreate.date())
        print('Date checkIn:', checkIn.date())
        print('Date checkOut:', checkOut.date())
        print('Delta:', int(periodOfStay.days))

        if invoice.scalar() is not None :
            invoice = invoice.one()
            invoice.roomCatID = roomCatID
            invoice.customerID = customerID
            invoice.dateCreate = dateCreate.date()
            invoice.total = float(total)
            invoice.vat = float(vat)
            invoice.amountDue = float(amountDue)
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
                "msg":"User not found",
                "status":"100"
            }
            return log

    def delete(self, customerID):
        invoice = session.query(TBL_Invoices)
        invoice = invoice.filter(TBL_Invoices.invoiceID==invoiceID)
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

    def getAllInvoice(self):
        invoices = session.query(TBL_Invoices).all()
        return [self.serialize(invoice) for invoice in invoices]
    

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