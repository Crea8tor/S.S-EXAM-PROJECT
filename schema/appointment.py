from typing import List
from enum import Enum

from pydantic import BaseModel

from schema.patient import Patient, patients
from schema.doctor import Doctor, doctors

# Helps to change status of Appointments
class AppointmentStatus(Enum):
    completed = 'COMPLETED'
    active = "ACTIVE"
    canceled = "CANCELLED"
    
    


class Appointment(BaseModel):
    id : int
    patient : int | Patient
    doctor : int | Doctor
    date : str
    status : str = AppointmentStatus.active.value


class AppointmentCreate(BaseModel):
    patient : int | Patient
    date : str
 


appointments : List = [
    Appointment(
        id = 1,
        patient = patients[0],
        doctor = doctors[0],
        date = "02-10-2024",
        status = AppointmentStatus.active.value
    )
]













# from pydantic import BaseModel


# from schema.doctor import  doctors, Doctors,docs
# from schema.patient import Patients, patients,pats

# class Appointments(BaseModel):
#     id: int
#     patients: list[Patients]
#     doctors:list[Doctors]
#     date:str

# class AppointmentsCreate(BaseModel):
#     patients: list
#     doctors: list 
#     date:str


# appointments: list[Appointments] = [
#       Appointments(
#         id=0, patient=patients[0], doctor=doctors[0], date='22-02-2015')
# ]
# # = [
# #     Appointments(
# #         id=0, patient=patients, doctor=doctors[0], date='22-02-2015')
    
# # ]