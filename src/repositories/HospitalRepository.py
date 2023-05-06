from utils.id_generator import Id


class HospitalRepositoryImpl:
    __hospitals = {}

    def save_hospital(self, hospital):
        hospital.set_hospital_id(Id.hospital_id(hospital))
        self.__hospitals[hospital.get_hospital_id()] = hospital

        return hospital.get_hospital_id()

    def find_hospital_by_id(self, hospital_id):
        return self.__hospitals.get(hospital_id)

