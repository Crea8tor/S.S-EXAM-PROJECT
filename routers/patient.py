from typing import Annotated

from fastapi import APIRouter, status, Depends

from services.patient import PatientService
from schemas.appointment import appointments, AppointmentStatus
from schemas.patient import PatientCreate, patients

patient_router = APIRouter()

@patient_router.post("/create", status_code=status.HTTP_201_CREATED)
def create_patient(payload : PatientCreate):
    data = PatientService.create_doctor(payload)
    return data


@patient_router.get("/get", status_code= status.HTTP_200_OK)
def get_patients():
    data = PatientService.process_patients()
    return {
        "message" : "Success",
        "data" : data
    }

@patient_router.get("/get/{id}", status_code=status.HTTP_200_OK)
def get_patient_by_id(id : int):
    data = PatientService.process_patient_by_id(id)
    return data

@patient_router.put("/edit", status_code=status.HTTP_202_ACCEPTED)
def edit_patient(patient_id : int, payload : PatientCreate):
    curr_patient = PatientService.fetch_patient_by_id(patient_id)
    curr_patient.name = payload.name
    curr_patient.age = payload.age
    curr_patient.gender = payload.gender
    curr_patient.weight = payload.weight
    curr_patient.height = payload.height
    curr_patient.phone = payload.phone

    return {
        "message" : "Doctor Successfully updated",
        "data" : curr_patient
    }

@patient_router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id : int):
    curr_patient = PatientService.fetch_patient_by_id(patient_id)

    for appointment in appointments:
        if appointment.patient == curr_patient:
            break
        appointment.status = AppointmentStatus.canceled.value


        appointed_doctor = appointment.doctor
        appointed_doctor.is_available = True

    del patients[patient_id]

    return {
        "message" : "Patient deleted successfully"
    }