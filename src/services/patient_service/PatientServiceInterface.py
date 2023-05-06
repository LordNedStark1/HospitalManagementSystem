from abc import ABC, abstractmethod


class PatientServiceInterface(ABC):

    @abstractmethod
    def register_patient(self, patient):
        pass

    def book_doctor_appointment(self, booking_doctor_appointment_request):
        pass