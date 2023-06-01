from repositories.HospitalRepositoryInterface import HospitalRepositoryInterface
from utils.id_generator import Id
import threading


class HarmonyHospitalRepository (HospitalRepositoryInterface):
    __hospitals = {}
    __instance = None
    __instance_lock = threading.Lock()
    __data_lock = threading.Lock()

    def __init__(self):
        if HarmonyHospitalRepository.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            HarmonyHospitalRepository.__instance = self

    @staticmethod
    def get_instance():
        with HarmonyHospitalRepository.__instance_lock:
            if HarmonyHospitalRepository.__instance is None:
                HarmonyHospitalRepository()
            return HarmonyHospitalRepository.__instance

    def save_hospital(self, hospital):
        with HarmonyHospitalRepository.__data_lock:
            hospital.set_hospital_id(Id.hospital_id(hospital))
            self.__hospitals[hospital.get_hospital_id()] = hospital

        return hospital.get_hospital_id()

    def find_hospital_by_id(self, hospital_id):
        with self.__data_lock:
            return self.__hospitals.get(hospital_id)
