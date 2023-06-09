from dto.requests.EmploymentRequest import EmploymentRequest
from dto.requests.PatientRegistrationRequest import PatientRegistrationRequest
import services.patient_service.HarmonyPatientService

from models.Hospital import Hospital

from repositories.HarmonyHospitalRepository import HarmonyHospitalRepository
from services.hospital_service.HospitalService import HospitalService
from services.medical_staff_service.HarmonyMedicalStaffService import HarmonyMedicalStaffService
from utils.Mapper import Mapper


class HarmonyHospitalService(HospitalService):

    patient_service = services.patient_service.HarmonyPatientService.HarmonyPatientService()

    hospital_repo = HarmonyHospitalRepository.get_instance()
    medical_staff_service = HarmonyMedicalStaffService()
    id_counter = 1

    def register_new_hospital(self, hospital_name):
        hospital = Hospital()

        hospital.set_hospital_name(hospital_name)

        hospital.set_hospital_id(hospital_name[0:2] + str(self.id_counter))
        self.id_counter += 1

        self.hospital_repo.save_hospital(hospital)
        return hospital.get_hospital_id()

    def employ_medical_staff(self, employment_request: EmploymentRequest):

        hospital = self.hospital_repo.find_hospital_by_id(employment_request.get_hospital_id())

        if hospital is not None:
            medical_staff = Mapper.map_medical_staff_request(employment_request, hospital)

            hospital.set_medical_staff(medical_staff.get_medical_staff_id())

            return self.medical_staff_service.employ_medical_staff(medical_staff)

    def register_patient(self, patient_registration_request: PatientRegistrationRequest):
        hospital: Hospital = self.find_hospital_by_id(patient_registration_request.get_hospital_id())
        return self.patient_service.patient_registration(patient_registration_request)

    def admit_patient(self, patient_admission_request):
        pass

    def find_hospital_by_id(self, hospital_id):
        return self.hospital_repo.find_hospital_by_id(hospital_id)

    def total_number_of_staff(self):
        return self.medical_staff_service.total_number_of_staff()


