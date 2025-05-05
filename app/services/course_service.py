from fastapi import FastAPI, Depends, HTTPException
from app.db.database import engine, get_session
from app.models.course import CourseBase, Course


def create_new_course(course, session):
	rec = Course.model_validate(course)
	session.add(rec)
	session.commit()
	session.refresh(rec)
	return rec


def get_course_details(course_id: int, session):
	course = session.get(Course, course_id)
	if not course:
		raise HTTPException(status_code=403, detail="Course not found")
	return course
