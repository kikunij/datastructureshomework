import random
import time 
names = ["joey", "bobby", "susan", "Loretta", "grant",\
         "jenny", "Pedelson", "Amadou", "Ajata", "Marie",\
         "Albert", "Jonathan", "Dylan"]
waitingRoom = []
triageRoom = []
examRoomSize = 6
doctors = 6
triageRoomSize = 10
examRoom = []
patientsTreated = []
triageNumber = 10


def callNurse():
    "move patient from waiting room to triage room"
    triageRoom.append(waitingRoom.pop(0))
    triageRoom.sort(key =lambda Patient: Patient.triageNumber)

class Patient:
    def __init__(self, time):
        self.triageNumber = random.randint(1, 100)
        self.name = names[random.randint(0, len(names)-1)]\
                     + " " +names[random.randint(0, len(names)-1)]
        self.arrivalTime = time
        self.treatmentTime = random.randint(15, 20)
        self.timeEnteredRoom = 0
              
def simulation():
    time.clock()
    patientTreated = 0
    minute = 1
    while minute != 11:
        print("minute", minute)

        if minute % 2 ==0:
            for i in range(6):
                waitingRoom.append(Patient(minute+1))
        if len(triageRoom) < triageRoomSize:
            if len(waitingRoom) < triageRoomSize:
                for i in range(len(triageRoom), len(waitingRoom)):
                    callNurse()
            elif len(waitingRoom) < triageRoomSize:
                for i in range(len(triageRoom), triageRoomSize):
                    callNurse()
        if len(triageRoom) < triageRoomSize:                        
            for i in range(6):
                waitingRoom.append(Patient(minute))
                
            for i in range(len(waitingRoom)):
                callNurse()
            if len(examRoom) < examRoomSize:
                for i in range (len(examRoom), examRoomSize):
                    nextPatient = triageRoom.pop(0)
                    examRoom.append(nextPatient)
                    nextPatient.timeEnteredExamRoom = minute + 1
                             

        print("patients in exam room")
        for p in examRoom:
            print(p.name, "treatment time", p.treatmentTime, p.timeEnteredExamRoom)
            
        print("patients in Triage room")
        for p in triageRoom:
            print(p.name, "treatment time", p.triageNumber)

        print("patients in waiting room")
        for p in waitingRoom:
            print(p.name)
        print("patients treated:", patientsTreated)
        print("\n") 
        time.sleep(1)
        minute += 1
simulation()
