from unittest import TestCase

from models.DoctorReport import DoctorReport
from models.PatientMedicalHistory import PatientMedicalHistory


class PatientMedicalHistoryTest(TestCase):
    def setUp(self) -> None:
        self.patient_history = PatientMedicalHistory()
        self.appointment = DoctorReport()
        self.appointment.set_patient_name("John")
        self.appointment.set_patient_illment("code headache")
        self.appointment.set_doctor_name("Mark")
        self.appointment.set_doctor_statement("He needs to really rest if you ask me")

    def test_add_history(self):
        self.patient_history.add_new_history("string demo")
        self.patient_history.add_new_history(3)
        self.patient_history.add_new_history("second")
        self.patient_history.add_new_history(self.appointment)
        history = self.patient_history.get_patient_medical_history()
        self.assertEqual("John", history[3].get_patient_name())
        self.assertEqual(3, history[1])

