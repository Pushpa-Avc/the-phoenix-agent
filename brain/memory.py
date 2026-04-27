
import json
import os
import datetime

class Memory:
    def __init__(self, knowledge_dir="knowledge"):
        self.knowledge_dir = knowledge_dir
        self.pages_dir = os.path.join(knowledge_dir, "pages")
        self.index_file = os.path.join(knowledge_dir, "index.md")
        self.log_file = os.path.join(knowledge_dir, "log.md")
        self._ensure_knowledge_structure_exists()

    def _ensure_knowledge_structure_exists(self):
        os.makedirs(self.pages_dir, exist_ok=True)
        if not os.path.exists(self.index_file):
            with open(self.index_file, "w") as f:
                f.write("# Knowledge Index\n\n")
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as f:
                f.write("# Evolution Log\n\n")

    def _add_to_log(self, entry_type, content):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"## [{timestamp}] {entry_type} | {content}\n\n")

    def add_finding(self, finding_title, finding_content):
        # Create a new page for the finding
        filename = finding_title.lower().replace(" ", "_").replace(".", "") + ".md"
        filepath = os.path.join(self.pages_dir, filename)
        with open(filepath, "w") as f:
            f.write(f"# {finding_title}\n\n{finding_content}\n")
        
        # Add to index
        with open(self.index_file, "a") as f:
            f.write(f"- [{finding_title}](pages/{filename})\n")
            
        self._add_to_log("Finding Added", finding_title)

    def add_decision(self, decision_title, decision_content):
        # Create a new page for the decision
        filename = decision_title.lower().replace(" ", "_").replace(".", "") + ".md"
        filepath = os.path.join(self.pages_dir, filename)
        with open(filepath, "w") as f:
            f.write(f"# {decision_title}\n\n{decision_content}\n")
            
        # Add to index
        with open(self.index_file, "a") as f:
            f.write(f"- [{decision_title}](pages/{filename})\n")
            
        self._add_to_log("Decision Made", decision_title)

    def get_all_memory(self):
        # For now, just return the log and index content
        with open(self.index_file, "r") as f:
            index_content = f.read()
        with open(self.log_file, "r") as f:
            log_content = f.read()
        return {"index": index_content, "log": log_content}

    def clear_memory(self):
        # This will clear the index and log, but not individual pages for now
        with open(self.index_file, "w") as f:
            f.write("# Knowledge Index\n\n")
        with open(self.log_file, "w") as f:
            f.write("# Evolution Log\n\n")
        # TODO: Add logic to clear all pages in the future if needed
