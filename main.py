from standards import offerings

print("Hello instructor! Thanks for using this project to assess your student's readiness for their RCM examination. ")

student = input("Before we begin who is being assessed today? (don't worry all of their data is stored locally on your computer) ")

for course in offerings:
    print(course)

exam = input(f"Which technical exam would {student} like to take? ")

print(f"Lets do it here is {exam}!!")
