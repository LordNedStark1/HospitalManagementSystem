from dto.requests.PatientRegistrationRequest import PatientRegistrationRequest
from models.Hospital import Hospital
from repositories.HospitalRepository import HospitalRepositoryImpl

from repositories.PatientRepository import PatientRepository
from services.PatientMedicalHistoryService.PatientMedicalHistoryImpl import PatientMedicalHistoryImpl
from services.hospital_service.HospitalServiceImpl import HospitalServiceImpl

from services.patient_service.PatientServiceInterface import PatientServiceInterface
from utils.Mapper import Mapper


class PatientServiceImpl(PatientServiceInterface):
    patient_repo = PatientRepository()
    patient_medical_history_impl = PatientMedicalHistoryImpl()
    hospital_repo = HospitalRepositoryImpl.get_instance()
    hospital_service = HospitalServiceImpl(hospital_repo)

    def register_patient(self, patient_registration_request: PatientRegistrationRequest):
        hospital: Hospital = self.hospital_service.find_hospital_by_id(patient_registration_request.get_hospital_id())
        if hospital is not None:

            patient = Mapper.map_patient_registration(hospital, patient_registration_request)
            patient_medical_history_id = self.patient_medical_history_impl.creat_new_patient_medical_history()

            patient.set_patient_medical_history_id(patient_medical_history_id)
            self.patient_repo.save_patient(patient)

            return Mapper.map_patient_registration_response(patient)

    def book_doctor_appointment(self, booking_doctor_appointment_request):
        pass
