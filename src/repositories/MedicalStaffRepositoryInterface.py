from abc import abstractmethod, ABC

from models.MedicalStaff import MedicalStaff


class MedicalStaffRepositoryInterface(ABC):
    @abstractmethod
    def save(self, medical_staff: MedicalStaff):
        pass

    @abstractmethod
    def total_number_of_staff(self):
        pass

    @abstractmethod
    def find_staff_by_id(self, staff_id):
        pass