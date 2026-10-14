from standards import offerings


def get_name():
    return input("\nBefore we begin who is being assessed today? (data is not stored): ")


def choose_exam(student):
    print("\nExam Offerings")
    for course in offerings:
        print(f"- {course}: {offerings[course]["name"]}")

    lookup = {}
    for key in offerings:
        lookup[key.lower()] = key

    choice = input(f"\nWhich technical exam would {student} like to take? ")
    while choice.strip().lower() not in lookup:
        print("Exam doesn't match offerings")
        choice = input("Please try again: ")

    return lookup[choice.strip().lower()]


def preview_exam(exam):
    print(f"\nLet's begin {offerings[exam]["name"]}\nThis exam contains {len(offerings[exam]["sections"])} section(s):\n")

    for num, section in enumerate(offerings[exam]["sections"], start=1):
        print(f"{num}. {section} - {len(offerings[exam]["sections"][section]["items"])} items")

    ready = input(f"\nType READY when you are ready to begin with section 1: {list(offerings[exam]["sections"])[0]} ")
    while ready != "READY":
        ready = input("Answer not accepted try again ")


def get_score(item):
    while True:
        try:
            score = int(input("Score 0-5 entered as a number: "))
            if score > 5 or score < 0:
                print("Invalid score! Try again ")
                continue
            return score
        except ValueError:
            print(f"Please enter a valid score 0-5 for {item}: ")


def run_exam(exam):
    total = 0
    results = {}

    for num, section in enumerate(offerings[exam]["sections"], start=1):
        current = offerings[exam]["sections"][section]
        print(f"{num}/{len(offerings[exam]["sections"])} - {section}")
        section_total = 0

        for item in current["items"]:
            print(item, " - Section Score: ", round(section_total, 2), " Total Score: ", round(total, 2))
            score = get_score(item)
            section_total = section_total + current["Weight"]*score/5

        total = total + section_total
        results[section] = section_total

    return results


def print_summary(student, exam, results):
    total = sum(results.values())
    max_total = 0

    print(f"--- Results for {student}: {offerings[exam]["name"]} ---")
    for section in offerings[exam]["sections"]:
        current = offerings[exam]["sections"][section]
        section_max = current["Weight"] * len(current["items"])
        print(f"{section}:          {round(results[section], 2)} / {section_max}")
        max_total = max_total + section_max
    print(f"Total:          {round(total, 2)} / {round(max_total, 2)} ({round(100*total/max_total, 2)}%)")


if __name__ == "__main__":
    print("Hello instructor! \nThanks for using this project to assess your student's readiness for their RCM examination. ")
    student = get_name()
    exam = choose_exam(student)
    preview_exam(exam)
    results = run_exam(exam)
    print_summary(student, exam, results)
