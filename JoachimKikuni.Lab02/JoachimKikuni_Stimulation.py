import random

class Physician:
    def __init__(self, name):

        self.name = name


class Patient:
    def __init__(self, triaged, triageLevel, waitingRoom, ExamRoom, minutes):
        self.triaged = triaged
        self.triageLevel = triageLevel
        self.waitingRoom = waitingRoom
        self.ExamRoom = ExamRoom
        self.minutes = random.randint(15, 20)

class ExamRoom:
    def __init__(self, name, physicianName, isfull, patient):
        self.name = name
        self.physicianName = physicianName
        self.idFull = isFull
        self.Patient = Patient

physian1 = Physician ("Physician1")
physian2 = Physician ("Physician2")
physian3 = Physician ("Physician3")
physian4 = Physician ("Physician4")
physicians = [physian1, physian2, physian3, physian4]

patient1 = Patient(False, 0, False, None, 0)
patient2 = Patient(False, 0, False, None, 0)
patients = [patient1, patient2]


exam = ExamRoom["ExamRoom 1", "", False, None]
exam = ExamRoom["ExamRoom 2", "", False, None]
exam = ExamRoom["ExamRoom 3", "", False, None]
exam = ExamRoom["ExamRoom 4", "", False, None]

examrooms = [exam1, exam2, exam3, exam4]

def simulate():
    for physician in physicians:
        for examroom in examrooms:
            if examroom.PhycisianName is "":
                examroom.physicianName = physicianName
                break
    urgency = 0
    for x in range(len(patients)):
        if patients[x].triagelevel > urgency:
            urgance = patients[x].triageLevel

            for examroom in examrooms:
                if examroom.Patient is None:
                    examroom.Patient = Patients[x]
            
    
    print(patient1.minutes)
    for examroom in examrooms:
        print(examroom.name, examroom.phhysicianName)

