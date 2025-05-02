from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import  SQLModel
from app.db.database import engine, get_session
from app.api.v1 import course_routes
from app.models.course import CourseBase, Course

# # Allow CORS for all origins (development mode)
# app.add_middleware(
# 	CORSMiddleware,
# 	allow_origins=["*"],  # Allow all for now; restrict in production!
# 	allow_credentials=True,
# 	allow_methods=["*"],  # Allow all methods like POST, GET, etc.
# 	allow_headers=["*"],  # Allow all headers
# )

# # Mount the 'frontend' folder to /frontend URL
# app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")
#
# students = []
# enrollments = {}  # key = course_id, value = list of student_ids
#
#
# # Redirect root URL to your main page (optional)
# @app.get("/")
# async def root():
# 	return RedirectResponse(url="/frontend/user_registration.html")
#
#
# class StudentModel(BaseModel):
# 	# student_id: int
# 	first_name: str
# 	last_name: str
# 	dob: date
# 	gender: str


SQLModel.metadata.create_all(engine)

app = FastAPI()

app.include_router(course_routes.router)

# @app.post("/v1/create_course", response_model= Course)
# async def create_course(course: CourseBase, session = Depends(get_session)):
# 	rec = Course.model_validate(course)
# 	session.add(rec)
# 	session.commit()
# 	session.refresh(rec)
# 	return rec
#
#
# @app.get("/v1/course/{course_id}", response_model=Course)
# async def get_course(course_id: int, session = Depends(get_session)):
# 	course = session.get(Course, course_id)
# 	if not course:
# 		raise HTTPException(status_code=403, detail="Course not found")
# 	return course

#
# @app.post("/v1/student/register")
# def student_register(student: StudentModel):
# 	# if student.student_id not in [s.student_id for s in students]:
# 	#     students.append(student)
# 	#     return {"status": "success"}
# 	# else:
# 	#     return {"status": "skipped", "message": "Student already registered."}
# 	students.append(student)
#
#
# @app.get("/v1/students")
# def list_students():
# 	return {"status": "success", "data": students}
#
#
# @app.post("/v1/course/{course_id}/enroll/{student_id}")
# def enroll(course_id: int, student_id: int):
# 	course = inventory.find_course(course_id)
# 	if not course:
# 		return {"status": "error", "message": "Course not found."}
#
# 	student_exists = any(s.student_id == student_id for s in students)
# 	if not student_exists:
# 		return {"status": "error", "message": "Student not registered."}
#
# 	current_enrolled = len(enrollments.get(course_id, []))
# 	if current_enrolled >= course.capacity:
# 		return {"status": "error", "message": "Course is full."}
#
# 	if course_id in enrollments:
# 		if student_id not in enrollments[course_id]:
# 			enrollments[course_id].append(student_id)
# 	else:
# 		enrollments[course_id] = [student_id]
#
# 	return {"status": "success", "message": "Enrollment successful."}
#
#
# @app.get("/v1/course/{course_id}/enrolls")
# def list_enrolled_students(course_id: int):
# 	enrolled_students = enrollments.get(course_id, [])
# 	return {"status": "success", "data": enrolled_students}
