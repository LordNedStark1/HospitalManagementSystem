from abc import ABC, abstractmethod


class PatientServiceInterface(ABC):

    @abstractmethod
    def register_patient(self, patient, hospital):
        pass