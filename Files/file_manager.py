from ..Tasks.task import Task
from ..Tasks.task_manager import TaskManager
import json
import os

class FileManager:
    """Handle saving and loading of data"""
    def __init__(self, filename="shabbat_checklist.txt"):
        self.filename = filename
        
    def save_tasks(self, tasks):
        "Save tasks to file"
        try:
            data = {
                tasks: [task.to_dict() for task in tasks]
            }
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False
        
    def load_tasks(self):
        "Load tasks from file"
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    tasks = [Task.from_dict(task_data) for task_data in data.get('tasks', [])]
                    return tasks, True
            else:
                return [], False
            
        except Exception as e:
            print(f"Error loading file: {e}")
            return False
        