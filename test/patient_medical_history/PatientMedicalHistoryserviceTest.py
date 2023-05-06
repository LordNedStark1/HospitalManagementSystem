from unittest import TestCase

from services.PatientMedicalHistoryService.PatientMedicalHistoryImpl import PatientMedicalHistoryImpl


class PatientMedicalHistoryServiceTest(TestCase):
    def setUp(self) -> None:
        self.patient_medical_history_service = PatientMedicalHistoryImpl()

    def test_creat_new_patient_medical_history(self):
        history_id = self.patient_medical_history_service.creat_new_patient_medical_history()
        self.assertEqual(history_id, self.patient_medical_history_service.find_patient_medical_history_by_id(history_id).get_patient_medical_history_id())

    def test_add_patient_medical_history(self):
        pass