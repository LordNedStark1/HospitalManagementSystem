from repositories.MedicalStaffRepository import MedicalStaffRepository
from services.medical_staff_service.MedicalStaffServiceInterface import MedicalStaffServiceInterface
from utils.Mapper import Mapper


class MedicalStaffServiceImpl(MedicalStaffServiceInterface):
    medical_staff_repo = MedicalStaffRepository()

    def employ_medical_staff(self, medical_staff):
        self.medical_staff_repo.save(medical_staff)
        return Mapper.map_employed_staff_response(medical_staff)

    def find_staff_by_id(self, staff_id):
        return self.medical_staff_repo.find_staff_by_id(staff_id)

    def total_number_of_staff(self):
        return self.medical_staff_repo.total_number_of_staff()
