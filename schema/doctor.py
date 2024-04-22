from pydantic import BaseModel
from enum import Enum
from typing import Dict

class DoctorStatus(Enum):
    is_available = True
    unavailable = False
   

class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: bool= DoctorStatus.is_available._value_

class DoctorCreateEdit(BaseModel):
    name: str
    specialization: str
    phone: str
    is_available: bool= DoctorStatus.is_available._value_




doctors: dict[int, Doctor] = {
     0: Doctor(
        id=0, name='patient 0', specialization='Doctor', phone='0800', is_available= False
     ),
     1: Doctor(
        id=1, name='emma',  specialization='Surgeon', phone='0803', is_available= True
     ),
     2: Doctor(
        id=2, name='titi',   specialization='nurse', phone='0805', is_available= True
     ), 
}

