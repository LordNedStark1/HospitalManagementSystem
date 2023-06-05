from abc import ABC, abstractmethod


class HospitalApi(ABC):

    @abstractmethod
    def register_new_hospital(self, hospital_name):
        pass

    @abstractmethod
    def employ_medical_staff(self, employment_request):
        pass

    @abstractmethod
    def register_patient(self, patient_registration_request):
        pass

    @abstractmethod
    def admit_patient(self, patient_admission_request):
        pass

    @abstractmethod
    def find_hospital_by_id(self, hospital_id):
        pass
