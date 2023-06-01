from unittest import TestCase
import typing

from models.Hospital import Hospital
from repositories.HarmonyHospitalRepository import HarmonyHospitalRepository


class HospitalRepositoryTest(TestCase):
    hospital_repo = HarmonyHospitalRepository()

    def test_save_method(self):
        hospital = Hospital()

        hospital.set_hospital_name("Unilag Hospital")
        hospital_id = self.hospital_repo.save_hospital(hospital)

        self.assertEquals(hospital, self.hospital_repo.find_hospital_by_id(hospital_id))
