from dto.response.EmploymentResponse import EmploymentResponse
from dto.response.PatientRegistrationResponse import PatientRegistrationResponse
from models.Hospital import Hospital
from models.MedicalStaff import MedicalStaff
from models.Patient import Patient


class Mapper:

    @classmethod
    def map_medical_staff_request(cls, employment_request, hospital: Hospital):
        medical_staff = MedicalStaff()

        medical_staff.set_name(employment_request.get_name())
        medical_staff.set_job_title(employment_request.get_job_title())
        medical_staff.set_hospital_name(hospital.get_hospital_name())

        medical_staff.set_hospital_id(hospital.get_hospital_id())
        medical_staff.set_specialty(employment_request.get_specialty())
        medical_staff.set_qualification(employment_request.get_qualification())
        medical_staff.set_password(employment_request.get_password())

        return medical_staff

    @classmethod
    def map_employed_staff_response(cls, medical_staff):
        employment_response = EmploymentResponse()
        employment_response.set_id(medical_staff.get_medical_staff_id())
        employment_response.set_name(medical_staff.get_name())
        employment_response.set_job_title(medical_staff.get_job_title())
        employment_response.set_specialty(medical_staff.get_specialty())
        employment_response.set_hospital_name(medical_staff.get_hospital_name())

        employment_response.set_message("you are employed")
        return employment_response

    @classmethod
    def map_patient_registration(cls, hospital, patient_registration_request):
        patient = Patient()
        patient.set_patient_name(patient_registration_request.get_patient_name())
        patient.set_hospital_name(hospital.get_hospital_name())
        patient.set_hospital_id(hospital.get_hospital_id())

        return patient

    @classmethod
    def map_patient_registration_response(cls, patient):
        response = PatientRegistrationResponse()

        response.set_hospital_name(patient.get_hospital_name())
        response.set_hospital_id(patient.get_hospital_id())
        response.set_patient_name(patient.get_patient_name())
        response.set_patient_id(patient.get_patient_id())

        response.set_message("You health is our first priority")

        return response
