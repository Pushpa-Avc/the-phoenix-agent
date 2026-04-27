
from brain.memory import Memory
from core.todo_manager import TodoManager

class PlanningAgent:
    def __init__(self):
        self.memory = Memory()
        self.todo_manager = TodoManager()

    def plan(self, goal, available_tools):
        print(f"Planning for goal: {goal}")
        print(f"Available tools: {available_tools}")

        plan_description = f"Planned for goal: {goal} with tools: {available_tools}"
        self.memory.add_decision(f"Plan for {goal}", plan_description)
        self.todo_manager.add_task(f"Plan generated for: {goal}")

        # For now, let's just return a dummy plan.
        # In a real scenario, this would involve more sophisticated logic
        # to select and order tools based on the goal and available_tools metadata.
        return ["research_subtask", "develop_subtask", "test_subtask"]
