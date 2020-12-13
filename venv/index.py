from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from src import Customer as C
from src import Auth as Au
from src import Room as R
from src import Invoice as I
from src import Receipt as Re
from src import Employee as E

app = Flask(__name__)
CORS(app)

Customer = C.Customer()
Auth = Au.Auth()
Room = R.Room()
Invoice = I.Invoice()
Receipt = Re.Receipt()
Employee = E.Employee()

@app.route('/')
@cross_origin()
def home():
    return 'This is backend new-hotel'

# Customer
# createCustomer use for create customer
@app.route('/customer',methods=["POST"])
@cross_origin()
def createCustomer():
    customerID = request.form['customerID']
    firstname = request.form['firstname']
    familyname = request.form['familyname']
    email = request.form['email']
    phoneNumber = request.form['phoneNumber']
    creditCardNumber = request.form['creditCardNumber']
    point = request.form['point']

    logs = Customer.create(customerID, firstname, familyname, email, phoneNumber, creditCardNumber, point)
    return logs

# readCustomer get all or get specific by customerID from customer
@app.route('/customer/<customerID>',methods=["GET"])
@cross_origin()
def readCustomer(customerID=None):
    if customerID != None:
        log = Customer.read(customerID)
        return jsonify(log)

@app.route('/getAllcustomer', methods=["GET"])
@cross_origin()
def getAllCustomer():
    log = Customer.getAllCustomer()
    return jsonify(log)

# updateCustomer use for update customer 
@app.route('/customer',methods=["PUT"])
@cross_origin()
def updateCustomer():
    customerID = request.form['customerID']
    firstname = request.form['firstname']
    familyname = request.form['familyname']
    email = request.form['email']
    phoneNumber = request.form['phoneNumber']
    creditCardNumber = request.form['creditCardNumber']
    point = request.form['point']

    log = Customer.update(customerID, firstname, familyname, email, phoneNumber, creditCardNumber, point)
    return jsonify(log)

# deleteCustomer use for delele customer
@app.route('/customer/<customerID>',methods=["DELETE"])
@cross_origin()
def deleteAccount(customerID=None):
    if customerID != None:
        log = Customer.delete(customerID)
        return jsonify(log)


# Auth
# createAuth use for create auth
@app.route('/auth',methods=["POST"])
@cross_origin()
def createAuth():
    authID = request.form['authID']
    customerID = request.form['customerID']
    password = request.form['password']

    logs = Auth.create(authID, customerID, password)
    return logs

# readAccount get all or get specific by customerID from customer
@app.route('/auth/<customerID>',methods=["GET"])
@cross_origin()
def readAuth(customerID=None):
    if customerID != None:
        log = Auth.read(customerID)
        return jsonify(log)

@app.route('/getAllauth', methods=["GET"])
@cross_origin()
def getAllAuth():
    log = Auth.getAllAuth()
    return jsonify(log)

# updateCustomer use for update customer 
@app.route('/auth',methods=["PUT"])
@cross_origin()
def updateAuth():
    authID = request.form['authID']
    customerID = request.form['customerID']
    password = request.form['password']

    log = Auth.update(authID, customerID, password)
    return jsonify(log)

# deleteCustomer use for delele customer
@app.route('/auth/<customerID>',methods=["DELETE"])
@cross_origin()
def deleteAuth(customerID=None):
    if customerID != None:
        log = Auth.delete(customerID)
        return jsonify(log)

# login for customer to login who already register
@app.route('/login',methods=["POST"])
@cross_origin()
def login():
    email = request.form['email']
    password = request.form['password']

    log = Auth.login(email, password)
    return jsonify(log)

# register for customer who isn't register
@app.route('/register',methods=["POST"])
@cross_origin()
def register():
    firstname = request.form['firstname']
    familyname = request.form['familyname']
    email = request.form['email']
    phoneNumber = request.form['phoneNumber']
    creditCardNumber = request.form['creditCardNumber']
    point = request.form['point']
    password = request.form['password']

    log = Auth.register(firstname, familyname, email, phoneNumber, creditCardNumber, point, password)
    return jsonify(log)

