"""
Unit tests for To-Do List Application (todo.py)
"""

import os
import unittest
from todo import (
    add_task,
    remove_task,
    toggle_task_status,
    save_tasks,
    load_tasks,
)


class TestTodoApp(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_tasks.txt"
        self.tasks = []
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        result = add_task(self.tasks, "Buy milk")
        self.assertTrue(result)
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0]["title"], "Buy milk")
        self.assertFalse(self.tasks[0]["completed"])

    def test_add_empty_task(self):
        result = add_task(self.tasks, "   ")
        self.assertFalse(result)
        self.assertEqual(len(self.tasks), 0)

    def test_toggle_task_status(self):
        add_task(self.tasks, "Read a book")
        result = toggle_task_status(self.tasks, 1)
        self.assertTrue(result)
        self.assertTrue(self.tasks[0]["completed"])

        # Toggle back to false
        result_toggle_back = toggle_task_status(self.tasks, 1)
        self.assertTrue(result_toggle_back)
        self.assertFalse(self.tasks[0]["completed"])

    def test_toggle_invalid_index(self):
        add_task(self.tasks, "Read a book")
        result = toggle_task_status(self.tasks, 99)
        self.assertFalse(result)

    def test_remove_task(self):
        add_task(self.tasks, "Task 1")
        add_task(self.tasks, "Task 2")
        result = remove_task(self.tasks, 1)
        self.assertTrue(result)
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0]["title"], "Task 2")

    def test_remove_invalid_index(self):
        add_task(self.tasks, "Task 1")
        result = remove_task(self.tasks, 5)
        self.assertFalse(result)
        self.assertEqual(len(self.tasks), 1)

    def test_save_and_load_tasks(self):
        add_task(self.tasks, "Task persistent A")
        add_task(self.tasks, "Task persistent B")
        toggle_task_status(self.tasks, 2)

        save_tasks(self.tasks, self.test_file)
        loaded = load_tasks(self.test_file)

        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0]["title"], "Task persistent A")
        self.assertFalse(loaded[0]["completed"])
        self.assertEqual(loaded[1]["title"], "Task persistent B")
        self.assertTrue(loaded[1]["completed"])

    def test_load_nonexistent_file(self):
        loaded = load_tasks("nonexistent_file_xyz.txt")
        self.assertEqual(loaded, [])


if __name__ == "__main__":
    unittest.main()
