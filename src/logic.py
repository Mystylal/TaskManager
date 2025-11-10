def add_task(tasks, task_data):
    new_id = max([t["id"] for t in tasks], default=0) + 1
    task_data["id"] = new_id
    task_data["status"] = "новая"
    tasks.append(task_data)

def change_status(tasks, task_id, new_status):
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = new_status
            return True
    return False

def delete_task(tasks, task_id):
    return [t for t in tasks if t["id"] != task_id]