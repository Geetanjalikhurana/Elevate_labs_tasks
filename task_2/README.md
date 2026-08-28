# Task 2: Console-based To-Do List Application

**Elevate Labs - Python Developer Internship**

A clean, persistent, console-based To-Do List Application built with Python. This application allows users to view, add, toggle completion status, and remove tasks, with automatic persistent text file storage.

---

## 📌 Features

- **Task Management**: View, add, mark complete/pending, and remove tasks easily via an interactive terminal menu.
- **File Persistence**: All tasks are automatically stored in `tasks.txt` so your data persists across app restarts.
- **Input Validation**: Robust error handling for empty task titles, invalid list index choices, and non-integer inputs.
- **Automated Testing**: Includes full unit test coverage using Python's built-in `unittest` framework.

---

## 📂 Project Structure

```text
task_2/
├── todo.py          # Main application source code
├── test_todo.py     # Unit test suite
├── tasks.txt        # Persistent task storage file (auto-generated)
└── README.md        # Documentation and interview question responses
```

---

## 🚀 Getting Started & Usage

### Prerequisites
- Python 3.x installed on your machine.

### Running the To-Do Application
Open your terminal in the `task_2` directory and execute:

```bash
python todo.py
```

#### Menu Options
```text
==============================
      TO-DO LIST MANAGER      
==============================
1. View Tasks
2. Add Task
3. Toggle Task Complete/Pending
4. Remove Task
5. Exit
==============================
```

### Running Unit Tests
To verify all core functionality, execute:

```bash
python -m unittest test_todo.py
```

---

## 📚 Technical Interview Questions & Answers

### 1. How do you open and write to a file in Python?
You open a file using Python's built-in `open()` function, specifying the file path and mode (such as `'w'` for write or `'a'` for append). It is best practice to use a `with` statement (context manager) to ensure proper resource handling and automatic closing:

```python
with open("tasks.txt", "w", encoding="utf-8") as file:
    file.write("[ ] Buy groceries\n")
```

### 2. What are common file modes?
The primary file modes in Python are:
- `'r'`: Read mode (default). Opens file for reading; raises `FileNotFoundError` if the file doesn't exist.
- `'w'`: Write mode. Opens file for writing; creates file if it doesn't exist, or overwrites/truncates it if it does.
- `'a'`: Append mode. Opens file for writing; appends new content to the end of the file without deleting existing content.
- `'r+'`: Read and Write mode. Opens file for both reading and writing.
- `'b'`: Binary mode (e.g., `'rb'`, `'wb'`). Opens file in binary format instead of text.

### 3. What's the use of `.strip()`?
The `.strip()` method removes leading and trailing whitespace (spaces, tabs, newlines `\n`) from a string. It is useful when reading lines from a text file to remove the trailing newline character, or when validating user input:

```python
line = "  Buy milk\n  "
clean_line = line.strip()  # Output: "Buy milk"
```

### 4. How do lists work in Python?
Lists in Python are dynamic, ordered, and mutable collections of items. They allow duplicate elements and can store elements of mixed data types. Internally, Python lists are implemented as dynamically resized arrays, providing indexed access in $O(1)$ time.

```python
tasks = ["Task 1", "Task 2"]
print(tasks[0])  # Access first element -> "Task 1"
```

### 5. What is the difference between `append()` and `insert()`?
- `append(item)`: Adds an element to the **end** of the list ($O(1)$ amortized time complexity).
- `insert(index, item)`: Inserts an element at a **specific index**, shifting existing elements to the right ($O(n)$ time complexity).

```python
tasks = ["A", "C"]
tasks.append("D")          # ["A", "C", "D"]
tasks.insert(1, "B")       # ["A", "B", "C", "D"]
```

### 6. How can you remove elements from a list?
Elements can be removed using several methods depending on the use case:
- `list.pop(index)`: Removes and returns the item at the specified index (defaults to the last item).
- `list.remove(value)`: Removes the first occurrence of a specified value.
- `del list[index]`: Deletes an element at a given index or slice.
- `list.clear()`: Removes all items from the list.

```python
tasks = ["Task 1", "Task 2", "Task 3"]
tasks.pop(0)            # Removes "Task 1" by index
tasks.remove("Task 2")  # Removes "Task 2" by value
```

### 7. What are context managers (`with` statement)?
Context managers manage resources efficiently by automatically handling setup and cleanup tasks (such as opening and closing files, or acquiring and releasing locks), even if exceptions occur within the block.

```python
# The file is automatically closed when exiting the block
with open("file.txt", "r") as f:
    content = f.read()
```

### 8. How do you loop through a file line by line?
You can iterate directly over the file object using a `for` loop, which processes the file line-by-line efficiently without loading the whole file into memory at once:

```python
with open("tasks.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

### 9. What is a data structure?
A data structure is a specialized format for organizing, processing, retrieving, and storing data efficiently. Examples in Python include lists, dictionaries, tuples, sets, and custom classes, each offering trade-offs for different operations (e.g., lookups, insertions, ordering).

### 10. What happens if the file doesn't exist?
- When opening in **read mode (`'r'`)**: Python raises a `FileNotFoundError`. To handle this, use `try-except` blocks or check `os.path.exists()`.
- When opening in **write mode (`'w'`)** or **append mode (`'a'`)**: Python creates a new, empty file automatically.

```python
import os

if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
else:
    tasks = []  # Start with an empty list if file doesn't exist
```

---

## 🛠️ Key Concepts Applied
- **File Handling**: File operations with context managers (`open()`, `with`, `r`, `w` modes).
- **Lists & Dictionaries**: Structured task storage with `title` and `completed` status flags.
- **String Manipulation**: String formatting, `.strip()`, `.startswith()`, and index slicing.
- **Error & Exception Handling**: Safe handling of `ValueError`, `IndexError`, and missing files.
