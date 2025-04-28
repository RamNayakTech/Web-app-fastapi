# Requirements
## Courses
- Each course has: course_id, name, capacity.
- Capacity = maximum number of students allowed.

## Students
- Each student has: student_id, name.
---
### APIs Needed
- Create a new course
- Register a new student
- Enroll a student into a course
- Check if course capacity is not full before enrolling.
- Prevent duplicate enrollment (student cannot enroll twice in same course).
- Get list of students enrolled in a course
--- 
## Persistence
- For now, use in-memory data structures (no database).
- Later we can extend to file/database if you want.
---
## Error Handling
- If someone tries to enroll into a full course → return an appropriate error.
- If course/student doesn’t exist → error.