course = 'Python'  # Курс, который проходит студент
count_completed_tasks = 12  # Количество выполненных задач
count_hours_spent = 1.5  # Затраченное время на выполнение задач
time_for_one_task = count_hours_spent / count_completed_tasks   # Среднее время выполнения одной задачи

print('Курс:', course + ',', 'всего задач:', str(count_completed_tasks) + ',', 'затрачено часов:', str(count_hours_spent) + ',', 'среднее время выполнения', time_for_one_task, 'часа.')

