
import unittest
import os
from evolution.daily_evolution import DailyEvolution
from core.todo_manager import TodoManager
from brain.memory import Memory
from tools.tool_registry import ToolRegistry

class TestPhoenixAgent(unittest.TestCase):

    def setUp(self):
        # Clean up any existing todo.md or memory.json before each test
        if os.path.exists("todo.md"):
            os.remove("todo.md")
        if os.path.exists("memory.json"):
            os.remove("memory.json")

        self.daily_evolution = DailyEvolution()
        self.todo_manager = TodoManager()
        self.memory = Memory()
        self.tool_registry = ToolRegistry()

    def tearDown(self):
        # Clean up any created files after each test
        if os.path.exists("todo.md"):
            os.remove("todo.md")
        if os.path.exists("memory.json"):
            os.remove("memory.json")

    def test_todo_manager(self):
        self.todo_manager.add_task("Test task 1")
        self.todo_manager.add_task("Test task 2")
        tasks = self.todo_manager.get_tasks()
        self.assertIn("- [ ] Test task 1", tasks)
        self.assertIn("- [ ] Test task 2", tasks)

        self.todo_manager.update_task_status("Test task 1", "done")
        tasks = self.todo_manager.get_tasks()
        self.assertIn("- [x] Test task 1", tasks)

    def test_memory(self):
        self.memory.add_finding("New AI agent architecture discovered.")
        self.memory.add_decision("Decided to implement context engineering.")
        all_memory = self.memory.get_all_memory()
        self.assertIn("New AI agent architecture discovered.", all_memory["findings"])
        self.assertIn("Decided to implement context engineering.", all_memory["decisions"])

    def test_tool_registry_with_metadata(self):
        def dummy_tool_func():
            pass
        self.tool_registry.register_tool(
            "new_tool",
            dummy_tool_func,
            description="A new dummy tool.",
            input_schema={"type": "string"}
        )
        tools_info = self.tool_registry.list_tools()
        self.assertTrue(any(tool["name"] == "new_tool" for tool in tools_info))
        new_tool_info = next(tool for tool in tools_info if tool["name"] == "new_tool")
        self.assertEqual(new_tool_info["description"], "A new dummy tool.")
        self.assertEqual(new_tool_info["input_schema"], {"type": "string"})

    def test_daily_evolution_integration(self):
        result = self.daily_evolution.run_daily_evolution("Initial run.", "Clean repository.")
        self.assertEqual(result, "Evolution complete.")

        # Verify todo.md and memory.json are updated
        tasks = self.todo_manager.get_tasks()
        self.assertIn("- [x] Perform daily evolution protocol", tasks)
        self.assertIn("- [ ] Address reflection: Consider adding a planning module to break down complex tasks.", tasks)

        all_memory = self.memory.get_all_memory()
        self.assertTrue(len(all_memory["findings"]) > 0)
        self.assertTrue(len(all_memory["decisions"]) > 0)

if __name__ == '__main__':
    unittest.main()