# Rooms
# createRooms use for create room
@app.route('/room',methods=["POST"])
@cross_origin()
def createRoom():
    roomID = request.form['roomID']
    roomCatID = request.form['roomCatID']
    status = request.form['status']
    cleanStatus = request.form['cleanStatus']

    logs = Room.create(roomID, roomCatID, status, cleanStatus)
    return logs

# readRoom get all or get specific by roomID
@app.route('/room/<roomID>',methods=["GET"])
@cross_origin()
def readRoom(roomID=None):
    if roomID != None:
        log = Room.read(roomID)
        return jsonify(log)

@app.route('/getAllroom', methods=["GET"])
@cross_origin()
def getAllRoom():
    log = Room.getAllRoom()
    return jsonify(log)

# updateRoom use for update room 
@app.route('/room',methods=["PUT"])
@cross_origin()
def updateRoom():
    roomID = request.form['roomID']
    roomCatID = request.form['roomCatID']
    status = request.form['status']
    cleanStatus = request.form['cleanStatus']

    log = Room.update(roomID, roomCatID, status, cleanStatus)
    return jsonify(log)

# deleteRoom use for delele room
@app.route('/room/<roomID>',methods=["DELETE"])
@cross_origin()
def deleteRoom(roomID=None):
    if roomID != None:
        log = Room.delete(roomID)
        return jsonify(log)

# roomCatType use for create roomCatType
@app.route('/roomcat',methods=["POST"])
@cross_origin()
def createRoomCat():
    roomCatID = request.form['roomCatID']
    name = request.form['name']
    bedType = request.form['bedType']
    numberBed = request.form['numberBed']
    guestRoom = request.form['guestRoom']
    fare = request.form['fare']

    logs = Room.createRoomCat(roomCatID, name, bedType, numberBed, guestRoom, fare)
    return logs

# readRoomType get all or get specific by roomCatID from roomCatType
@app.route('/roomcat/<roomCatID>',methods=["GET"])
@cross_origin()
def readRoomCat(roomCatID=None):
    if roomCatID != None:
        log = Room.readRoomCat(roomCatID)
        return jsonify(log)

@app.route('/getAllroomCat', methods=["GET"])
@cross_origin()
def getAllRoomCat():
    log = Room.getAllRoomCat()
    return jsonify(log)

# updateRoomCat use for update roomCat 
@app.route('/roomcat',methods=["PUT"])
@cross_origin()
def updateRoomCat():
    roomCatID = request.form['roomCatID']
    name = request.form['name']
    bedType = request.form['bedType']
    numberBed = request.form['numberBed']
    guestRoom = request.form['guestRoom']
    fare = request.form['fare']

    log = Room.updateRoomCat(roomCatID, name, bedType, numberBed, guestRoom, fare)
    return jsonify(log)

# deleteRoomCat use for delele customer
@app.route('/roomcat/<roomCatID>',methods=["DELETE"])
@cross_origin()
def deleteRoomCat(roomCatID=None):
    if roomCatID != None:
        log = Room.deleteRoomCat(roomCatID)
        return jsonify(log)

# Invoice
# Invoice use for create invoice
@app.route('/invoice',methods=["POST"])
@cross_origin()
def createInvoice():
    invoiceID = request.form['invoiceID']
    roomCatID = request.form['roomCatID']
    customerID = request.form['customerID']
    dateCreate = request.form['dateCreate']
    total = request.form['total']
    vat = request.form['vat']
    checkIn = request.form['checkIn']
    checkOut = request.form['checkOut']
    numberOfRoom = request.form['numberOfRoom']

    logs = Invoice.create(invoiceID, roomCatID, customerID, dateCreate, total, vat, checkIn, checkOut, numberOfRoom)
    return logs

# createInvoiceWithOutId use for create invoice with out id
@app.route('/invoiceWithoutID',methods=["POST"])
@cross_origin()
def createInvoiceWithOutId():
    roomCatID = request.form['roomCatID']
    customerID = request.form['customerID']
    dateCreate = request.form['dateCreate']
    total = request.form['total']
    vat = request.form['vat']
    checkIn = request.form['checkIn']
    checkOut = request.form['checkOut']
    numberOfRoom = request.form['numberOfRoom']

    logs = Invoice.createWithOutID(roomCatID, customerID, dateCreate, total, vat, checkIn, checkOut, numberOfRoom)
    return logs

