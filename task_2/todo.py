"""
Console-based To-Do List Application
Task 2 - Elevate Labs Python Developer Internship

This module provides a command-line interface (CLI) to manage a to-do list
with file persistence support.
"""

import os
from typing import List, Dict

FILE_PATH = "tasks.txt"


def load_tasks(filepath: str = FILE_PATH) -> List[Dict[str, any]]:
    """
    Loads tasks from a text file.

    Returns:
        List[Dict[str, any]]: A list of task dictionaries containing 'title' and 'completed'.
    """
    tasks = []
    if not os.path.exists(filepath):
        return tasks

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                # Line format expected: "[X] Task description" or "[ ] Task description"
                if line.startswith("[X]") or line.startswith("[x]"):
                    completed = True
                    title = line[3:].strip()
                elif line.startswith("[ ]"):
                    completed = False
                    title = line[3:].strip()
                else:
                    # Fallback for plain lines without checkbox prefix
                    completed = False
                    title = line

                if title:
                    tasks.append({"title": title, "completed": completed})
    except IOError as e:
        print(f"Error reading file {filepath}: {e}")

    return tasks


def save_tasks(tasks: List[Dict[str, any]], filepath: str = FILE_PATH) -> None:
    """
    Saves the list of tasks to a text file.

    Args:
        tasks: List of task dictionaries.
        filepath: Path to the target text file.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            for task in tasks:
                status = "[X]" if task["completed"] else "[ ]"
                file.write(f"{status} {task['title']}\n")
    except IOError as e:
        print(f"Error writing to file {filepath}: {e}")


def display_tasks(tasks: List[Dict[str, any]]) -> None:
    """
    Prints all tasks in a formatted list.
    """
    if not tasks:
        print("\nYour to-do list is currently empty!")
        return

    print("\n--- YOUR TO-DO LIST ---")
    for index, task in enumerate(tasks, start=1):
        status = "[✓]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['title']}")
    print("-----------------------")


def add_task(tasks: List[Dict[str, any]], title: str) -> bool:
    """
    Adds a new task to the task list.

    Returns:
        bool: True if task was added successfully, False otherwise.
    """
    cleaned_title = title.strip()
    if not cleaned_title:
        print("Error: Task title cannot be empty.")
        return False

    tasks.append({"title": cleaned_title, "completed": False})
    print(f"Added task: \"{cleaned_title}\"")
    return True


def toggle_task_status(tasks: List[Dict[str, any]], index: int) -> bool:
    """
    Toggles the completion status of a task by 1-based index.

    Returns:
        bool: True if operation succeeded, False otherwise.
    """
    if 1 <= index <= len(tasks):
        task = tasks[index - 1]
        task["completed"] = not task["completed"]
        status_str = "completed" if task["completed"] else "pending"
        print(f"Marked task \"{task['title']}\" as {status_str}.")
        return True
    else:
        print(f"Error: Invalid task number {index}. Please enter a valid number.")
        return False


def remove_task(tasks: List[Dict[str, any]], index: int) -> bool:
    """
    Removes a task from the list by 1-based index.

    Returns:
        bool: True if task was removed successfully, False otherwise.
    """
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Removed task: \"{removed_task['title']}\"")
        return True
    else:
        print(f"Error: Invalid task number {index}. Please enter a valid number.")
        return False


def print_menu() -> None:
    """
    Displays the CLI menu options.
    """
    print("\n==============================")
    print("      TO-DO LIST MANAGER      ")
    print("==============================")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Toggle Task Complete/Pending")
    print("4. Remove Task")
    print("5. Exit")
    print("==============================")


def main() -> None:
    """
    Main loop for running the CLI application.
    """
    tasks = load_tasks()

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_tasks(tasks)

        elif choice == "2":
            title = input("Enter task title: ")
            if add_task(tasks, title):
                save_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            if tasks:
                try:
                    num = int(input("Enter task number to toggle status: ").strip())
                    if toggle_task_status(tasks, num):
                        save_tasks(tasks)
                except ValueError:
                    print("Error: Please enter a valid integer task number.")

        elif choice == "4":
            display_tasks(tasks)
            if tasks:
                try:
                    num = int(input("Enter task number to remove: ").strip())
                    if remove_task(tasks, num):
                        save_tasks(tasks)
                except ValueError:
                    print("Error: Please enter a valid integer task number.")

        elif choice == "5":
            save_tasks(tasks)
            print("\nTasks saved successfully. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option between 1 and 5.")


if __name__ == "__main__":
    main()
