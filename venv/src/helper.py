from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os 
 
engine = create_engine(os.getenv('DATABASE_URL'))

def initDatabase():
    sm = sessionmaker(engine)
    session = sm()
    return session
def increaseID(textID,breakpoint):
    x = textID.split(breakpoint)
    newVal = str(int(x[1]) + 1)
    newID = breakpoint + (6 - len(newVal) - len(breakpoint))*"0" + newVal
    return newID