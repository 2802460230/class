#circle class

class circle:
    def __init__(self):
        self.radius = 0
        self.colour = ""
        self.pi = 3.14

    def getColour(self):
        return self.colour
    
    def getCircum(self):
        Circum = self.pi * 2 * self.radius
        return Circum

  #player class

class player:
    def __init__(self):
        self.inventory = {}
        self.money = 0
        self.health = 0

    def addinventory(self,itemid,quanitity):
        self.inventory[itemid] = quanitity

    def removeinventory(self,itemid,quantity):
        self.inventory.pop(itemid)

    def addmoney(self,money):
        self.money = self.money + money

    def removemoney(self,money):
        self.money = self.money - money

    def reducehealth(self,health):
        self.health = self.health - health
        if self.health < 0:
            print("dead")

import datetime
import pickle

#my own class

class CarRecord:
  def __init__(self,VehicleID="",RegistrationNumber="",EngineSize= 0):
    self.VehicleID = VehicleID
    self.RegistrationNumber = RegistrationNumber
    self.RegistrationDate = ""
    self.EngineSize = EngineSize
    self.PurchasePrice = 0.0

  def setDateOfRegistration(self,RegistrationDate):
    self.DateOfRegistration = RegistrationDate
  def setPurchasePrice(self,PurchasePrice):
    self.PurchasePrice = PurchasePrice
  def getVehicleID(self):
    return(self.VehicleID)
  def getRegistration(self):
    return(self.RegistrationNumber)
  def getDateOfREgistration(self):
    return(self.DateOfRegistration)
  def getEmgomeSoze(self):
    return(self.EngineSize)
  def getPurchasePrice(self):
    return(self.PurchasePrice)

cars = [CarRecord() for i in range(2)]
cars[0] = CarRecord("ABCD","B1234",1000)
cars[1] = CarRecord("XYZ","B5678",2000)

print(cars[0].getVehicleID())

CarFile = open('CarFile.DAT', 'wb')
for i in range(2):
  pickle.dump(cars[i], CarFile)

CarFile.close()
CarFile = open('CarFile.DAT', 'rb')
cars1 = []
try:
  while True: 
    cars1.append(pickle.load(CarFile))
except:
  print("end of file reached")
CarFile.close()
for i in range(2):
  print(cars1[i].getVehicleID())