from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import List

app = FastAPI()

students = []
enrollments = {}  # key = course_id, value = list of student_ids

class StudentModel(BaseModel):
    student_id: int
    name: str

class CourseModel(BaseModel):
    course_id: int
    course_name: str
    capacity: int

class CourseInventory:
    def __init__(self):
        self.courses: List[CourseModel] = []

    def add_course(self, course: CourseModel):
        if course.course_id not in [c.course_id for c in self.courses]:
            self.courses.append(course)
            return True
        else:
            return False

    def find_course(self, course_id: int):
        return next((c for c in self.courses if c.course_id == course_id), None)

    def list_courses(self):
        return self.courses

inventory = CourseInventory()

@app.get("/v1/courses")
async def list_courses():
    return {"status": "success", "data": inventory.list_courses()}

@app.post("/v1/create_course")
async def create_course(course: CourseModel):
    try:
        if inventory.add_course(course):
            return {"status": "success"}
        else:
            return {"status": "skipped", "message": "Course already exists."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/v1/student/register")
def student_register(student: StudentModel):
    if student.student_id not in [s.student_id for s in students]:
        students.append(student)
        return {"status": "success"}
    else:
        return {"status": "skipped", "message": "Student already registered."}

@app.get("/v1/students")
def list_students():
    return {"status": "success", "data": students}

@app.post("/v1/course/{course_id}/enroll/{student_id}")
def enroll(course_id: int, student_id: int):
    course = inventory.find_course(course_id)
    if not course:
        return {"status": "error", "message": "Course not found."}

    student_exists = any(s.student_id == student_id for s in students)
    if not student_exists:
        return {"status": "error", "message": "Student not registered."}

    current_enrolled = len(enrollments.get(course_id, []))
    if current_enrolled >= course.capacity:
        return {"status": "error", "message": "Course is full."}

    if course_id in enrollments:
        if student_id not in enrollments[course_id]:
            enrollments[course_id].append(student_id)
    else:
        enrollments[course_id] = [student_id]

    return {"status": "success", "message": "Enrollment successful."}

@app.get("/v1/course/{course_id}/enrolls")
def list_enrolled_students(course_id: int):
    enrolled_students = enrollments.get(course_id, [])
    return {"status": "success", "data": enrolled_students}
