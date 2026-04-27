
from brain.memory import Memory
from core.todo_manager import TodoManager

class ReflectionAgent:
    def __init__(self):
        self.memory = Memory()
        self.todo_manager = TodoManager()

    def reflect(self, previous_task_result, current_repository_state):
        print("Performing reflection...")
        print(f"Previous task result: {previous_task_result}")
        print(f"Current repository state: {current_repository_state}")
        
        finding_title = "Reflection on Daily Evolution"
        finding_content = f"Reflection performed with previous result: {previous_task_result} and state: {current_repository_state}"
        self.memory.add_finding(finding_title, finding_content)
        self.todo_manager.add_task("Reflection completed.")

        # For now, let's just return a dummy improvement suggestion.
        return "Consider adding a planning module to break down complex tasks."
