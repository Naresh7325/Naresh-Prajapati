import json
from datetime import datetime

class TaskManager:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description, priority, due_date):
        task = {
            "description": description,
            "priority": priority,
            "due_date": due_date,
            "status": "pending"
        }
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self, status=None):
        for i, task in enumerate(self.tasks, start=1):
            if status is None or task["status"] == status:
                print(f"{i}. {task['description']} (Priority: {task['priority']}, Due: {task['due_date']}, Status: {task['status']})")

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["status"] = "completed"
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

# Sample Main Program
if __name__ == "__main__":
    manager = TaskManager()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            desc = input("Task Description: ")
            priority = input("Priority (low/medium/high): ")
            due = input("Due Date (YYYY-MM-DD): ")
            manager.add_task(desc, priority, due)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            idx = int(input("Task Number to mark complete: ")) - 1
            manager.mark_complete(idx)
        elif choice == "4":
            idx = int(input("Task Number to delete: ")) - 1
            manager.delete_task(idx)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
