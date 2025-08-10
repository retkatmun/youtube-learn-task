student = {
    "name": "scholar",
    "age": 20,
    "grade": "A"
}
print(student["name"])

student["hubby"] = "coding"
student["grade"] = "B"
print(student)

convert = list(student)
print(type(convert))

third = convert[2]
print(third)

for key in student:
	print(key)
for value in student:
	print(value)

student.pop("hubby")
print(student)

for key, value in student.items():
	print(f"{key}: {value}")

	
