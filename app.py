# Student Study Planner Agent

print("=== Student Study Planner Agent ===")

name = input("Enter your name: ")
subjects = int(input("How many subjects do you have? "))

subject_list = []

for i in range(subjects):
    subject = input(f"Enter Subject {i+1}: ")
    hours = float(input(f"Hours needed for {subject} per week: "))
    subject_list.append((subject, hours))

print("\n----- Study Plan for", name, "-----")

total_hours = 0

for subject, hours in subject_list:
    print(f"{subject} : {hours} hours/week")
    total_hours += hours

print("\nTotal Study Hours Required:", total_hours)

days = 7
daily_hours = total_hours / days

print(f"Recommended Daily Study Time: {daily_hours:.2f} hours/day")

print("\nSuggested Timetable:")
for subject, hours in subject_list:
    print(f"- Study {subject} for {hours/days:.2f} hours daily")

print("\nStay consistent and revise regularly!")
