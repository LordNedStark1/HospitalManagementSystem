from unittest import TestCase

from dto.requests.EmploymentRequest import EmploymentRequest
from dto.requests.PatientRegistrationRequest import PatientRegistrationRequest
from dto.response.EmploymentResponse import EmploymentResponse
from dto.response.PatientRegistrationResponse import PatientRegistrationResponse
from models.Hospital import Hospital
from repositories.HospitalRepository import HospitalRepositoryImpl
from services.hospital_service.HarmonyHospitalService import HarmonyHospitalServiceImpl


class HospitalServiceTest(TestCase):
    def setUp(self) -> None:

        self.hospital_service = HarmonyHospitalServiceImpl()

        self.employment_request = EmploymentRequest()
        self.patient_registration_request = PatientRegistrationRequest()

        self.hospital_id = self.hospital_service.register_new_hospital("unilag Hospital")
        self.hospital: Hospital = self.hospital_service.find_hospital_by_id(self.hospital_id)

        self.__employment_request_method()
        self.employment_response: EmploymentResponse = self.hospital_service.employ_medical_staff(
            self.employment_request)

        self.__patient_registration_request_method()
        self.patient_registration_response: PatientRegistrationResponse = self.hospital_service \
            .register_patient(self.patient_registration_request)

    def __patient_registration_request_method(self):
        self.patient_registration_request.set_patient_name("Musa Aliyu")
        self.patient_registration_request.set_hospital_id(self.hospital_id)
        self.patient_registration_request.set_hospital_name(self.hospital.get_hospital_name())

    def __employment_request_method(self):
        self.employment_request.set_job_title("Doctor")
        self.employment_request.set_name("Elder Boch ")
        self.employment_request.set_password("elder24@_boch")
        self.employment_request.set_hospital_id(self.hospital_id)
        self.employment_request.set_qualification("Msc. in Medicine")
        self.employment_request.set_school_of_learning("UNN")
        self.employment_request.set_years_of_practice(4)
        self.employment_request.set_specialty("Cardiovascular")

    def test_register_new_hospital_method(self):
        hospital_id = self.hospital_service.register_new_hospital("Unizik Hospital")
        hospital: Hospital = self.hospital_service.find_hospital_by_id(hospital_id)
        self.assertEqual("Unizik Hospital", hospital.get_hospital_name())

    def test_employ_medical_staff_method(self):
        self.employment_request.set_job_title("Doctor")
        self.employment_request.set_name("Mark John")
        self.employment_request.set_password("mark94@_john")
        self.employment_request.set_hospital_id(self.hospital_id)
        self.employment_request.set_qualification("Bsc in Medicine")
        self.employment_request.set_school_of_learning("Unizik")
        self.employment_request.set_years_of_practice(2)
        self.employment_request.set_specialty("physiotherapy")
        hospital: Hospital = self.hospital_service.find_hospital_by_id(self.hospital_id)
        employment_response: EmploymentResponse = self.hospital_service.employ_medical_staff(self.employment_request)

        message = "you are employed"
        response = f"Welcome to {hospital.get_hospital_name()}, Mark John, {message}" \
                   f" Your staff id is {employment_response.get_id()}. You will be working with us as a Doctor"

        self.assertEqual(response, employment_response.to_string())
        self.assertEqual(2, self.hospital_service.total_number_of_staff())

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
        # print(self.patient_registration_response.to_string())
        self.assertEqual(response, self.patient_registration_response.to_string())
