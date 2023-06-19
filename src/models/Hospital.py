class Hospital:
    def __init__(self):
        self.__hospital_head = None
        self.__hospital_name = ""
        self.__hospital_id = ""
        self.__hospital_id = ""
        self.__hospital_name = ""
        self.__medical_staffs_id = []
        self.__patients_id = []

    def set_hospital_id(self, hospital_id):
        self.__hospital_id = hospital_id

    def get_hospital_id(self):
        return self.__hospital_id

    def set_hospital_name(self, hospital_name):
        self.__hospital_name = hospital_name

    def get_hospital_name(self):
        return self.__hospital_name

    def get_doctor_name(self):
        return self.__hospital_name

    def set_medical_staff(self, medical_staff_id):
        self.__medical_staffs_id.append(medical_staff_id)

    def get_medical_staffs(self):
        return self.__medical_staffs_id

    def set_patient(self, patient_id):
        self.__patients_id.append(patient_id)

    def get_patients(self):
        return self.__patients_id

    def set_hospital_head(self, hospital_head):
        self.__hospital_head = hospital_head

    def get_hospital_head(self):
        return self.__hospital_head