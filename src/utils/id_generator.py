class Id:
    id_counter = 3
    letters_counter = 0
    id_letter = "abcdefghijklmnopqrstuvwxwy"

    @classmethod
    def hospital_id(cls, hospital):
        cls.validate_letter_counter()
        mul = str(cls.id_counter * cls.letters_counter)
        id = hospital.get_hospital_name()[0:2] + \
              str((cls.id_counter + 12) * (cls.letters_counter + 8)) + \
             str(cls.id_counter) + "h" + cls.id_letter[cls.letters_counter] \
             + cls.id_letter[cls.letters_counter + 1]
        cls.id_counter += 1
        cls.letters_counter += 1
        return id

    @classmethod
    def medical_staff_id(cls, person_name):
        cls.validate_letter_counter()

        id = person_name.get_hospital_name()[0:2] + person_name.get_hospital_id()[3:6] \
             + str((cls.id_counter + 12) * (cls.letters_counter + 8)) + "ms" + \
             str(cls.id_counter) + cls.id_letter[cls.letters_counter]
        cls.id_counter += 1
        cls.letters_counter += 1
        return id

    @classmethod
    def patient_medical_history_id(cls):
        cls.validate_letter_counter()

        id = str((cls.id_counter + 12) * (cls.letters_counter + 8)) + \
             str(cls.id_counter) + cls.id_letter[cls.letters_counter]
        cls.id_counter += 1
        cls.letters_counter += 1
        return id

    @classmethod
    def patient_id(cls, person):
        cls.validate_letter_counter()

        id = person.get_hospital_name()[0:2] + person.get_hospital_id()[3:6] \
             + person.get_hospital_id()[-1] + "p" + \
             str((cls.id_counter + 12) * (cls.letters_counter + 8)) + \
             str(cls.id_counter) + cls.id_letter[cls.letters_counter]
        cls.id_counter += 1
        cls.letters_counter += 1
        return id

    @classmethod
    def validate_letter_counter(cls):
        if cls.letters_counter == 24:
            cls.letters_counter = 0
