import sqlalchemy as sa
from sqlalchemy import Column 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TBL_Customer(Base):
    __tablename__ = 'TBL_Customer'
    customerID = Column('customerID', sa.String(6) ,primary_key=True)
    firstname = Column('firstname', sa.String(20) )
    familyname = Column('familyname', sa.String(20) )
    email = Column('email', sa.String(50) )
    phoneNumber = Column('phoneNumber', sa.String(10) )
    creditCardNumber = Column('creditCardNumber', sa.String(16) )
    point = Column('point', sa.Integer )
