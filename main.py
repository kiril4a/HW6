import sqlite3
from faker import Faker
import random
from datetime import datetime

# Ініціалізація бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Створення таблиць
cursor.executescript('''
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS groups;
DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS grades;

CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
);

CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
);

CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date TEXT,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
);
''')

fake = Faker()

# Заповнення груп
groups = ['Group A', 'Group B', 'Group C']
for group in groups:
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (group,))

# Заповнення викладачів
teachers = [fake.name() for _ in range(5)]
for teacher in teachers:
    cursor.execute("INSERT INTO teachers (name) VALUES (?)", (teacher,))

# Заповнення предметів
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Literature', 'Computer Science']
for subject in subjects:
    teacher_id = random.randint(1, len(teachers))
    cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject, teacher_id))

# Заповнення студентів
for _ in range(50):
    name = fake.name()
    group_id = random.randint(1, len(groups))
    cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))

# Заповнення оцінок
for student_id in range(1, 51):
    for _ in range(random.randint(10, 20)):
        subject_id = random.randint(1, len(subjects))
        grade = random.randint(60, 100)
        date = fake.date_this_year().isoformat()
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                       (student_id, subject_id, grade, date))

conn.commit()
conn.close()
