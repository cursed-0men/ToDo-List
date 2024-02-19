# ToDo List 
# 1. Overview
The Task Management System is a simple Python application designed to help users manage tasks by providing functionalities to add tasks, display tasks, mark tasks as complete, delete tasks, save tasks to a file, and load saved tasks from a file.

# 2. File Structure
task_management.py: This is the main Python script containing the implementation of the Task Management System.
tasks.json: This file is used to store tasks in JSON format.

# 3. Functionalities
1. Adding a Task
Function: add_task(tasks)
Description: Prompts the user to enter the name of a task and add it to the list of tasks with a default status of "Pending".
Usage: Enter the task name when prompted.

2. Displaying Tasks
Function: display_task(tasks)
Description: Displays the list of tasks along with their IDs, names, and statuses.
Usage: This function is called whenever the user chooses to display tasks.

3. Saving Tasks
Function: save_task(tasks)
Description: Saves the current list of tasks to a JSON file named "tasks.json".
Usage: This function is called when the user chooses to save tasks.

5. Loading Tasks
Function: load_task()
Description: Loads previously saved tasks from the "tasks.json" file.
Usage: This function is automatically called at the beginning of the program to load saved tasks.

6. Marking a Task as Complete
Function: mark_complete(tasks)
Description: Allows the user to mark a task as complete by entering its ID.
Usage: Enter the ID of the task to mark it as complete when prompted.

7. Deleting a Task
Function: delete_task(tasks)
Description: Allows the user to delete a task by entering its ID.
Usage: Enter the ID of the task to delete it when prompted.

# NOTES
Task IDs are automatically assigned based on the order in which tasks are added.
Tasks are saved in JSON format for easy persistence.
