
from core.reflection import ReflectionAgent
from core.planning import PlanningAgent
from core.todo_manager import TodoManager
from brain.memory import Memory
from tools.tool_registry import ToolRegistry

class DailyEvolution:
    def __init__(self):
        self.reflection_agent = ReflectionAgent()
        self.planning_agent = PlanningAgent()
        self.todo_manager = TodoManager()
        self.memory = Memory()
        self.tool_registry = ToolRegistry()

        # Register dummy tools with metadata
        self.tool_registry.register_tool(
            "research_tool",
            self._dummy_research_tool,
            description="Researches a given query and returns results.",
            input_schema={"type": "string", "description": "The research query."},
            output_schema={"type": "string", "description": "The research results."}
        )
        self.tool_registry.register_tool(
            "develop_tool",
            self._dummy_develop_tool,
            description="Develops a feature based on a given task.",
            input_schema={"type": "string", "description": "The development task."},
            output_schema={"type": "string", "description": "Development status."}
        )
        self.tool_registry.register_tool(
            "test_tool",
            self._dummy_test_tool,
            description="Runs tests for a given component.",
            input_schema={"type": "string", "description": "The component to test."},
            output_schema={"type": "string", "description": "Test results."}
        )

    def _dummy_research_tool(self, query):
        print(f"Executing research tool with query: {query}")
        result = "Research results for " + query
        self.memory.add_finding(f"Research Query: {query}", result)
        return result

    def _dummy_develop_tool(self, task):
        print(f"Executing development tool for task: {task}")
        result = "Development complete for " + task
        self.memory.add_decision(f"Development Task: {task}", result)
        return result

    def _dummy_test_tool(self, component):
        print(f"Executing test tool for component: {component}")
        result = "Tests passed for " + component
        self.memory.add_decision(f"Test Component: {component}", result)
        return result

    def run_daily_evolution(self, previous_task_result, current_repository_state):
        print("Starting daily evolution protocol...")

        # Add initial task to todo list
        self.todo_manager.add_task("Perform daily evolution protocol")

        # 1. Reflect
        improvement_suggestion = self.reflection_agent.reflect(
            previous_task_result,
            current_repository_state + "\n" + self.memory.get_all_memory()["index"]
        )
        print(f"Reflection suggested: {improvement_suggestion}")
        self.todo_manager.add_task(f"Address reflection: {improvement_suggestion}")

        # 2. Plan
        available_tools_info = self.tool_registry.list_tools()
        plan = self.planning_agent.plan(improvement_suggestion, available_tools_info)
        print(f"Generated plan: {plan}")
        self.todo_manager.add_task(f"Execute plan: {plan}")

        # 3. Execute Plan
        for task_name in plan:
            retries = 3
            tool_executed = False
            for attempt in range(retries):
                tool_function = self.tool_registry.get_tool(task_name.replace("_subtask", "_tool"))
                if tool_function:
                    try:
                        print(f"Executing tool: {task_name} (attempt {attempt+1}/{retries})")
                        # For now, assuming tools take the task_name as input
                        result = tool_function(task_name)
                        print(f"Tool execution result: {result}")
                        self.todo_manager.update_task_status(f"Execute plan: {plan}", "done")
                        tool_executed = True
                        break  # Break from retry loop on success
                    except Exception as e:
                        print(f"Tool execution failed for {task_name} (attempt {attempt+1}/{retries}): {e}")
                        if attempt == retries - 1:
                            self.todo_manager.add_task(f"Failed to execute tool after multiple retries: {task_name}")
                else:
                    print(f"Tool not found for task: {task_name}")
                    self.todo_manager.add_task(f"Failed to execute tool: {task_name}")
                    tool_executed = True # Mark as executed to avoid further retries for non-existent tool
                    break
            if not tool_executed:
                self.todo_manager.add_task(f"Failed to execute tool: {task_name} after all retries.")

        # 4. Validate (dummy for now)
        print("Running validation tests...")
        test_result = self._dummy_test_tool("all_components")
        print(f"Validation result: {test_result}")
        self.todo_manager.update_task_status("Perform daily evolution protocol", "done")

        print("Daily evolution protocol completed.")
        return "Evolution complete."

if __name__ == "__main__":
    daily_evolution = DailyEvolution()
    daily_evolution.run_daily_evolution("Previous day's task was successful.", "Repository is up-to-date.")
