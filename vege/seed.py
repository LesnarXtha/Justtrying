from faker import Faker 
from vege.models import *
import random

fake = Faker()
fake.unique.clear()  # Clear previous uniqueness tracking

def create_fake_marks(n=10):
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            subject_obj = Subject.objects.all()
            for subject in subject_obj:
                SubjectMarks.objects.create(
                    student = student,
                    subject = subject,
                    marks = random.randint(0,100)
                )
    except Exception as e:
        print(e)


def seed_db(n=25):
    try:
        departments = list(Department.objects.all())
        if not departments:
            print("No departments found. Please add some first.")
            return
        
        for i in range(1, n + 1):
            department = random.choice(departments)
            student_name = fake.name()
            student_email = fake.unique.email()  # ensures uniqueness
            student_age = random.randint(18, 25)
            student_address = fake.address()

            # Generate unique student ID like STU001, STU002, ...
            student_id_str = f"STU{str(i).zfill(3)}"
            student_id_obj = StudentID.objects.create(student_id=student_id_str)

            Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address
            )
        
        print(f"{n} students seeded successfully.")
    
    except Exception as e:
        print("Error:", e)