# readInvovice get all or get specific by invoiceID from invoice
@app.route('/invoice/<invoiceID>',methods=["GET"])
@cross_origin()
def readInvovice(invoiceID=None):
    if invoiceID != None:
        log = Invoice.read(invoiceID)
        return jsonify(log)

@app.route('/getAllInvoice', methods=["GET"])
@cross_origin()
def getAllInovice():
    log = Invoice.getAllInvoice()
    return jsonify(log)

# updateInvoice use for update Invocie 
@app.route('/invoice',methods=["PUT"])
@cross_origin()
def updateInvoice():
    invoiceID = request.form['invoiceID']
    roomCatID = request.form['roomCatID']
    customerID = request.form['customerID']
    dateCreate = request.form['dateCreate']
    total = request.form['total']
    vat = request.form['vat']
    checkIn = request.form['checkIn']
    checkOut = request.form['checkOut']
    numberOfRoom = request.form['numberOfRoom']

    log = Invoice.update(invoiceID, roomCatID, customerID, dateCreate, total, vat, checkIn, checkOut, numberOfRoom)
    return jsonify(log)

# deleteInvoice use for delele invoice
@app.route('/invoice/<invoiceID>',methods=["DELETE"])
@cross_origin()
def deleteInvoice(invoiceID=None):
    if invoiceID != None:
        log = Invoice.delete(invoiceID)
        return jsonify(log)

# createInvoiceLine use for create invoiceLine
@app.route('/invoiceLine',methods=["POST"])
@cross_origin()
def createInvoiceLine():
    invoiceID = request.form['invoiceID']
    roomID = request.form['roomID']
    remark = request.form['remark']

    logs = Invoice.createInvoiceLine(invoiceID, roomID, remark)
    return logs

# readInvoviceLine get all or get specific by invoiceID and roomID from invoiceLine
@app.route('/invoiceLine',methods=["GET"])
@cross_origin()
def readInvoviceLine():
    invoiceID = request.args.get('invoiceID')
    roomID = request.args.get('roomID')
    if invoiceID != None and roomID != None:
        log = Invoice.readInvoiceLine(invoiceID, roomID)
        return jsonify(log)

@app.route('/getAllInvoiceLine', methods=["GET"])
@cross_origin()
def getAllInoviceLine():
    log = Invoice.getAllInvoiceLine()
    return jsonify(log)

# updateInvoiceLine use for update invoiceLine 
@app.route('/invoiceLine',methods=["PUT"])
@cross_origin()
def updateInvoiceLine():
    invoiceID = request.form['invoiceID']
    roomID = request.form['roomID']
    remark = request.form['remark']

    log = Invoice.updateInvoiceLine(invoiceID, roomID, remark)
    return jsonify(log)

# deleteInvoiceLine use for delele invoiceLine
@app.route('/invoiceLine',methods=["DELETE"])
@cross_origin()
def deleteInvoiceLine():
    invoiceID = request.args.get('invoiceID')
    roomID = request.args.get('roomID')
    if invoiceID != None and roomID != None:
        log = Invoice.deleteInvoiceLine(invoiceID, roomID)
        return jsonify(log)

# deleteInvoiceLineByInvoivceID use for delele invoiceLine by invoiceID
@app.route('/invoiceLineByInvoviceID',methods=["DELETE"])
@cross_origin()
def deleteInvoiceLineByInvoivceID():
    invoiceID = request.args.get('invoiceID')
    if invoiceID != None:
        log = Invoice.deleteInvoiceLineByInvoivceID(invoiceID)
        return jsonify(log)

# readInvoiceLineByInvoivceID use for read invoiceLine by invoiceID
@app.route('/invoiceLineByInvoviceID',methods=["GET"])
@cross_origin()
def readInvoiceLineByInvoivceID():
    invoiceID = request.args.get('invoiceID')
    if invoiceID != None:
        log = Invoice.readInvoiceLineByInvoiceID(invoiceID)
        return jsonify(log)

