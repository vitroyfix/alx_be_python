
task = input("Enter the task you want to be reminded of: ")
time_bound = input("Is this task time-bound? (yes/no): ").lower()
priority = input("What is the priority? (high/medium/low): ").lower()


reminder_message = f" Task: {task}\n"


match priority:
    case "high":
        reminder_message += " Priority: High - Handle this task with urgency.\n"
    case "medium":
        reminder_message += " Priority: Medium - Plan to do this soon.\n"
    case "low":
        reminder_message += " Priority: Low - No rush, just keep it in mind.\n"
    case _:
        reminder_message += " Priority: Unknown - Please clarify priority.\n"


if time_bound == "yes":
    reminder_message += " This task is time-sensitive. Take immediate action!"
else:
    reminder_message += " This task is not urgent. Plan accordingly."


print("\n--- DAILY REMINDER ---")
print(reminder_message)
