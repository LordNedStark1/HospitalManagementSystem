class MedicalStaff:
    def __init__(self):
        self.__medical_staff_id = ""
        self.__hospital_id = ""
        self.__hospital_name = ""
        self.__name = ""
        self.__job_title = None
        self.__school_of_learning = ""
        self.__qualification = ""
        self.__specialty = ""
        self.__years_of_practice = ""
        self.__patients_assigned_to = []
        self.__password = ""

    def set_medical_staff_id(self, medical_staff_id):
        self.__medical_staff_id = medical_staff_id

    def get_medical_staff_id(self):
        return self.__medical_staff_id

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_job_title(self):
        return self.__job_title

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_school_of_learning(self, school_of_learning):
        self.__school_of_learning = school_of_learning

    def get_school_of_learning(self):
        return self.__school_of_learning

    def set_qualification(self, qualification):
        self.__qualification = qualification

    def get_qualification(self):
        return self.__qualification

    def set_specialty(self, specialty):
        self.__specialty = specialty

    def get_specialty(self):
        return self.__specialty

    def set_years_of_practice(self, years_of_practice):
        self.__years_of_practice = years_of_practice

    def get_years_of_practice(self):
        return self.__years_of_practice

    def set_patients_assigned_to(self, patients_assigned_to):
        self.__patients_assigned_to.append(patients_assigned_to)

    def get_patients_assigned_to(self):
        return self.__patients_assigned_to

    def set_hospital_name(self, hospital_name):
        self.__hospital_name = hospital_name

    def get_hospital_name(self):
        return self.__hospital_name

    def set_hospital_id(self, hospital_id):
        self.__hospital_id = hospital_id

    def get_hospital_id(self):
        return self.__hospital_id

    def __str__(self):
        return f"""
        {self.__name}
        {self.__medical_staff_id }
        {self.__hospital_id}
        {self.__hospital_name}
        {self.__job_title }
        """