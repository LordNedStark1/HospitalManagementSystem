class PatientRegistrationResponse:
    def __init__(self):
        self.__patient_id = ""
        self.__patient_name = ""
        self.__hospital_id = ""
        self.__hospital_name = ""
        self.__message = ""

    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id

    def set_message(self, message):
        self.__message = message

    def get_message(self):
        return self.__message

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

    def to_string(self):
        return f"Welcome to {self.__hospital_name} {self.__patient_name}." \
                   f" Your patient id number is {self.__patient_id}." \
                   f"{self.__message}."

    def __str__(self):
        return f"Welcome to {self.__hospital_name} {self.__patient_name}." \
            f" Your patient id number is {self.__patient_id}." \
            f"{self.__message}."

    def __repr__(self):
        return f"Welcome to {self.__hospital_name} {self.__patient_name}." \
            f" Your patient id number is {self.__patient_id}." \
            f"{self.__message}."