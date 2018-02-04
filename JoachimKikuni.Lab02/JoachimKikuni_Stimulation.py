import random

names = ["joey", "bobby", "susan", "Loretta", "grant",\
         "jenny"]
waitingRoom = []
triageRoom = []
examRoom = []
examRoomSize = 6
doctors = 6



class Physician:
    def __init__(self, name):

        self.name = name
        
    def examination():

    def callNurse():
        "move patient from waiting room to triage room"
    triageRoom.append(waitingRoom.pop(0))
    sort(triageRoom, key=patient.triageNumber)
    
         

class nurse: 

    def __init__(self, name):
        self.name = name

    def getPatient():

    def sendPatient():


class Patient:
    def __init__(self):
        self.triageNumber = random.randint(100)
        self.name = names[random.randint(len(names))]\
                     +names[random.randint(len(names))]
        self.arrivalTime = time
        self.treatmentTime = random.randint(15, 20)
        
        
        #currentLocation
        #triageTime
        #name
        #arrivalTime
        #treatmentTime(15-20 minutes)

    def exit(self):
        #remove patient from simulation
        pass
    
        

class ExamRoom:
    def __init__(self, name, physician):
        
        self.name = name
        self.physician = physician
        self.runTime = 0
        self.Patient = None
        
    def addPatients(self, waitingRoom):
        self.waitingList2.pop(0)

    
    def removePatients(self):
    
    def timeRemaining(self):
        return self.runTime

class WaitingRoom:
    
    def __innit__(self):
        self.waitingList1 = []
        self.waitingList2 = []
        
        
    def addPatients(self, patient):
        self.waitingList.append(patient)
        
    
    def removePatients(self):
        self.waitingList.pop(0)

    def addPatientsTwo():
        self.waitingList2.append(patient)
        
    def removePatientsTwo:
        return self.waitingList2.pop(0)

