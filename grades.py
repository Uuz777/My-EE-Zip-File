courses = {}

print("=== Grade Tracker ===\n")
num_courses = int(input("How many courses? "))

for i in range(num_courses):
    name = input(f"\nCourse {i+1} name: ")
    grade = float(input(f"Current grade in {name} (%): "))
    weight = float(input(f"How much is the final worth (%)?: "))
    target = float(input(f"Target final grade (%): "))

    current_weight = 100 - weight
    needed = (target - (grade * current_weight / 100)) / (weight / 100)
    courses[name] = {"current": grade, "needed_on_final": needed}

print("\n====== RESULTS ======")
total = 0
for course, data in courses.items():
    print(f"\n{course}:")
    print(f"  Current grade: {data['current']}%")
    print(f"  Need on final: {data['needed_on_final']:.1f}%")
    total += data['current']

print(f"\nOverall average: {total/len(courses):.1f}%")None