from fastapi import APIRouter, Response

from schema.doctor import doctors, DoctorCreateEdit
from services.doctor import DoctorSerivce

doctor_router = APIRouter()

@doctor_router.get('/', status_code=200)
def get_doctors():
    data = DoctorSerivce.parse_doctor()
    return {'message': 'successful', 'data': data}

@doctor_router.get('/{doctor_id}', status_code=200)
def get_doctor_by_id(doctor_id: int):
    data =  DoctorSerivce.get_doctor_by_id(doctor_id)
    return {'message': 'successful', 'data': data} 

@doctor_router.post('/', status_code=201)
def create_doctor(payload: DoctorCreateEdit):
    data = DoctorSerivce.create_doctor(payload)
    return {'message': 'Created', 'data': data}

@doctor_router.put('/{doctor_id}', status_code=200)
def edit_doctor(doctor_id: int, payload: DoctorCreateEdit):
    data = DoctorSerivce.edit_doctor(payload)
    return {'message': 'success', 'data': data}

@doctor_router.delete('/{doctor_id}')
def delete_doctor(doctor_id: int):
    DoctorSerivce.delete_doctor(doctor_id)
    return {'messge': 'doctor deleted successfully.'}