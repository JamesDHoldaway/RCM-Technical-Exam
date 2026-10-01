from standards import offerings

print("Hello instructor! \nThanks for using this project to assess your student's readiness for their RCM examination. ")

student = input("\nBefore we begin who is being assessed today? (data is not stored): ")

print("\nExam Offerings")
for course in offerings:
    print(f"- {course}: {offerings[course]["name"]}")

exam = input(f"\nWhich technical exam would {student} like to take? ")

while exam not in offerings:
    print("Exam doesn't match offerings")
    exam = input("Please try again: ")

print(f"\nLet's begin {offerings[exam]["name"]}\nThis exam contains {len(offerings[exam]["sections"])} section(s):\n")

num = 1

for section in offerings[exam]["sections"]:
    print(f"{num}. {section} - {len(offerings[exam]["sections"][section]["items"])} items")
    num = num + 1
