from sqlmodel import SQLModel, Field
from typing import Optional

class StudentBase(SQLModel):
	student_name:str


# Table model
class Student(StudentBase, table= True):
	student_id : Optional[int] = Field(default=None, primary_key=True)

