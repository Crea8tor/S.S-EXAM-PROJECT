from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException

from services.appointment import AppointmentService
from schemas.appointment import AppointmentCreate, appointments, AppointmentStatus
from schemas.doctor import doctors
from routers.doctor import set_avalilability_status

router = APIRouter()



@router.post("/book", status_code= status.HTTP_201_CREATED)
def book_appointment(payload : AppointmentCreate):
    data = AppointmentService.create_appointment(payload)
    return {
        "message" : "Appointment Successfully created",
        "data" : data
    }

@router.get("/get", status_code=status.HTTP_200_OK)
def get_appointments():
     return appointments

@router.get("/get/{id}", status_code=status.HTTP_200_OK)
def get_appointment_by_id(id : int):
      appointment = AppointmentService.process_appointment_by_id(id)
      print(appointment)
      return {
            "message" : f"Appointment with id '{id} fetched successfully",
            "data" : appointment   
      }            
    
@router.put("/process_appointments/{id}", status_code=status.HTTP_202_ACCEPTED)
def process_appointments(appointment_id : Annotated[int, Depends(AppointmentService.does_appointments_exist)]):
    
    appointment = AppointmentService.process_appointment_by_id(appointment_id)
   
    if appointment.status == AppointmentStatus.canceled.value:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This appointment was already canceled and cannot be processed."
        )
    else:
        for doctor in doctors.values():
            if doctor == appointment.doctor:
                doctor.is_available = True

        appointment.status = AppointmentStatus.completed.value

        return {
        "message": "Appointment Processed Successfully"
        }

@router.put("/cancel_appointment/{id}", status_code=status.HTTP_202_ACCEPTED)
def cancel_appointment(appointment_id : Annotated [int, Depends(AppointmentService.does_appointments_exist)]):
     
        doctors_values = list(doctors.values())
        for appointment in appointments:
            if appointment.id == appointment_id:
                for doctor in doctors_values:  
                    if doctor == appointment.doctor:
                      doctor.is_available = True
                if appointment.status == AppointmentStatus.completed.value:
                    raise HTTPException (
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="This appointment was already processed and cannot be cancelled."
                    )
                appointment.status = AppointmentStatus.canceled
                return {
                    "message" : "Appointment Cancelled Successfully"
                    }
     
     
     


        

            

    
    
    
    