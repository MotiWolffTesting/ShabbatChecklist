from Files.file_manager import FileManager
from Tasks.task_manager import TaskManager
from UI.user_interface import UserInterface

class Main:
    """Main Application"""
    def __init__(self):
        self.task_manager = TaskManager()
        self.file_manager = FileManager()
        self.ui = UserInterface()
        self.load_checklist()
        
    def load_checklist(self):
        "Load checklist from file, or create default if file doesn't exist"
        tasks, file_existed = self.file_manager.load_tasks()
        
        if file_existed and tasks:
            self.task_manager.tasks = tasks
            self.ui.show_message("Checklist loaded from file.")
        else:
            self.task_manager.init_default_tasks()
            self.ui.show_message("Created new checklist with default tasks.")
            
    def save_checklist(self):
        "Save checklist to file"
        if self.task_manager.is_empty():
            self.ui.show_message("No tasks to mark as completed.")
            return
        
        self.ui.display_checklist(self.task_manager)
        task_index = self.ui.get_task_number(
            "Enter the number of the task to mark as completed: ",
            self.task_manager.get_task_count()
        )
        
        if task_index is not None:
            if self.task_manager.mark_task_completed(task_index):
                task_description = self.task_manager.tasks[task_index].description
                self.ui.show_message(f"Task '{task_description}' marked as completed!")
    
    def mark_task_completed(self):
        "Handle marking a task as completed"
        if self.task_manager.is_empty():
            self.ui.show_message("No tasks to mark as completed.")
            return
        
        self.ui.display_checklist(self.task_manager)
        task_index = self.ui.get_task_number(
            "Enter the number of the task to mark as completed: ",
            self.task_manager.get_task_count()
        )
        
        if task_index is not None:
            if self.task_manager.mark_task_completed(task_index):
                task_description = self.task_manager.tasks[task_index].description
                self.ui.show_message(f"Task '{task_description}' marked as completed! ✔️")
    
    def add_task(self):
        "Handle adding a new task"
        description = self.ui.get_new_task_description()
        if self.task_manager.add_task(description):
            self.ui.show_message(f"Task '{description}' added to the checklist!")
        else:
            self.ui.show_message("Task cannot be empty.")
    
    def remove_task(self):
        "Handle removing a task"
        if self.task_manager.is_empty():
            self.ui.show_message("No tasks to remove.")
            return
        
        self.ui.display_checklist(self.task_manager)
        task_index = self.ui.get_task_number(
            "Enter the number of the task to remove: ",
            self.task_manager.get_task_count()
        )
        
        if task_index is not None:
            removed_task = self.task_manager.remove_task(task_index)
            if removed_task:
                self.ui.show_message(f"Task '{removed_task.description}' removed from the checklist!")
    
    def reset_completed_tasks(self):
        "Handle resetting all tasks"
        self.task_manager.reset_all_tasks()
        self.ui.show_message("All tasks reset to not completed.")
    
    def run(self):
        "Main program loop"
        self.ui.show_message("Welcome to the Shabbat Preparation Checklist Manager!")
        
        while True:
            self.ui.show_menu()
            choice = self.ui.get_user_choice()
            
            if choice == '1':
                self.ui.display_checklist(self.task_manager)
            elif choice == '2':
                self.mark_task_completed()
            elif choice == '3':
                self.add_task()
            elif choice == '4':
                self.remove_task()
            elif choice == '5':
                self.reset_completed_tasks()
            elif choice == '6':
                if self.save_checklist():
                    self.ui.show_message("Goodbye! Shabbat Shalom!")
                    break
            elif choice == '7':
                self.ui.show_message("Exiting without saving. Shabbat Shalom!")
                break
            else:
                self.ui.show_message("Invalid option. Please choose 1-7.")


def main():
    "Main function to run the program"
    checklist = Main()
    checklist.run()


if __name__ == "__main__":
    main()