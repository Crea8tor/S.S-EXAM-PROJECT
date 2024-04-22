from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str

class PatientCreateEdit(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str


patients: dict[int, Patient] = {
     0: Patient(
        id=0, name='patient 0', age=30, sex= 'm' , weight= 2.0, height= 4.7, phone='0800'
     ),
      1: Patient(
        id=0, name='patient 1', age=20, sex= 'm' , weight= 4.6, height= 6.7, phone='0803'
     ),
      2: Patient(
        id=0, name='patient 2', age=39, sex= 'f' , weight= 1.6, height= 7.7, phone='0805'
     ), 
}



