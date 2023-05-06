from models.Hospital import Hospital
from repositories.HospitalRepository import HospitalRepositoryImpl

hospital_repo: HospitalRepositoryImpl = HospitalRepositoryImpl.get_instance()
hospital_repo2 = HospitalRepositoryImpl.get_instance()
hospital = Hospital()
hospital2 = Hospital()

first_id = hospital_repo.save_hospital(hospital)
first_id2 = hospital_repo2.save_hospital(hospital)
first_id3 = hospital_repo2.save_hospital(hospital2)

found1 = hospital_repo.find_hospital_by_id(first_id3)
print(hospital2 == found1)