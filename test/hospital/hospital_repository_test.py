from unittest import TestCase

from models.Hospital import Hospital
from repositories.HospitalRepository import HospitalRepositoryImpl


class HospitalRepositoryTest(TestCase):
    hospital_repo = HospitalRepositoryImpl()

    def test_save_method(self):
        hospital = Hospital()

        hospital.set_hospital_name("Unilag Hospital")
        hospital_id = self.hospital_repo.save_hospital(hospital)
        print(hospital_id)

        self.assertEquals(hospital, self.hospital_repo.find_hospital_by_id(hospital_id))