# Receipt
# createReceipt use for create Receipt
@app.route('/receipt',methods=["POST"])
@cross_origin()
def createReceipt():
    receiptID = request.form['receiptID']
    customerID = request.form['customerID']
    paymentMedId = request.form['paymentMedId']
    cuponID = request.form['cuponID']
    dateCreate = request.form['dateCreate']
    paymentRef = request.form['paymentRef']
    totalReceived = request.form['totalReceived']
    remark = request.form['remark']

    logs = Receipt.create(receiptID, customerID, paymentMedId, cuponID, dateCreate, paymentRef, totalReceived, remark)
    return logs

# createReceiptWithOutId use for create Receipt without id
@app.route('/receiptWithoutID',methods=["POST"])
@cross_origin()
def createReceiptWithOutId():
    customerID = request.form['customerID']
    paymentMedId = request.form['paymentMedId']
    cuponID = request.form['cuponID']
    dateCreate = request.form['dateCreate']
    paymentRef = request.form['paymentRef']
    totalReceived = request.form['totalReceived']
    remark = request.form['remark']

    logs = Receipt.createWithOutID(customerID, paymentMedId, cuponID, dateCreate, paymentRef, totalReceived, remark)
    return logs

# readReceipt get all or get specific by receiptID from receipt
@app.route('/receipt/<receiptID>',methods=["GET"])
@cross_origin()
def readReceipt(receiptID=None):
    if receiptID != None:
        log = Receipt.read(receiptID)
        return jsonify(log)

@app.route('/getAllReceipt', methods=["GET"])
@cross_origin()
def getAllReceipt():
    log = Receipt.getAllReceipt()
    return jsonify(log)

# updateReceipt use for update receipt 
@app.route('/receipt',methods=["PUT"])
@cross_origin()
def updateReceipt():
    receiptID = request.form['receiptID']
    customerID = request.form['customerID']
    paymentMedId = request.form['paymentMedId']
    cuponID = request.form['cuponID']
    dateCreate = request.form['dateCreate']
    paymentRef = request.form['paymentRef']
    totalReceived = request.form['totalReceived']
    remark = request.form['remark']

    log = Receipt.update(receiptID, customerID, paymentMedId, cuponID, dateCreate, paymentRef, totalReceived, remark)
    return jsonify(log)

# deleteReceipt use for delele receipt
@app.route('/receipt/<receiptID>',methods=["DELETE"])
@cross_origin()
def deleteReceipt(receiptID=None):
    if receiptID != None:
        log = Receipt.delete(receiptID)
        return jsonify(log)

# createReceiptLine use for create receiptLine
@app.route('/receiptLine',methods=["POST"])
@cross_origin()
def createReceiptLine():
    receiptID = request.form['receiptID']
    invoiceID = request.form['invoiceID']
    remark = request.form['remark']

    logs = Receipt.createReceiptLine(receiptID, invoiceID, remark)
    return logs

# readReceiptLine get all or get specific by receiptID and invoiceID from receiptLine
@app.route('/receiptLine',methods=["GET"])
@cross_origin()
def readReceiptLine():
    receiptID = request.args.get('receiptID')
    invoiceID = request.args.get('invoiceID')

    if receiptID != None and invoiceID != None:
        log = Receipt.readReceiptLine(receiptID, invoiceID)
        return jsonify(log)

@app.route('/getAllReceiptLine', methods=["GET"])
@cross_origin()
def getAllReceiptLine():
    log = Receipt.getAllReceiptLine()
    return jsonify(log)

# updateReceiptLine use for update receiptLine 
@app.route('/receiptLine',methods=["PUT"])
@cross_origin()
def updateReceiptLine():
    receiptID = request.form['receiptID']
    invoiceID = request.form['invoiceID']
    remark = request.form['remark']

    log = Receipt.updateReceiptLine(receiptID, invoiceID, remark)
    return jsonify(log)

# deleteReceiptLine use for delele receiptLine
@app.route('/receiptLine',methods=["DELETE"])
@cross_origin()
def deleteReceiptLine():
    receiptID = request.args.get('receiptID')
    invoiceID = request.args.get('invoiceID')
    if receiptID != None and invoiceID != None:
        log = Receipt.deleteReceiptLine(receiptID, invoiceID)
        return jsonify(log)

