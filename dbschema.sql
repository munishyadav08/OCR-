CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob DATE
);

CREATE TABLE functional_assessment (
    id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(id),
    date DATE,
    injection VARCHAR(3),
    exercise_therapy VARCHAR(3),
    difficulty_ratings JSONB,
    patient_changes JSONB
);

CREATE TABLE pain_symptoms (
    id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(id),
    pain INT,
    numbness INT,
    tingling INT,
    burning INT,
    tightness INT
);

CREATE TABLE medical_assistant_data (
    id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(id),
    blood_pressure VARCHAR(20),
    heart_rate VARCHAR(10),
    weight VARCHAR(10),
    height VARCHAR(10),
    temperature VARCHAR(10),
    blood_glucose VARCHAR(10),
    respirations VARCHAR(10),
    spo2 VARCHAR(10)
);
