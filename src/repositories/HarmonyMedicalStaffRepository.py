from models.MedicalStaff import MedicalStaff
from repositories.MedicalStaffRepositoryInterface import MedicalStaffRepositoryInterface
from utils.id_generator import Id


class HarmonyMedicalStaffRepository(MedicalStaffRepositoryInterface):
    medical_staffs = {}

    def save(self, medical_staff: MedicalStaff):
        medical_staff.set_medical_staff_id(Id.medical_staff_id(medical_staff))

        self.medical_staffs[medical_staff.get_medical_staff_id()] = medical_staff

    def total_number_of_staff(self):
        return len(self.medical_staffs)

    def find_staff_by_id(self, staff_id):
        return self.medical_staffs.get(staff_id)