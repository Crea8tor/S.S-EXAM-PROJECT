from fastapi import HTTPException, status, Depends

from schema.appointment import Appointment, appointments, AppointmentCreate, AppointmentStatus
from schema.patient import patients
from schema.doctor import doctors,Doctor,DoctorStatus

class AppointmentService:
     

 
     @staticmethod      
     def check_availability(payload: Doctor):
        doc_status = payload.is_available
        for stat in doc_status:
            doctor: Doctor = doctors.get(str(stat))
            if doctor.is_available == False :
                # logger.warning("Product is no more available")
             raise HTTPException(status_code=400, detail='doctor is unavailable')
            # product.quantity_available -= 1
        return payload





     @staticmethod
     #book an Appointment
     def create_appointment(payload: AppointmentCreate = Depends(check_availability)):
        appointment_id = len(appointments) + 1
        # current_patient = AppointmentService.patient_availability(payload)
        patient: int = payload.patient
        appointment = Appointment(
            id = appointment_id,
            patient = patient,
            doctor = doctors[0],
            date = payload.date,
            status = AppointmentStatus.active.value
        )

        appointments.append(appointment)
        return appointment
     
     @staticmethod
     def does_appointments_exist(appointment_id : int):
         
         appointment_ids = [appointment.id for appointment in appointments]
         if appointment_id not in appointment_ids:
            raise HTTPException(
                 status_code= status.HTTP_404_NOT_FOUND,
                 detail= f"Appointment with id '{appointment_id}' not found"
             )
         return appointment_id
     
     @staticmethod
     def return_appointed_doctor(appointment_id : int):
         for doctor in doctors:
             if appointment_id == doctor:
                 return doctor
             

     @staticmethod
     #get appointment by id
     def get_appointment_by_id(id : int):
         curr_appointment = None

         for appointment in appointments:
             if appointment.id == id:
                 curr_appointment = appointment
                 break
         if not curr_appointment:
                 raise HTTPException(
                     status_code=status.HTTP_404_NOT_FOUND,
                     detail= f"Appointment with id '{id}' not found"
                 )

         return curr_appointment
    
    
     
     
    #  @staticmethod
    #  def delete_appointment(appointment_id):
    #    appointments: Appointment  = AppointmentHelpers.get_appointment_by_id(appointment_id)
    #  if not appointment:
    #      raise HTTPException(detail='Appointment not found', status_code=404)
    #     del appointments[appointment_id]   

             
 

        
         
  
             

       

         
        

















# from fastapi import HTTPException

# from schema.appointment import AppointmentsCreate, Appointments, appointments
# from schema.patient import Patients, patients
# from schema.doctor import Doctors, doctors
# from utils.appointment import AppointmentHelpers

# class AppointmentService:

#     @staticmethod
#     def create_appointment(payload: AppointmentsCreate):
#         id = len(appointments)
#         patient: Patients = patients[payload.patient]
#         doctor: Doctors = doctors[payload.doctor]
#         appointment = Appointments(
#             id=id,
#             patient=patient,
#             doctor=payload.doctor,
#             date=payload.date,
#         )
#         appointments.append(appointment)
#         return appointment
    




#     @staticmethod
#     def get_appointment_by_id(appointment_id: int):
#         appointment = AppointmentHelpers.get_appointment_by_id(appointment_id)
#         if not appointment:
#             raise HTTPException(detail='Appointment not found', status_code=404)
#         return appointment
    
   