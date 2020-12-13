import sqlalchemy as sa
from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TBL_Customers(Base):
    __tablename__ = 'TBL_Customer'
    customerID = Column('customerID', sa.String(6) ,primary_key=True)
    firstname = Column('firstname', sa.String(20) )
    familyname = Column('familyname', sa.String(20) )
    email = Column('email', sa.String(50) )
    phoneNumber = Column('phoneNumber', sa.String(10) )
    creditCardNumber = Column('creditCardNumber', sa.String(16) )
    point = Column('point', sa.Integer )

class TBL_Auth(Base):
    __tablename__ = 'TBL_Auth'
    authID = Column('authID', sa.String(6), primary_key=True)
    customerID = Column('customerID', ForeignKey('TBL_Customer.customerID'))
    password = Column('password', sa.String(20) )

class TBL_Rooms(Base):
    __tablename__ = 'TBL_Rooms'
    roomID = Column('roomID', sa.String(6), primary_key=True)
    roomCatID = Column('roomCatID', ForeignKey('TBL_RoomCategorys.roomCatID'))
    status = Column('status', sa.Boolean)
    cleanStatus = Column('cleanStatus', sa.Boolean)

class TBL_RoomCategorys(Base):
    __tablename__ = 'TBL_RoomCategorys'
    roomCatID = Column('roomCatID', sa.String(6), primary_key=True)
    name = Column('name', sa.String(20))
    bedType = Column('bedType', sa.String(20))
    numberBed = Column('numberBed', sa.Integer)
    guestRoom = Column('guestRoom', sa.Boolean)
    fare = Column('fare', sa.Float(precision=2))

class TBL_Invoices(Base):
    __tablename__ = 'TBL_Invoices'
    invoiceID = Column('invoiceID', sa.String(6), primary_key=True)
    roomCatID = Column('roomCatID', ForeignKey('TBL_RoomCategorys.roomCatID'))
    customerID = Column('customerID', ForeignKey('TBL_Customer.customerID'))
    dateCreate = Column('dateCreate', sa.Date)
    total = Column('total', sa.Float(precision=2))
    vat = Column('vat', sa.Float(precision=2))
    amountDue = Column('amountDue', sa.Float(precision=2))
    periodOfStay = Column('periodOfStay', sa.Integer)
    checkIn = Column('checkIn', sa.Date)
    checkOut = Column('checkOut', sa.Date)
    numberOfRoom = Column('numberOfRoom', sa.Integer)

class TBL_InvoiceLineItem(Base):
    __tablename__ = 'TBL_InvoiceLineItem'
    invoiceID = Column('invoiceID', ForeignKey('TBL_Invoices.invoiceID'), primary_key=True)
    roomID = Column('roomID', ForeignKey('TBL_Rooms.roomID'), primary_key=True)
    remark = Column('remark', sa.String(50))

class TBL_Receipts(Base):
    __tablename__ = 'TBL_Receipts'
    receiptID = Column('receiptID', sa.String(6), primary_key=True)
    customerID = Column('customerID', ForeignKey('TBL_Customer.customerID'))
    paymentMedId = Column('paymentMedId', ForeignKey('TBL_PaymentMedthods.paymentMedId'))
    cuponID = Column('cuponID', ForeignKey('TBL_Coupons.cuponID'))
    dateCreate = Column('dateCreate', sa.Date)
    paymentRef = Column('paymentRef', sa.String(30))
    totalReceived = Column('totalReceived', sa.Float(precision=2))
    remark = Column('remark', sa.String(50))

class TBL_ReceiptsLineItem(Base):
    __tablename__ = 'TBL_ReceiptsLineItem'
    receiptID = Column('receiptID', ForeignKey('TBL_Receipts.receiptID'), primary_key=True)
    invoiceID = Column('invoiceID', ForeignKey('TBL_Invoices.invoiceID'), primary_key=True)
    remark = Column('remark', sa.String(50))

class TBL_PaymentMedthods(Base):
    __tablename__ = 'TBL_PaymentMedthods'
    paymentMedId = Column('paymentMedId', sa.String(6), primary_key=True)
    name = Column('name', sa.String(10))

class TBL_Coupons(Base):
    __tablename__ = 'TBL_Coupons'
    cuponID = Column('cuponID', sa.String(6), primary_key=True)
    name = Column('name', sa.String(10))
    exipreDate = Column('exipreDate', sa.Date)

class TBL_Employees(Base):
    employeeID = Column('employeeID', sa.String(6), primary_key=True)
    employeeTypeID = Column('employeeTypeID', ForeignKey('TBL_EmployeeTypes.employeeTypeID'))
    firstname = Column('firstname', sa.String(20))
    familyname = Column('familyname', sa.String(20))
    email = Column('email', sa.String(50))
    phoneNumber = Column('phoneNumber', sa.String(10))
    accepteDate = Column('accepteDate', sa.String(10))

class TBL_EmployeeTypes(Base)
    employeeTypeID = Column('employeeTypeID', sa.String(6), primary_key=True)
    name = Column('name', sa.String(20))
    salary = Column('salary', sa.Float(precision=2))