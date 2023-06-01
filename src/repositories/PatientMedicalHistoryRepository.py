from models.PatientMedicalHistory import PatientMedicalHistory
from repositories.PatientMEdicalHistoryRepositoryInterface import PatientMedicalHistoryRepositoryInterface
from utils.id_generator import Id


class PatientMedicalHistoryRepository (PatientMedicalHistoryRepositoryInterface):
    __patient_medical_history = {}

    def save_patient_medical_history(self, patient_medical_history: PatientMedicalHistory):
        patient_medical_history.set_patient_medical_history_id(Id.patient_medical_history_id())
        self.__patient_medical_history[patient_medical_history.get_patient_medical_history_id()] = \
            patient_medical_history
        return patient_medical_history.get_patient_medical_history_id()

    def find_patient_medical_history_by_id(self, patient_medical_history_id) -> PatientMedicalHistory:
        return self.__patient_medical_history.get(patient_medical_history_id)