from schema.doctor import doctors

class DoctorHelpers:

    @staticmethod
    def get_doctor_by_id(doctor_id: int):
        for doctor in doctors:
            if doctor.id == doctor_id:
                return doctor
        return None