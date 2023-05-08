from utils.id_generator import Id
import threading


class PatientRepository:
    __patients = {}
    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        if PatientRepository.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            PatientRepository.__instance = self

    @staticmethod
    def get_instance():
        with PatientRepository.__lock:
            if PatientRepository.__instance is None:
                PatientRepository()
            return PatientRepository.__instance

    def save_patient(self, patient):
        patient.set_patient_id(Id.patient_id(patient))
        self.__patients[patient.get_patient_id()] = patient

        return patient.get_patient_id()

    def find_patient_by_id(self, patient_id):
        return self.__patients.get(patient_id)
