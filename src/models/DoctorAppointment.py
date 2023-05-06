from datetime import datetime


class DoctorAppointment:
    def __init__(self):
        self.__doctor_id = ""
        self.__doctor_name = ""
        self.__patient_id = ""
        self.__patient_name = ""
        self.__illment = ""
        self.date = datetime
        self.__doctor_statement = ""
        self.__doctor_prescriptions = []
        self.__attachments = []

    def set_doctor_id(self, medical_staff_id):
        self.__doctor_id = medical_staff_id

    def get_doctor_id(self):
        return self.__doctor_id

    def set_doctor_name(self, medical_staff_name):
        self.__doctor_name = medical_staff_name

    def get_doctor_name(self):
        return self.__doctor_name

    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id

    def get_patient_id(self):
        return self.__patient_id

    def set_patient_name(self, patient_name):
        self.__patient_name = patient_name

    def get_patient_name(self):
        return self.__patient_name

    def set_patient_illment(self, illment):
        self.__illment = illment

    def get_patient_illment(self):
        return self.__illment

    def set_doctor_statement(self, doctor_statement):
        self.__doctor_statement = doctor_statement

    def get_doctor_statement(self):
        return self.__doctor_statement

    def set_doctor_prescriptions(self, prescriptions):
        self.__doctor_prescriptions.append(prescriptions)

    def get_doctor_prescriptions(self):
        return self.__doctor_prescriptions

    def set_attachments(self, attachment):
        self.__attachments.append(attachment)

    def get_attachments(self):
        return self.__attachments
