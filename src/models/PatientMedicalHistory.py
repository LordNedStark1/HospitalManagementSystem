
class PatientMedicalHistory:
    def __init__(self):
        self.__patient_histories = []
        self.__patient_medical_history_id = ""

    def set_patient_medical_history_id(self, id):
        self.__patient_medical_history_id = id

    def get_patient_medical_history_id(self):
        return self.__patient_medical_history_id

    def add_new_history(self, history):
        self.__patient_histories.append(history)

    def get_patient_medical_history(self):
        return self.__patient_histories
