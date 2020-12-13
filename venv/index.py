from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from src import Customer as C
from src import Auth as Au
from src import Room as R
from src import Invoice as I

app = Flask(__name__)
CORS(app)

Customer = C.Customer()
Auth = Au.Auth()
Room = R.Room()
Invoice = I.Invoice()

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