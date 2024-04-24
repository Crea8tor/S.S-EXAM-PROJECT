from pydantic import BaseModel

class Doctor(BaseModel):
    id : int
    name: str
    specialization: str
    phone : str
    is_available: bool = True

class DoctorCreate(BaseModel):
    name : str
    specialization: str
    phone : str
    is_available: bool = True




doctors:dict[int,Doctor] = {
    1 : Doctor(
        id = "1",
        name = "titi",
        specialization = "dentist",
        phone = "0905848484",
        is_available = True
    ),
    2 : Doctor(
        id = "2",
        name = "kemi",
        specialization = "doctor of heart",
        phone = "80857573473",
        is_available = False
    ),
    3 : Doctor(
        id = "3",
        name = "adebayo",
        specialization = "surgeon",
        phone = "0900838300",
        is_available = True
    )
}