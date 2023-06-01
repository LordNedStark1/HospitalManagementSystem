from abc import ABC, abstractmethod

from models.PatientMedicalHistory import PatientMedicalHistory


class PatientMedicalHistoryRepositoryInterface(ABC):
    @abstractmethod
    def save_patient_medical_history(self, patient_medical_history: PatientMedicalHistory):
       pass

    @abstractmethod
    def find_patient_medical_history_by_id(self, patient_medical_history_id) -> PatientMedicalHistory:
        pass