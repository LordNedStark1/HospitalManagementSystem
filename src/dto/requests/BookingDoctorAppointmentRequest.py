class BookingDoctorAppointmentRequest:
    def __init__(self):
        self.__patient_id = ""
        self.__patient_condition = ""

    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id

    def get_patient_id(self):
        return self.__patient_id

    def set_patient_condition(self, patient_condition):
        self.__patient_condition = patient_condition

    def get_patient_condition(self):
        return self.__patient_condition
