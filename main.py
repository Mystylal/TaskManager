from src import data, logic, ui
from typing import List, Dict

def main() -> None:
    tasks: List[Dict] = data.load_tasks()

    while True:
        choice = ui.show_menu()

        if choice == "1":
            task_data = ui.get_task_input()
            logic.add_task(tasks, task_data)

        elif choice == "2":
            if not tasks:
                print("Список пуст")
            else:
                for t in tasks:
                    print(f"{t['id']}. {t['name']} — {t['status']}")

        elif choice == "3":
            try:
                task_id = int(input("ID задачи: "))
                new_status = input("Новый статус: ")
                ok = logic.change_status(tasks, task_id, new_status)
                if not ok:
                    print("Не найдено")
            except ValueError:
                print("Неверный ввод")

        elif choice == "4":
            try:
                task_id = int(input("ID задачи: "))
                tasks = logic.delete_task(tasks, task_id)
            except ValueError:
                print("Неверный ввод")

        elif choice == "q":
            data.save_tasks(tasks)
            print("Сохранено. Выход.")
            break

        else:
            print("Нет такого пункта")

if __name__ == "__main__":
    main()