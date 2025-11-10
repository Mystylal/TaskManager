import json, os
from typing import List, Dict

FILE = "tasks.json"

def load_tasks() -> List[Dict]:
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks: List[Dict]) -> None:
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)   