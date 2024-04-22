from fastapi import FastAPI
from fastapi import status

from routers.patient import patient_router
from routers.appointment import appointment_router
from routers.doctor import doctor_router

app = FastAPI()

app.include_router(router=patient_router, prefix='/patients', tags=['patients'])
app.include_router(router=appointment_router, prefix='/patients', tags=['appointments'])
app.include_router(router=doctor_router, prefix='/doctors', tags=['doctors'])

@app.get("/Home", status_code=status.HTTP_200_OK, tags=["Home Page"])
def index():
    return "Welcome to Ace Medical Appointment Api"