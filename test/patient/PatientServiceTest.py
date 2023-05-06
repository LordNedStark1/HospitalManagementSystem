from unittest import TestCase

from dto.requests.PatientRegistrationRequest import PatientRegistrationRequest
from dto.response.PatientRegistrationResponse import PatientRegistrationResponse
from models.Hospital import Hospital
from repositories.HospitalRepository import HospitalRepositoryImpl
from services.hospital_service.HospitalServiceImpl import HospitalServiceImpl
from services.patient_service.PatientServiceImpl import PatientServiceImpl


class PatientServiceTest(TestCase):

    def setUp(self) -> None:
        self.hospital_repo = HospitalRepositoryImpl()
        self.hospital_service = HospitalServiceImpl(self.hospital_repo)
        self.patiemt_service = PatientServiceImpl()

        self.patient_registration_request = PatientRegistrationRequest()
        self.hospital_id = self.hospital_service.register_new_hospital("unilag Hospital")
        self.hospital: Hospital = self.hospital_service.find_hospital_by_id(self.hospital_id)

    def __patient_registration_request_method(self):
        self.patient_registration_request.set_patient_name("Musa Aliyu")
        self.patient_registration_request.set_hospital_id(self.hospital_id)
        self.patient_registration_request.set_hospital_name(self.hospital.get_hospital_name())

    def test_register_patient_method(self):
        self.patient_registration_request.set_patient_name("Musa Aliyu")
        self.patient_registration_request.set_hospital_id(self.hospital_id)
        self.patient_registration_request.set_hospital_name(self.hospital.get_hospital_name())
        self.patient_registration_response: PatientRegistrationResponse = \
            self.hospital_service.register_patient(self.patient_registration_request)

        message = "You health is our first priority"
        response = f"Welcome to {self.hospital.get_hospital_name()} {self.patient_registration_request.get_patient_name()}." \
                   f" Your patient id number is {self.patient_registration_response.get_patient_id()}." \
                   f"{message}."

        self.assertEqual(response, self.patient_registration_response.to_string())
