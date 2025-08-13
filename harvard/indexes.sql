create index enrollments_index on enrollments(student_id, course_id);
create index courses_3_index on courses(department,number,semester);
create index enrollments_by_course_id_index on enrollments(course_id);
create index course_by_semester_index on courses(semester, department, title);
create index satisfies_index on satisfies(course_id,requirement_id);
