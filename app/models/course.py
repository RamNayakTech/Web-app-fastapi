from sqlmodel import SQLModel, Field
from typing import Optional


class CourseBase(SQLModel):
	course_name: str
	capacity: int


class Course(CourseBase, table=True):
	course_id: Optional[int] = Field(default=None, primary_key=True)

