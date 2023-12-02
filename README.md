**How to use**
```shell
$ pip install -r requirements.txt

$ python manage.py runserver
```

**This system includes three types of users: students, instructors, and system administrators, the brief requirements of these three types of users for the system are summarized as follows:**

**Student User**
The primary requirements of students for this system are to utilize it for online learning, which includes completing assignments, participating in Q&A sessions, taking online exams, and viewing overall scores, among other functions.
- Online Learning Requirements: Students should be able to access all course materials, including course materials, videos, and presentations, on this system.
- Online Exam Requirements: Students should be able to select and complete exams on this system.
- Assignment Submission Requirements: Students should be able to complete assignments posted by instructors on this system.

**Instructor User**
Instructors primarily need the system for managing students, uploading all necessary teaching materials, assigning and reviewing assignments, assessing student notes and code, and managing exams, among other functions.
- Student Management Requirements: Instructors should be able to add or remove students as needed for effective student management.
- Teaching Material Upload Requirements: Instructors need to upload teaching materials for students' use.
- Assignment Posting and Review Requirements: Instructors need to post and review assignments.
- Exam Management Requirements: Instructors should have administrative privileges for exam-related functions on the system.

**System Administrator User**
System administrators have the highest level of system authority, responsible for the dynamic synchronization and maintenance of all necessary data for the system. The basic functional requirements are as follows:
- System Settings: Configuring student ID length to accommodate different educational institutions using the system.
- Adding and Querying Departments: Adding different departments based on different educational institutions.
- Adding and Querying Classes: Adding different classes based on different departments.
- Adding and Querying Courses: Adding different courses based on different educational institutions.
- Adding and Querying Instructors: Adding different instructor users based on different departments.
- Adding and Querying Students: Adding different student users based on different departments.

**System Functional Description**
The online teaching platform consists of five major modules: the instructor system, forum management, student system, teaching management system, and process assessment. These modules are interconnected and collaborate with each other to create a complete online teaching system.
- Teaching System Management
   - User Management: The system administrator can perform functions such as user addition, deletion, modification, and inquiry, while other users can only inquire about or modify their own information.
   - Basic Information Management: The system administrator can establish and modify database information, including adding, deleting, modifying, and querying department, class, and course information.
   - Question Bank Management: Administrators can add, delete, modify, and query questions.
- Student System (Students learn and record learning progress; instructors and administrators can learn but do not record results)
   - Online Testing (score control)
   - Online Learning
   - Assignment Inquiry
   - Download or Browse Teaching Materials
   - Personal Space
- Instructor System (Only allows instructors to maintain their own teaching)
   - Basic Course Information Management: Including the establishment and upload of course basic information.
   - Student Management: Instructors can add, delete, modify, and query student users.
   - Teaching Material Management: Uploading and maintaining teaching materials.
   - Assignment Management: Uploading and maintaining course assignments.
   - Exam Management: Creating questions, publishing exams, and grading exam scores.
 

**System Functional Diagram**
# Online Teaching Platform

## Instructor System Module
- User Management
- Basic Course Info Management
- Student Management
- Teaching Material Management
- Assignment Management
- Exam Management

## Forum Management Module
- Discussion Forum Management
- User Comments Management

## Student System Module
- Online Testing
- Online Learning
- Assignment Inquiry
- Download or Browse Materials
- Personal Space

## Teaching Management System Module
- User Management
- Basic Info Management
- Question Bank Management

## Process Assessment Module
- Student Progress Monitoring
- Performance Assessment

