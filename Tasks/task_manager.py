from Tasks.task import Task

class TaskManager:
    """Manage all tasks"""
    def __init__(self):
        self.tasks = []
        self.default_tasks = [
            "Buy challah",
            "Cook cholent",
            "Light Candles",
            "Set the table",
            "Turn off phone"
        ]
        
    def init_default_tasks(self):
        "Initiate list with default tasks"
        self.tasks = [Task(description) for description in self.default_tasks]
        
    def add_task(self, description):
        "Add new task"
        if description.strip():
            task = Task(description.strip())
            self.tasks.append(task)
            return True
        return False
    
    def remove_task(self, index):
        "Remove task"
        if 0 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index)
            return removed_task
        return None
    
    def mark_task_completed(self, index):
        "Mark task as completed by index"
        if 0 <= index <= len(self.tasks):
            self.tasks[index].mark_completed()
            return True
        return False
    
    def reset_all_tasks(self):
        "Reseting tasks"
        for task in self.tasks:
            task.mark_incomplete()
            
    def get_task_count(self):
        "Get amount of tasks"
        return len(self.tasks)
    
    def get_completed_count(self):
        "Get completed amount"
        return sum(1 for task in self.tasks if task.completed)
    
    def is_empty(self):
        "Check if list is empty"
        return len(self.tasks) == 0
    
    