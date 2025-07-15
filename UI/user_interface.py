from ..Tasks.task_manager import TaskManager

class UserInterface:
    """Handles all user interactions and display"""
    
    @staticmethod
    def display_checklist(task_manager=TaskManager()):
        "Display the checklist with numbers and completion status"
        print("\n == Shabbat Preparation Checklist == ")
        if task_manager.is_empty():
            print("No tasks in the checklist.")
            return
        
        for i, task in enumerate(task_manager.tasks):
            print(f"{i + 1}. {task}")
            
        completed = task_manager.get_completed_count()
        total = task_manager.get_task_count()
        print (f"\nProgress: {completed}/{total} tasks completed.")
        
    @staticmethod
    def show_menu():
        "Display the main menu"
        print("\n=== Shabbat Checklist Manager ===")
        print("1. View checklist")
        print("2. Mark task as completed")
        print("3. Add new task")
        print("4. Remove task")
        print("5. Reset all tasks")
        print("6. Save and exit")
        print("7. Exit without saving")
        
    @staticmethod
    def get_user_choice():
        "Get user menu choice"
        return input("\nChoose an option (1-7): ").strip()
    
    @staticmethod
    def get_task_number(prompt, max_number):
        "Get a valid task number from user"
        try:
            choice = int(input(prompt))
            if 1 <= choice <= max_number:
                return choice - 1
            else:
                print(f"Invalid task number. Please enter 1-{max_number}.")
                return None
        except ValueError:
            print("Please enter a valid number.")
            return None
        
    @staticmethod
    def get_new_task_description():
        "Get description for new task"
        return input("Enter the new task: ").strip()
    
    @staticmethod
    def show_message(message):
        "Display a message to user"
        print(message)