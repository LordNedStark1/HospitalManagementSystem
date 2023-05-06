from abc import ABC, abstractmethod


class MedicalStaffServiceInterface(ABC):

    @abstractmethod
    def employ_medical_staff(self, employment_request):
        pass