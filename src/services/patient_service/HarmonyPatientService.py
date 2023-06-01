from dto.requests.PatientRegistrationRequest import PatientRegistrationRequest
from models.Hospital import Hospital

from repositories.PatientRepository import PatientRepository
from services.PatientMedicalHistoryService.HarmonyPatientMedicalHistory import HarmonyPatientMedicalHistory

from services.patient_service.PatientService import PatientService
from utils.Mapper import Mapper


class HarmonyPatientService(PatientService):
    patient_repo = PatientRepository.get_instance()
    harmony_patient_medical_history = HarmonyPatientMedicalHistory()

    def register_patient(self, patient_registration_request: PatientRegistrationRequest):
        from services.hospital_service.HarmonyHospitalService import HarmonyHospitalService
        hospital_service = HarmonyHospitalService()

        hospital: Hospital = hospital_service.find_hospital_by_id(patient_registration_request.get_hospital_id())

        if hospital is not None:
            patient = Mapper.map_patient_registration(hospital, patient_registration_request)
            patient_medical_history_id = self.harmony_patient_medical_history.creat_new_patient_medical_history()

            patient.set_patient_medical_history_id(patient_medical_history_id)
            self.patient_repo.save_patient(patient)

            return Mapper.map_patient_registration_response(patient)

    def book_doctor_appointment(self, booking_doctor_appointment_request):
        pass
