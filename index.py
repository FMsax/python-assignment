class Patient:
    def __init__(self, id, name, age, sex, weight, height, phone):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.weight_in_kg = weight
        self.height_in_cm = height
        self.phone = phone

class Doctor:
    def __init__(self, id, name, specialization, phone, is_available=True):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.phone = phone
        self.is_available = is_available
        self.appointments = []

class Appointment:
    def __init__(self, id, patient, doctor, date):
        self.id = id
        self.patient = patient
        self.doctor = doctor
        self.date = date

# Initialize some sample data
patients = [Patient(1, "Feranmi", 30, "Male", 70, 170, "09092139148")]
doctors = [Doctor(1, "Dr. Seyi", "General Practitioner", "09087654321")]
appointments = []

def create_patient(name, age, sex, weight, height, phone):
    new_patient = Patient(len(patients) + 1, name, age, sex, weight, height, phone)
    patients.append(new_patient)
    return new_patient

def create_doctor(name, specialization, phone):
    new_doctor = Doctor(len(doctors) + 1, name, specialization, phone)
    doctors.append(new_doctor)
    return new_doctor

def create_appointment(patient_id, doctor_id, date):
    pat = next((pat for pat in patients if pat.id == patient_id), None)
    medprof = next((medprof for medprof in doctors if medprof.id == doctor_id), None)
    if pat is None or medprof is None:
        return None
    new_appointment = Appointment(len(appointments) + 1, pat, medprof, date)
    appointments.append(new_appointment)
    medprof.appointments.append(new_appointment)
    return new_appointment

def get_available_doctors():
    return [medprof for medprof in doctors if medprof.is_available]

def book_appointment(patient_id, date):
    available_doctors = get_available_doctors()
    if not available_doctors:
        return None
    medprof = available_doctors[0]
    medprof.is_available = False
    return create_appointment(patient_id, medprof.id, date)

def complete_appointment(appointment_id):
    appointment = next((appoint for appoint in appointments if a.id == appointment_id), None)
    if appointment is None:
        return False
    appointment.doctor.is_available = True
    appointment.doctor.appointments.remove(appointment)
    appointments.remove(appointment)
    return True

def cancel_appointment(appointment_id):
    appointment = next((a for a in appointments if a.id == appointment_id), None)
    if appointment is None:
        return False
    appointment.doctor.is_available = True
    appointment.doctor.appointments.remove(appointment)
    appointments.remove(appointment)
    return True

def get_doctor_appointments(doctor_id):
    medprof = next((medprof for medprof in doctors if medprof.id == doctor_id), None)
    if medprof is None:
        return []
    return medprof.appointments

def update_appointment(appointment_id, patient_id, doctor_id, date):
    appointment = next((a for a in appointments if a.id == appointment_id), None)
    if appointment is None:
        return False
    pat = next((pat for pat in patients if pat.id == patient_id), None)
    medprof = next((medprof for medprof in doctors if medprof.id == doctor_id), None)
    if pat is None or medprof is None:
        return False
    appointment.patient = pat
    appointment.doctor = medprof
    appointment.date = date
    return True

def delete_appointment(appointment_id):
    appointment = next((a for a in appointments if a.id == appointment_id), None)
    if appointment is None:
        return False
    appointment.doctor.appointments.remove(appointment)
    appointments.remove(appointment)
    return True

# CRUD endpoints for Doctors
def create_doctor_endpoint(name, specialization, phone):
    return create_doctor(name, specialization, phone)

def read_doctor_endpoint(doctor_id):
    medprof = next((medprof for medprof in doctors if medprof.id == doctor_id), None)
    if medprof is None:
        return None
    return medprof

def update_doctor_endpoint(doctor_id, name, specialization, phone):
    medprof = next((medprof for medprof in doctors if medprof.id == doctor_id), None)
    if medprof is None:
        return None