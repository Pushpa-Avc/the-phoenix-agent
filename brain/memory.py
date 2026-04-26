
import json
import os

class Memory:
    def __init__(self, memory_file="memory.json"):
        self.memory_file = memory_file
        self._ensure_memory_file_exists()

    def _ensure_memory_file_exists(self):
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, "w") as f:
                json.dump({"findings": [], "decisions": []}, f)

    def add_finding(self, finding):
        with open(self.memory_file, "r+") as f:
            data = json.load(f)
            data["findings"].append(finding)
            f.seek(0)
            json.dump(data, f, indent=4)

    def add_decision(self, decision):
        with open(self.memory_file, "r+") as f:
            data = json.load(f)
            data["decisions"].append(decision)
            f.seek(0)
            json.dump(data, f, indent=4)

    def get_all_memory(self):
        with open(self.memory_file, "r") as f:
            return json.load(f)

    def clear_memory(self):
        with open(self.memory_file, "w") as f:
            json.dump({"findings": [], "decisions": []}, f)
