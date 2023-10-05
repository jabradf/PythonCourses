from roster import student_roster
import classroom_organizer

students = iter(student_roster)

print(next(students))

students = classroom_organizer.ClassroomOrganizer()

students.student_combinations(students)