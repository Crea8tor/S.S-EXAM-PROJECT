from pydantic import BaseModel

class Patient(BaseModel):
    id : int
    name : str
    age : int
    gender : str
    weight : float
    height : float
    phone : str

class PatientCreate(BaseModel):
    name : str
    age : int
    gender : str
    weight : float
    height : float
    phone : str


patients:dict[int,Patient] = {
   1 : Patient(
       id = 1,
       name = "banjo",
       age = 25,
       gender = "m",
       weight = 6.0,
       height = 4.5,
       phone = "09094848484"
   ),
   2 : Patient(
       id = 2,
       name = "tunji",
       age = 47,
       gender = "m",
       weight= 70.9,
       height = 5.5,
       phone = "09084848423"
   )
}