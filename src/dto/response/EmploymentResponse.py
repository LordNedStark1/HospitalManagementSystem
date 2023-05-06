class EmploymentResponse:

    def __init__(self):
        self.__hospital_name = ""
        self.__medical_staff_id = ""
        self.__staff_name = ""
        self.__job_title = None
        self.__message = ""
        self.__specialty = ""

    def set_id(self, medical_staff_id):
        self.__medical_staff_id = medical_staff_id

    def get_id(self):
        return self.__medical_staff_id

    def set_message(self, message):
        self.__message = message

    def get_message(self):
        return self.__message

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_job_title(self):
        return self.__job_title

    def set_name(self, name):
        self.__staff_name = name

    def get_name(self):
        return self.__staff_name

    def set_specialty(self, specialty):
        self.__specialty = specialty

    def get_specialty(self):
        return self.__specialty

    def set_hospital_name(self, hospital_name):
        self.__hospital_name = hospital_name

    def get_hospital_name(self):
        return self.__hospital_name

    def to_string(self):
        return f"Welcome to {self.__hospital_name}, {self.__staff_name}, {self.__message}" \
               f" Your staff id is {self.__medical_staff_id}. You will be working with us as a {self.__job_title}"

    def __str__(self):
        return f"""
        Welcome
        {self.__staff_name}!!!
        To {self.__hospital_name}.
        {self.__message}.
        as a {self.__job_title}.
        specialized in {self.__specialty}
        Your staff id is {self.__medical_staff_id}
        """

    def __repr__(self):
        return f"""
        Welcome
        {self.__staff_name}!!!
        To {self.__hospital_name}.
        {self.__message}.
        as a {self.__job_title}.
        specialized in {self.__specialty}
        Your staff id is {self.__medical_staff_id}
        """
