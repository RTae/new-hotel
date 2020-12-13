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