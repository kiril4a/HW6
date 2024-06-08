SELECT students.name, grades.grade, grades.date
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = ? AND grades.subject_id = ?;
