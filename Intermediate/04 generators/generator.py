def student_standing_generator():
  student_standings = ['Freshman','Senior', 'Junior', 'Freshman']
  # Write your code below:
  for student in student_standings:
    if student == 'Freshman':
      yield 500
  

standing_values = student_standing_generator()

print(next(standing_values))
print(next(standing_values))
print(next(standing_values))