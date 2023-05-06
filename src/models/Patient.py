class Patient:
    def __init__(self):
        self.__patient_id = ""
        self.__patient_name = ""
        self.__hospital_id = ""
        self.__hospital_name = ""
        self.__doctors_report = ""
        self.__patient_medical_history_id = ""
        self.__doctors_assigned_to = []

    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id

    def get_patient_id(self):
        return self.__patient_id

    def set_hospital_name(self, hospital_name):
        self.__hospital_name = hospital_name

    def get_hospital_name(self):
        return self.__hospital_name

    def set_hospital_id(self, hospital_id):
        self.__hospital_id = hospital_id

    def get_hospital_id(self):
        return self.__hospital_id

    def set_patient_name(self, name):
        self.__patient_name = name

    def get_patient_name(self):
        return self.__patient_name

    def set_doctors_report(self, doctors_report):
        self.__doctors_report = doctors_report

    def get_doctors_report(self):
        return self.__doctors_report

    def set_patient_medical_history_id(self, patient_history):
        self.__patient_medical_history_id = patient_history

    def get_patient_medical_history_id(self):
        return self.__patient_medical_history_id
