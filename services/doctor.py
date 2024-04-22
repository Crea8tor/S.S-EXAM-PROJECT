from fastapi import HTTPException
from schema.doctor import doctors, Doctor, DoctorCreateEdit

class DoctorSerivce:

    @staticmethod
    def parse_doctor(doctor_data):
        data = []
        for cust in doctors:
            data.append(doctor_data[cust])
        return data
    
    @staticmethod
    def get_doctor_by_id(doctor_id:int):
      
       for doctor in doctors: 
        if doctor.id == doctor_id:
         
         
            raise HTTPException(detail='doctor not found.', status_code=404)
        return doctor
    
    @staticmethod
    def create_doctor(doctor_data: DoctorCreateEdit):
        id = len(doctors)
        doctor = Doctor(
            id=id,
            **doctor_data.model_dump()
        )
        doctors[id] = doctor
        doctors.append(doctor)
        return doctor
    
    @staticmethod
    def edit_doctor(payload: DoctorCreateEdit):
        id = len(doctors)
        doctor = Doctor(
            id=id,
            **payload.model_dump()
        )
        doctors[id] = doctor
        return doctor
    
    @staticmethod
    def delete_doctor(doctor_id: int):
        patient = doctors.get(doctor_id)
        if not patient:
            raise HTTPException(detail='doctor not found.', status_code=404)
        del doctors[doctor_id]






Doctor_services = DoctorSerivce()