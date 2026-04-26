
class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register_tool(self, name, tool_function, description="", input_schema=None, output_schema=None):
        self.tools[name] = {
            "function": tool_function,
            "description": description,
            "input_schema": input_schema,
            "output_schema": output_schema,
        }

    def get_tool(self, name):
        tool_info = self.tools.get(name)
        return tool_info["function"] if tool_info else None

    def list_tools(self):
        return [{
            "name": name,
            "description": tool_info["description"],
            "input_schema": tool_info["input_schema"],
            "output_schema": tool_info["output_schema"],
        } for name, tool_info in self.tools.items()]
