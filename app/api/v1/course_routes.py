from fastapi import APIRouter, HTTPException, Depends
from app.services.course_service import create_new_course, get_course_details
from app.models.course import Course, CourseBase
from app.db.database import get_session
router = APIRouter()


@router.post("/v1/create_course", response_model= Course)
def create_course(course: CourseBase, session = Depends(get_session)):
	try:
		return create_new_course(course, session)
	except Exception as e:
		raise HTTPException(status_code=403, detail=str(e))


@router.get("/v1/course/{course_id}", response_model=Course)
def get_course(course_id: int, session = Depends(get_session)):
	course = get_course_details(course_id, session)
	if not course:
		raise HTTPException(status_code=403, detail="Course not found")
	return course
