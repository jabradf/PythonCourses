def student_counter():
  for i in range(1,5001):
    try:
      yield i
    except GeneratorExit:
      print("")
      break

student_generator = student_counter()
for student_id in student_generator:
  print(student_id)
  # Write your code below:
  if student_id > 99:
    student_generator.close()