from standards import offerings

print("Hello instructor! \nThanks for using this project to assess your student's readiness for their RCM examination. ")

student = input("\nBefore we begin who is being assessed today? (data is not stored): ")

print("\nExam Offerings")
for course in offerings:
    print(f"- {course}: {offerings[course]["name"]}")

exam = input(f"\nWhich technical exam would {student} like to take? ")

print(f"\nLet's begin {offerings[exam]["name"]}")