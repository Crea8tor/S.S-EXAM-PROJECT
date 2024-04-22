from fastapi import HTTPException,status
from schema.patient import patients, Patient, PatientCreateEdit

class PatientSerivce:

   

    @staticmethod
    #get all patients 
    def get_patients():
        data = []
        for patient in patients:
            data.append(patients[patient])
        return {
            "message": "Successful",
            "data" : data
        }
    
    @staticmethod
    def get_patient_by_id(patient_id:int):
      
       curr_patient = None
     
       for patient in patients:
        if patient.id == patient_id:
            curr_patient = patient
            break
          
       if not  curr_patient:  
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= f"Patient  not found"
            )
       return curr_patient
     
    
    
    @staticmethod
    def create_patient(patient_data: PatientCreateEdit):
     id = len(patients) +1
     patient = Patient(
            id=id,
            **patient_data.model_dump()
        )
     patients[id] = patient
     return patient
    
    
    
   
    
    @staticmethod
    def edit_patient(patient_id: int,payload: PatientCreateEdit):
     curr_patient = None
    # get the customer
     for patient in patients:
        if patient.id == patient_id :
            curr_patient = patient
            break

     if not curr_patient:
        raise HTTPException(status_code=404, detail="patient not found")
     curr_patient.name = payload.name
     curr_patient.age = payload.age
     curr_patient.sex = payload.sex
     curr_patient.weight = payload.weight
     curr_patient.height = payload.height
     curr_patient.phone = payload.phone
    
     return {'message': 'patient edited successfully', 'data': curr_patient}


    @staticmethod
    def delete_patient(patient_id: int):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(detail='Patient not found.', status_code=404)
        del patients[patient_id]
