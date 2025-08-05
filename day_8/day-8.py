dog = {'name': 'bolt', 'breed': 'corgi', 'legs': 4, 'age': 4}
student = {
    'first_name': 'nico',
    'last_name': 'robin',
    'gender': 'female',
    'age': 30,
    'marital status': 'single',
    'skills': ['archeologist', 'poneglyph reader'],
    'country': 'ohara'
}

print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('strong slapper')
print(student)
print(list(student.keys()))
print(list(student.values()))
student_tpl = student.items()
print()
print(student_tpl)
student.pop('country')
print(student)
del student
# print(student)