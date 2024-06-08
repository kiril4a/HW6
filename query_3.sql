SELECT groups.name, AVG(grades.grade) as average_grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN groups ON students.group_id = groups.id
WHERE grades.subject_id = ?
GROUP BY groups.id;
