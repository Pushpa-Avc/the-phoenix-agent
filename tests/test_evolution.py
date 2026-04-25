
import unittest
from core.reflection import ReflectionAgent
from core.planning import PlanningAgent
from tools.tool_registry import ToolRegistry
from evolution.daily_evolution import DailyEvolution

class TestPhoenixAgent(unittest.TestCase):
    def test_reflection_agent(self):
        agent = ReflectionAgent()
        suggestion = agent.reflect("test result", "test state")
        self.assertIsInstance(suggestion, str)
        self.assertTrue(len(suggestion) > 0)

    def test_planning_agent(self):
        agent = PlanningAgent()
        plan = agent.plan("test goal", ["tool1", "tool2"])
        self.assertIsInstance(plan, list)
        self.assertTrue(len(plan) > 0)

    def test_tool_registry(self):
        registry = ToolRegistry()
        registry.register_tool("test_tool", lambda x: x)
        self.assertEqual(registry.get_tool("test_tool")("hello"), "hello")
        self.assertIn("test_tool", registry.list_tools())

    def test_daily_evolution(self):
        evolution = DailyEvolution()
        result = evolution.run_daily_evolution("success", "stable")
        self.assertEqual(result, "Evolution complete.")

if __name__ == "__main__":
    unittest.main()
