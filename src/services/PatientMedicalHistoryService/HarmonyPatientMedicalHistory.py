from models.PatientMedicalHistory import PatientMedicalHistory
from repositories.PatientMedicalHistoryRepository import PatientMedicalHistoryRepository


class HarmonyPatientMedicalHistory:
    patient_medical_history_repo = PatientMedicalHistoryRepository()

    def creat_new_patient_medical_history(self):
        patient_medical_history = PatientMedicalHistory()
        return self.patient_medical_history_repo.save_patient_medical_history(patient_medical_history)

    def find_patient_medical_history_by_id(self, patient_medical_history_id):
        return self.patient_medical_history_repo.find_patient_medical_history_by_id(patient_medical_history_id)

    def add_medical_history(self, patient_medical_history_id, new_history):
        medical_history = self.patient_medical_history_repo.find_patient_medical_history_by_id(
            patient_medical_history_id)
        medical_history.add_new_history(new_history)
        self.patient_medical_history_repo.save_patient_medical_history(new_history)
        return "History added"
