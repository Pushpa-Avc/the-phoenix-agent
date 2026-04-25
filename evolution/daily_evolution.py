
from core.reflection import ReflectionAgent
from core.planning import PlanningAgent
from tools.tool_registry import ToolRegistry

class DailyEvolution:
    def __init__(self):
        self.reflection_agent = ReflectionAgent()
        self.planning_agent = PlanningAgent()
        self.tool_registry = ToolRegistry()

        # Register dummy tools for demonstration
        self.tool_registry.register_tool("research_tool", self._dummy_research_tool)
        self.tool_registry.register_tool("develop_tool", self._dummy_develop_tool)
        self.tool_registry.register_tool("test_tool", self._dummy_test_tool)

    def _dummy_research_tool(self, query):
        print(f"Executing research tool with query: {query}")
        return "Research results for " + query

    def _dummy_develop_tool(self, task):
        print(f"Executing development tool for task: {task}")
        return "Development complete for " + task

    def _dummy_test_tool(self, component):
        print(f"Executing test tool for component: {component}")
        return "Tests passed for " + component

    def run_daily_evolution(self, previous_task_result, current_repository_state):
        print("Starting daily evolution protocol...")

        # 1. Reflect
        improvement_suggestion = self.reflection_agent.reflect(previous_task_result, current_repository_state)
        print(f"Reflection suggested: {improvement_suggestion}")

        # 2. Plan
        plan = self.planning_agent.plan(improvement_suggestion, self.tool_registry.list_tools())
        print(f"Generated plan: {plan}")

        # 3. Execute Plan (Develop)
        for task in plan:
            tool = self.tool_registry.get_tool(task.replace("_subtask", "_tool"))
            if tool:
                result = tool(task)
                print(f"Tool execution result: {result}")
            else:
                print(f"Tool not found for task: {task}")

        # 4. Validate (dummy for now)
        print("Running validation tests...")
        test_result = self._dummy_test_tool("all_components")
        print(f"Validation result: {test_result}")

        print("Daily evolution protocol completed.")
        return "Evolution complete."

if __name__ == "__main__":
    daily_evolution = DailyEvolution()
    daily_evolution.run_daily_evolution("Previous day's task was successful.", "Repository is up-to-date.")
