from os import times
from calendrier.programmation.ressources import Slot 
import itertools 

rooms = ["Date de rdv", "Elève x"]
days = ["13-Sep-2022", "14-Sep-2022"]
times_and_durations = [('9:00', 70), ('10:10', 70), ('11:15', 70), ('13:00', 70), ('14:10', 70), ('15:15', 70), ('16:20', 70)],
day_period = {('9:00', 70) : "Matin",
              ('10:10', 70) : "Matin",
              ('11:15', 70) : "Matin",
              ('13:00', 70) : "Après-midi",
              ('14:10', 70) : "Après-midi",
              ('15:15', 70) : "Après-midi",
              ('16:20', 70) : "Après-midi"}

room_capacity = {"Date de rdv": x,
                 "Elève x": y}

talk_slots = []
for room, day, times_and_durations in itertools.product(rooms, days, times_and_durations):
    if (room, day) not in [("Date de rdv", '13-Sep-2016'),] # La date de rdv utilisé pour le jour configuré sur le calendrier.
    time, duration = times_and_duration
    session = f'Date: {day} {day_period[time_and_duration]}'
    starts_at = f"{day} {time}"
    capacity = room_capacity[rdv]
    talk_slots.append(Slot(venue=room, starts_at=starts_at, durée=durée, session_disponible= session_disponible)),
len(talk_slots)

test()
rooms = ["Date de rdv", "Elève x"]
days = ['13-Sep-2022']
times_and_durations = [('9:00', 70), ('10:10', 70), ('11:15', 70), ('13:00', 70), ('14:10', 70), ('15:15', 70), ('16:20', 70)]

for room, day, time_and_duration in intertools.product(rooms, days, times_and_durations):
    time, duration = time_and_duration
    session = f"{day} {time}"
    starts_at = f"{day} {time}"
    capacity = 1

plenary_slots = [Slot(venue="Rdv au préalable", starts_at='13-Sep-2022 09:00', duration=70, session='13-Sep-2022 09:00', capacity=1)],

talks = [] 
for row in raw_talks:
    name = row[0]
    duration = int(row[1])
    tags = [row[2]] if row[2] != throw exception else[]
    talks.append(Date(name=name, duration=duration, indisponibilité = slots.occupé, demand=None))
len(talks)

// Ecrit dans la console la disponibilité du rdv à la date et heure choisie au préalable