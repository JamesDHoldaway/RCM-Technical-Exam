from standards import offerings

print("Hello instructor! \nThanks for using this project to assess your student's readiness for their RCM examination. ")

student = input("\nBefore we begin who is being assessed today? (data is not stored): ")

print("\nExam Offerings")
for course in offerings:
    print(f"- {course}: {offerings[course]["name"]}")

lookup = {}
for key in offerings:
    lookup[key.lower()] = key

exam = input(f"\nWhich technical exam would {student} like to take? ")

while exam.strip().lower() not in lookup:
    print("Exam doesn't match offerings")
    exam = input("Please try again: ")

exam = lookup[exam.strip().lower()]

print(f"\nLet's begin {offerings[exam]["name"]}\nThis exam contains {len(offerings[exam]["sections"])} section(s):\n")

num = 1

for section in offerings[exam]["sections"]:
    print(f"{num}. {section} - {len(offerings[exam]["sections"][section]["items"])} items")
    num = num + 1

ready = input(f"\nType READY when you are ready to begin with section 1: {list(offerings[exam]["sections"])[0]} ")

while ready != "READY":
    ready = input("Answer not accepted try again ")

num = 1
total = 0 
results = {}

for section in offerings[exam]["sections"]:
    current = offerings[exam]["sections"][section]
    print(f"{num}/{len(offerings[exam]["sections"])} - {section}")
    num = num +1
    section_total = 0
    for item in current["items"]:
        print(item, " - Section Score: ", round(section_total, 2), " Total Score: ", round(total, 2))
        while True:
            try:
                score = input("Score 0-5 entered as a number: ")
                score = int(score)
                if score > 5 or score < 0:
                    print("Invalid score! Try again ")
                    continue
                section_total = section_total + current["Weight"]*score/5
                break
            except ValueError:
                print(f"Please enter a valid score 0-5 for {item}: ")
    total = total + section_total
    results[section] = section_total

max_total = 0 
print(f"--- Results for {student}: {offerings[exam]["name"]} ---")
for section in offerings[exam]["sections"]:
    current = offerings[exam]["sections"][section]
    section_max = current["Weight"] * len(current["items"])
    print(f"{section}:          {round(results[section], 2)} / {section_max}")
    max_total = max_total + section_max
print(f"Total:          {round(total, 2)} / {round(max_total, 2)} ({round(100*total/max_total, 2)}%)")