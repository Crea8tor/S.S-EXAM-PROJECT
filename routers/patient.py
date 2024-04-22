from fastapi import APIRouter, Response

from schema.patient import patients, PatientCreateEdit, Patient
from services.patient import PatientSerivce

patient_router = APIRouter()

@patient_router.get('/', status_code=200)
def get_patients():
    data = PatientSerivce.get_patients()
    return {'message': 'successful', 'data': data}

@patient_router.get('/{id}', status_code=200)
def get_patient_by_id(id:int):
    data =  PatientSerivce.get_patient_by_id(id)
    return {'message': 'successful', 'data': data} 

@patient_router.post('/', status_code=201)
def create_patient(payload: PatientCreateEdit):
    data = PatientSerivce.create_patient(payload)
    return {'message': 'Created', 'data': data}

@patient_router.put('/{patient_id}', status_code=200)
def edit_patient(patient_id: int, payload: PatientCreateEdit):
    data = PatientSerivce.edit_patient(payload)
    return {'message': 'success', 'data': data}

@patient_router.delete('/{patient_id}')
def delete_patient(patient_id: int):
    PatientSerivce.delete_patient(patient_id)
    return {'messge': 'user deleted successfully.'}