# readReceiptLineByInvoivceID use for read invoiceLine by invoiceID
@app.route('/receiptLineByReceiptID',methods=["GET"])
@cross_origin()
def readReceiptLineByInvoivceID():
    receiptID = request.args.get('receiptID')
    if receiptID != None:
        log = Receipt.readReceiptLineByReceiptID(receiptID)
        return jsonify(log)

# Employee
# createEmployee use for create Employee
@app.route('/employee',methods=["POST"])
@cross_origin()
def createEmployee():
    employeeID = request.form['employeeID']
    employeeTypeID = request.form['employeeTypeID']
    firstname = request.form['firstname']
    familyname = request.form['familyname']
    email = request.form['email']
    phoneNumber = request.form['phoneNumber']
    accepteDate = request.form['accepteDate']

    logs = Employee.create(employeeID, employeeTypeID, firstname, familyname, email, phoneNumber, accepteDate)
    return logs

@app.route('/employeeWithoutID',methods=["POST"])
@cross_origin()
def createEmployeeWithoutID():
    employeeTypeID = request.form['employeeTypeID']
    firstname = request.form['firstname']
    familyname = request.form['familyname']
    email = request.form['email']
    phoneNumber = request.form['phoneNumber']
    accepteDate = request.form['accepteDate']

    logs = Employee.createWithOutID(employeeTypeID, firstname, familyname, email, phoneNumber, accepteDate)
    return logs

# readEmployee get all or get specific by employeeID from Employee
@app.route('/employee/<employeeID>',methods=["GET"])
@cross_origin()
def readEmployee(employeeID=None):
    if employeeID != None:
        log = Employee.read(employeeID)
        return jsonify(log)

@app.route('/getAllEmployee', methods=["GET"])
@cross_origin()
def getAllEmployee():
    log = Employee.getAllEmployee()
    return jsonify(log)

# updateEmployee use for update employee 
@app.route('/employee',methods=["PUT"])
@cross_origin()
def updateEmployee():
    employeeID = request.form['employeeID']
    employeeTypeID = request.form['employeeTypeID']
    firstname = request.form['firstname']
    familyname = request.form['familyname']
    email = request.form['email']
    phoneNumber = request.form['phoneNumber']
    accepteDate = request.form['accepteDate']

    log = Employee.update(employeeID, employeeTypeID, firstname, familyname, email, phoneNumber, accepteDate)
    return jsonify(log)

# deleteEmployee use for delele employee
@app.route('/employee/<employeeID>',methods=["DELETE"])
@cross_origin()
def deleteEmployee(employeeID=None):
    if employeeID != None:
        log = Employee.delete(employeeID)
        return jsonify(log)

# createEmployeeType use for create EmployeeType
@app.route('/employeeType',methods=["POST"])
@cross_origin()
def createEmployeeType():
    employeeTypeID = request.form['employeeTypeID']
    name = request.form['name']
    salary = request.form['salary']

    logs = Employee.createEmployeeType(employeeTypeID, name, salary)
    return logs

# readEmployeeType get all or get specific by employeeTypeID from EmployeeType
@app.route('/employeeType/<employeeTypeID>',methods=["GET"])
@cross_origin()
def readEmployeeType(employeeTypeID=None):
    if employeeTypeID != None:
        log = Employee.readEmployeeType(employeeTypeID)
        return jsonify(log)

@app.route('/getAllEmployeeType', methods=["GET"])
@cross_origin()
def getAllEmployeeType():
    log = Employee.getAllEmployeeType()
    return jsonify(log)

# updateEmployeeType use for update EmployeeType 
@app.route('/employeeType',methods=["PUT"])
@cross_origin()
def updateEmployeeType():
    employeeTypeID = request.form['employeeTypeID']
    name = request.form['name']
    salary = request.form['salary']

    log = Employee.updateEmployeeType(employeeTypeID, name, salary)
    return jsonify(log)

# deleteEmployeeType use for delele EmployeeType
@app.route('/employeeType/<employeeTypeID>',methods=["DELETE"])
@cross_origin()
def deleteEmployeeType(employeeTypeID=None):
    if employeeTypeID != None:
        log = Employee.deleteEmployeeType(employeeTypeID)
        return jsonify(log)
