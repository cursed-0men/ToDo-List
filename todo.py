import json
import os.path


# adding task function
def add_task(tasks):
    task_name = input("Enter task name: ")
    new_task = {'ID': len(tasks) + 1, 'Name': task_name, 'Status': 'Pending'}
    tasks.append(new_task)
    print(f"Task {task_name} added successfully.")

# displaying task function
def display_task(tasks):
    if not tasks:
        print("No tasks found...")
    else:
        print("Clipboard :")
        print("\t\t ID \t\t\t Name \t\t\t Status\n")
        for task in tasks:
            print(f"\t\t {task['ID']} \t\t\t {task['Name']: <30} \t\t\t {task['Status']}")

# save task
def save_task(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)
        f.write('\n')
    print("Tasks saved successfully.")

# load task
def load_task():
    tasks = []
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
            if tasks:
                  print("Tasks loaded successfully.")
                  display_task(tasks)
    else:
        print("No saved tasks found")
    return tasks

# mark as complete
def mark_complete(tasks):
    task_id = int(input("Enter ID of task to mark as complete: "))
    for task in tasks:
        if task['ID'] == task_id:
            task['Status'] = 'Completed'
            print(f"Task '{task['Name']}' with ID {task['ID']} is marked as Completed.")
            return
    print("Task not found.")

# deleting task
def delete_task(tasks):
    task_id = int(input("Enter ID of task to delete: "))
    for task in tasks:
        if task['ID'] == task_id:
            tasks.remove(task)
            print(f"Task '{task['Name']}' with ID {task['ID']} deleted successfully.")
            return
    print("Task not found.")

def main():
    tasks = load_task()
    while True:
        print("\n          SELECT OPTION          ")
        print("+-------------------------------+")
        print("| 1. Add task                   |")
        print("| 2. Display tasks              |")
        print("| 3. Save task                  |")
        print("| 4. Load saved task            |")
        print("| 5. Mark as complete           |")
        print("| 6. Delete task                |")
        print("| 7. Exit...                    |")
        print("+-------------------------------+")

        choice = input("Enter choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_task(tasks)
        elif choice == '3':
            save_task(tasks)
        elif choice == '4':
            tasks = load_task()
        elif choice == '5':
            mark_complete(tasks)
        elif choice == '6':
            delete_task(tasks)
        elif choice == '7':
            save_task(tasks)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()

# change display fn to support bigger names
