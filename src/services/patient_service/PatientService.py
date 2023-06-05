from abc import ABC, abstractmethod


class PatientService(ABC):

    @abstractmethod
    def patient_registration(self, patient):
        pass

    def book_doctor_appointment(self, booking_doctor_appointment_request):
        pass