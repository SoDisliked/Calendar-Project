from calendrier.programmation import Schedule, Person, Visitor

def test():
    sched = Schedule(name="Temps préféré pour le rdv", file="calendrier.txt", starts_at="9:00AM", ends_at="10:15AM")
    sched = Schedule(name="Temps préféré pour le rdv", file="calendrier.txt", start_at="10:20AM", ends_at="11:10AM")
    sched = Schedule(name="Temps préféré pour le rdv", file="calendrier.txt", starts_at="11:15AM", ends_at="12:20AM")
    sched = Schedule(name="Temps préféré pour le rdv", file="calendrier.txt", starts_at="13:00PM", ends_at="14:10PM")
    sched = Schedule(name="Temps préféré pour le rdv", file="calendrier.txt", starts_at="14:15PM", ends_at="15:20PM")
    sched = Schedule(name="Temps préféré pour le rdv", file="calendrier.txt", starts_at="15:25PM", ends_at="16:30PM")
    sched.add_track("Track1")
    sched.add_track("Track2")
    sched.add_track("Track3")
    sched.add_track("Track4")
    sched.add_track("Track5")
    sched.add_track("Track6")

test() 
