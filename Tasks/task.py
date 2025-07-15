class Task:
    """A single checklist task"""
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed
        
    def mark_completed(self):
        "Mark as completed"
        self.completed = True
        
    def mark_incomplete(self):
        "Mark as incompleted"
        self.completed = False
        
    def get_status_symbol(self):
        "Returns fitting symbol"
        return "V" if self.completed else "X"
    
    def to_dict(self):
        "Convert to dict for json serialization"
        return {
            'description': self.description,
            'completed': self.completed
        }
        
    @classmethod
    def from_dict(cls, data):
        "Create task from dict"
        return cls(data['description'], data['completed'])
    
    def __str__(self):
        return f"{self.description} {self.get_status_symbol()}"
        