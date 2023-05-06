from unittest import TestCase

from models.PatientMedicalHistory import PatientMedicalHistory
from repositories.PatientMedicalHistoryRepository import PatientMedicalHistoryRepository


class PatientMedicalHistoryRepositoryTest(TestCase):
    patient_medical_history_repository = PatientMedicalHistoryRepository()
    patient_medical_history = PatientMedicalHistory()

    def test_save_method(self):
       id = self.patient_medical_history_repository.save_patient_medical_history(self.patient_medical_history)
       retrived = self.patient_medical_history_repository.find_patient_medical_history_by_id(id).get_patient_medical_history_id()
       self.assertEqual(id, retrived )
