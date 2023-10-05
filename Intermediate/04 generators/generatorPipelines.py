def course_generator():
  yield ("Computer Science", 5)
  # Write your code below:
  yield("Art", 10)
  yield("Business", 15)
    
def add_five_students(courses):
  for item in courses:
    yield (item[0], item[1]+5)


increased_courses = add_five_students(course_generator())

for item in increased_courses:
  print(item)