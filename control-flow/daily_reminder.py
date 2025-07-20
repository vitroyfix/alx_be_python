task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Task: '{task}' has an undefined priority"

if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if "Reminder" in message:
        message += ". Plan your time accordingly."
    else:
        message += ". Consider completing it when you have free time."

print("\n" + message)
