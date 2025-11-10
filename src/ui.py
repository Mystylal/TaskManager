from typing import Dict

def show_menu() -> str:
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Изменить статус")
    print("4. Удалить задачу")
    print("q. Выход")
    return input("> ")

def get_task_input() -> Dict:
    name = input("Название: ")
    desc = input("Описание: ")
    return {"name": name, "desc": desc}