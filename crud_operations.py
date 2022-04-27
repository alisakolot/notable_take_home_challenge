import requests
import json 


"""Pulling data from the Doctors DB"""
f = open('doctors.json')
data = json.load(f)
doctors = data[0]['doctors']


def get_doctor_list(data):
    """Get list of Doctors"""

    doctors = data[0]['doctors']
    doctor_names_lst = doctors[0]["name"]
    return doctor_names_lst

print("Doctors: ", get_doctor_list(data), "\n")


def doctors_apt_lst(doctors, doctor_name): 
    """Get list of appointments for doctor"""

    for doctor in doctors: 
        if doctors[0]["name"] == doctor_name: 
            return doctors[0]["appointments"]

print("List of appointments: ", doctors_apt_lst(doctors, "Julius Hibbert"), '\n')


def specific_day_apts(doctors, day, doctor_name):
    """Get appointments on specific day for doctor"""
    for doctor in doctors: 
            if doctors[0]["name"] == doctor_name: 
                for item in doctors[0]["appointments"]: 
                    if item["day"] == day:
                        return item

print("Apts on specific day: ", specific_day_apts(doctors, "05/09/2018", "Julius Hibbert"))


# TODO: Appointments should be able to be removed by id, patient name, day, and kind
def delete_apt(doctors, doctor_name, id):
    """Delete specific appointment from doctor's calendar"""
    for doctor in doctors: 
        if doctors[0]["name"] == doctor_name: 
            for item in doctors[0]["appointments"]: 
                if item["id"] == id:
                    print("Item removed: ", item, '\n')
                    doctors[0]["appointments"].remove(item)
                    return doctors[0]["appointments"]

print("Updated appt list: ", delete_apt(doctors, "Julius Hibbert", 1), '\n')



# """
# Add a new appointment to doctor's calendar. 
# Appointments can only start in 15min intervals. 
# Doctor can have multiple appointments at the same time, but no more than 3 per time slot.    
# """
# # Add a new item to the appointment list
# # Conditions need to accoutnt for no more than 3 items can have the same time

# Test data
new_appts = [
    {"id":11, "patient name": "Madeleine L'Engle", "day": "05/10/2018", "time": "9:20AM", "kind": "New Patient"},
    {"id":7, "patient name":"Colin Robinson", "day": "05/10/2018", "time": "9:00AM", "kind": "New Patient"}, 
    {"id":8, "patient name":"George Glass", "day": "05/10/2018", "time": "9:00AM", "kind": "New Patient"}, 
    {"id":9, "patient name":"Keanu Reeves", "day": "05/10/2018", "time": "9:00AM", "kind": "New Patient"}, 
    {"id":10, "patient name":"Gordon Barry", "day": "05/10/2018", "time": "9:00AM", "kind": "New Patient"}, 
]

an_acceptable_time_dict = {"15", "30", "45", "00"}

def add_to_calendar(doctors, doctor_name, new_appts, an_acceptable_time): 

    for doctor in doctors: 
        if doctors[0]["name"] == "Julius Hibbert": 
            count = 0 

            for items in new_appts: 
                if items["time"][-4:-2] in an_acceptable_time_dict:
                    doctors[0]["appointments"].append(items)
                    count += 1

                    if count == 3:
                        break

                else: 
                    print("Cannot add", items["time"])

        return doctors[0]["appointments"]

print("Add to calendar: ", add_to_calendar(doctors, "Julius Hibbert",  new_appts,  {"15", "30", "45", "00"}))


