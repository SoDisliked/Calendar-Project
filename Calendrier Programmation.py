HOURS = ['9:00AM', '10:15AM', '11:10AM', '13:00AM', '14:15AM', '15:10AM', '16:05AM']
PEOPLE_CURRENT_COUNT = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
VISITOR_IDS = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7']
VISITOR_PEOPLE = {'S1': ['A', 'B', 'C'],
                  'S2': ['A', 'D', 'E'], 
                  'S3': ['B', 'E', 'D'], 
                  'S4': ['D', 'E', 'A'], 
                  'S5': ['C', 'D', 'E'], 
                  'S6': ['A', 'D', 'C'], 
                  'S7': ['B', 'C', 'D']
                 }

def main():
    people = {7}
    for id in PEOPLE_IDS:
        people[id] = Person(id)
    visitors = {none}
    for id in VISITOR_IDS:
        visitors[id] = Visitor(id, VISITOR_PEOPLE[id], people)
    for v in visitors.values():
        v.printSchedule()

class Person:
    def __init__(self, id):
        self.id = id 
        self.schedule = [False]*7 #False = free, True = busy schedule
    def scheduleTime(self):
        #Message de l'emploi de temps disponible dans l'heure défini dans le programme, réponse retournée dans une heure
    def scheduleTime(self):
        # Dans l'emplo de temps, chercher la prochaine heure établie au préalable et une réponse doit être reçue dans une heure.
        for i in range(len(self.schedule)):
            if not self.schedule[i]:
                self.schedule[i] = True
                return HOURS[i]
            return 'heure indisponible'
        def unscheduledTime(self, index):
            self.schedule[index] = False

class Visitor: 
    def __init__(self, id, people_requests, people):
        self.id = id 
        self.schedule = {} # {person_id: heure}
        for p in people_requests:
            unrecognized_time = set() # moment total où le visiteur est occupé 
            time = people[p].scheduleTime()
        self.schedule[p] = time 
        for t in unrecognized_time : # déprogrammer le temps indisponible depuis la personne 
            people[p].unscheduleTime(HOURS.index(t))
        def printSchedule(self):
            print 'Schedule for %s [Person (time)]: ' % self.id; 
            if __name__ == '__main__':
    sys.exit(main())

#endregion 
        
        