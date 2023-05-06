from utils.id_generator import Id


class PatientRepository:
    __patients = {}

    def save_patient(self, patient):
        patient.set_patient_id(Id.patient_id(patient))
        self.__patients[patient.get_patient_id()] = patient

        return patient.get_patient_id()

    def find_patient_by_id(self, patient_id):
        return self.__patients.get(patient_id)
