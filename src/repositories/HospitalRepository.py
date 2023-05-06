from utils.id_generator import Id


class HospitalRepositoryImpl:
    __hospitals = {}
    __instance = None

    def __init__(self):
        if HospitalRepositoryImpl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            HospitalRepositoryImpl.__instance = self

    @staticmethod
    def get_instance():
        if HospitalRepositoryImpl.__instance is None:
            HospitalRepositoryImpl()
        return HospitalRepositoryImpl.__instance

    def save_hospital(self, hospital):
        hospital.set_hospital_id(Id.hospital_id(hospital))
        self.__hospitals[hospital.get_hospital_id()] = hospital

        return hospital.get_hospital_id()

    def find_hospital_by_id(self, hospital_id):
        return self.__hospitals.get(hospital_id)
