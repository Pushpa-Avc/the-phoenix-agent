
import os

class TodoManager:
    def __init__(self, todo_file="todo.md"):
        self.todo_file = todo_file
        self._ensure_todo_file_exists()

    def _ensure_todo_file_exists(self):
        if not os.path.exists(self.todo_file):
            with open(self.todo_file, "w") as f:
                f.write("# Agent Todo List\n\n")

    def add_task(self, task):
        with open(self.todo_file, "a") as f:
            f.write(f"- [ ] {task}\n")

    def get_tasks(self):
        with open(self.todo_file, "r") as f:
            content = f.read()
        return content

    def clear_tasks(self):
        with open(self.todo_file, "w") as f:
            f.write("# Agent Todo List\n\n")

    def update_task_status(self, task_description, new_status):
        with open(self.todo_file, 'r') as f:
            lines = f.readlines()

        updated_lines = []
        found = False
        for line in lines:
            if task_description in line and line.strip().startswith('- ['):
                if new_status == 'done':
                    updated_lines.append(line.replace('- [ ]', '- [x]'))
                    found = True
                elif new_status == 'pending':
                    updated_lines.append(line.replace('- [x]', '- [ ]'))
                    found = True
                else:
                    updated_lines.append(line)
            else:
                updated_lines.append(line)

        if found:
            with open(self.todo_file, 'w') as f:
                f.writelines(updated_lines)
            return True
        return False
