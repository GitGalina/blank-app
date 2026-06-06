import streamlit as st

st.title("🎈 My new app")
st.write("StreamLit приложение🎈 ")

from ipywidgets import widgets, VBox, HBox, Layout
from IPython.display import display

# 1. Инициализируем список задач (словарь: название -> статус выполнения)
tasks = []

# 2. Создаем виджеты интерфейса

# Поле ввода новой задачи
task_input = widgets.Text(
    placeholder='Введите новую задачу...',
    layout=Layout(width='300px')
)

# Кнопка добавления задачи
add_button = widgets.Button(
    description='Добавить',
    button_style='success'
)

# Кнопка очистки выполненных задач
clear_done_button = widgets.Button(
    description='Удалить выполненные',
    button_style='warning'
)

# Область вывода списка задач
output = widgets.Output()

# 3. Функция для обновления отображения списка
def update_display():
    with output:
        output.clear_output()
        for i, task in enumerate(tasks):
            checkbox = widgets.Checkbox(
                value=task['done'],
                description=task['name'],
                layout=Layout(margin='5px 0')
            )
            # Связываем чекбокс с логикой обновления статуса
            checkbox.observe(lambda change, idx=i: update_task_status(idx, change['new']), names='value')
            display(checkbox)

# 4. Обработчики событий

def add_task(b):
    if task_input.value.strip():
        tasks.append({'name': task_input.value, 'done': False})
        task_input.value = ''  # Очищаем поле
        update_display()

def clear_done_tasks(b):
    global tasks
    tasks = [task for task in tasks if not task['done']]
    update_display()

def update_task_status(index, new_status):
    tasks[index]['done'] = new_status
    update_display()

# 5. Назначаем обработчики кнопкам
add_button.on_click(add_task)
clear_done_button.on_click(clear_done_tasks)

# 6. Собираем интерфейс в единую структуру
input_box = HBox([task_input, add_button])
control_box = HBox([clear_done_button])

# Вертикальное расположение: ввод -> список -> управление
full_ui = VBox([
    input_box,
    output,
    control_box
], layout=Layout(margin='20px'))

# 7. Отображаем интерфейс
display(full_ui)
