from unittest import TestCase

from models.Patient import Patient
from repositories.PatientRepository import PatientRepository


class PatientRepositoryTest(TestCase):
    patient: Patient = Patient()
    patient_repo = PatientRepository()

    def test_save_method(self):
        self.patient.set_patient_name("Angola")
        self.patient.set_hospital_id("demo_hospital_id1234")
        patient_id = self.patient_repo.save_patient(self.patient)
        self.assertEqual(self.patient, self.patient_repo.find_patient_by_id(patient_id))
