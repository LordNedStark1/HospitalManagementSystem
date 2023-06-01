from abc import abstractmethod, ABC


class HospitalRepositoryInterface(ABC):

    @abstractmethod
    def save_hospital(self, hospital):
        pass

    @abstractmethod
    def find_hospital_by_id(self, hospital_id):
        pass
