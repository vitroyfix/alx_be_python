task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        priority_note = "High - Handle this task with urgency."
    case "medium":
        priority_note = "Medium - Plan to do this soon."
    case "low":
        priority_note = "Low - No rush, just keep it in mind."
    case _:
        priority_note = "Unknown - Please clarify priority."

if time_bound == "yes":
    urgency_note = "This task is time-sensitive. Take immediate action!"
else:
    urgency_note = "This task is not urgent. Plan accordingly."

print(f"Reminder: {task} | Priority: {priority_note} | {urgency_note}")
