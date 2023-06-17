from unittest import TestCase

from dto.requests.EmploymentRequest import EmploymentRequest
from dto.response.EmploymentResponse import EmploymentResponse
from models.Hospital import Hospital
from services.hospital_service.HarmonyHospitalService import HarmonyHospitalService
from services.medical_staff_service.HarmonyMedicalStaffService import HarmonyMedicalStaffService


class MedicalStaffServiceTest(TestCase):
    def setUp(self) -> None:
        self.medical_staff_service = HarmonyMedicalStaffService()
        self.hospital_service = HarmonyHospitalService()
        self.hospital_id = self.hospital_service.register_new_hospital("unilag Hospital")
        self.employment_request = EmploymentRequest()
        self.__employment_request_method()

    def __employment_request_method(self):
        self.employment_request.set_job_title("Doctor")
        self.employment_request.set_name("Elder Boch ")
        self.employment_request.set_password("elder24@_boch")
        self.employment_request.set_hospital_id(self.hospital_id)
        self.employment_request.set_qualification("Msc. in Medicine")
        self.employment_request.set_school_of_learning("UNN")
        self.employment_request.set_years_of_practice(4)
        self.employment_request.set_specialty("Cardiovascular")

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
        self.assertEqual(1, self.hospital_service.total_number_of_staff())

        staff = self.medical_staff_service.find_staff_by_id(employment_response.get_id())
        self.assertEqual("Mark John",staff.get_name())

        def test_medical_staff_can_view_all_appointments(self):
            pass
