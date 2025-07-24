# Главный файл
# Отвечает за запуск приложения
#----------------------------------------------------
from controllers.task_controller import TaskController
from views.cli_view import CLIView

def main():
    # Инициализация контроллера задач и представления
    controller = TaskController()
    view = CLIView()

    while True:
        # Получение пользовательского ввода для добавления новой задачи
        user_input = view.get_user_input()
        if user_input.lower() == 'exit':
            break # Выход из цикла если пользователь ввёл 'exit'

        # Получение описания задачи и добавления её в контроллер
        description = view.get_task_description()
        controller.add_task(user_input, description)
        view.display_tasks(controller.get_tasks())
        
        # Запрос на завершение задачи
        complete_action = input("Хотите завершить задачу? (да/нет): ").strip().lower()
        if complete_action == "да":
            index = view.get_task_to_complete()
            controller.complete_task(index)

        # Запрос на изменение или удаление задачи
        action = input("Хотите изменить или удалить задачу? (изменить/удалить/нет): ").strip().lower()
        if action == "изменить":
            index = view.get_task_index()
            new_title = input("Введите новый заголовок (или оставьте пустым для сохранения): ")
            new_description = input("Введите новое описание (или оставьте пустым для сохранения): ")
            # Обновление задачи с новыми данными если они предоставлены
            controller.update_task(index,  
                                   new_title if new_title else None, 
                                   new_description if new_description else None)
        elif action == "удалить":
            index = view.get_task_index() # Получение индекса задачи для удаление
            controller.remove_task(index) # Удаление задачи

        view.display_tasks(controller.get_tasks()) # Отображение обновленного списка задач

if __name__ == "__main__":
    main() # Запуск главной функции
