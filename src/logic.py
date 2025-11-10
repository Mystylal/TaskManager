from typing import List, Dict

def add_task(tasks: List[Dict], task_data: Dict) -> None:
    new_id = max((t["id"] for t in tasks), default=0) + 1
    task_data["id"] = new_id
    task_data["status"] = "новая"
    tasks.append(task_data)

def change_status(tasks: List[Dict], task_id: int, new_status: str) -> bool:
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = new_status
            return True
    return False

def delete_task(tasks: List[Dict], task_id: int) -> List[Dict]:
    return [t for t in tasks if t["id"] != task_id]