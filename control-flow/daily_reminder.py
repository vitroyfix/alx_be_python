
task = input("Enter your task: ")
time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()
priority = input("Enter the priority (high/medium/low): ").strip().lower()

reminder = f"Reminder: '{task}' - Priority: {priority.capitalize()}."

match priority:
    case "high":
        reminder += " This task is highly important."
    case "medium":
        reminder += " This task has moderate importance."
    case "low":
        reminder += " This task can be handled with lower urgency."
    case _:
        reminder += " Priority level is unknown."

if time_bound == "yes":
    reminder += "  Immediate action is required due to time sensitivity!"
else:
    reminder += " No urgent deadline — plan accordingly."


print(reminder)
