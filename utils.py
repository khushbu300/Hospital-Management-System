import os
def save_patient_to_file(patient):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)

    file_path = os.path.join(data_dir, 'patients.txt')

    with open(file_path, 'a') as file:
        file.write(f"{patient.patient_id},{patient.name},{patient.age},{patient.gender},{patient.disease}\n")


def load_patients_from_file():
    patients = []
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'data', 'patients.txt')

        with open(file_path, 'r') as file:
            for line in file:
                patient_data = line.strip().split(',')
                patients.append({
                    "patient_id": int(patient_data[0]),
                    "name": patient_data[1],
                    "age": int(patient_data[2]),
                    "gender": patient_data[3],
                    "disease": patient_data[4]
                })
    except FileNotFoundError:
        print("No patient records found.")
    return patients

# ------------------------------------------------------------------------------------------------------------------------------------------------------



def save_doctor_to_file(doctor):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)

    file_path = os.path.join(data_dir, 'doctors.txt')

    with open(file_path, 'a') as file:
        file.write(f"{doctor.doctor_id},{doctor.name},{doctor.age},{doctor.gender},{doctor.specialization}\n")


def load_doctors_from_file():
    doctors = []
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'data', 'doctors.txt')

        with open(file_path, 'r') as file:
            for line in file:
                doctor_data = line.strip().split(',')
                doctors.append({
                    "doctor_id": int(doctor_data[0]),
                    "name": doctor_data[1],
                    "age": int(doctor_data[2]),
                    "gender": doctor_data[3],
                    "specialization": doctor_data[4]
                })
    except FileNotFoundError:
        print("No doctor records found.")
    return doctors