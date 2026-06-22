new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 

# Перенос задачи из списка в другой список и удаление его из первоначального списка
completed_tasks.append(new_tasks.pop(4))

# Удаление задачи из списка
new_tasks.remove(new_tasks[2])

# Список задач 
print('Заказчик поднял приоритет, поэтому ' + (new_tasks[2]) + ' нужно будет взять в работу следующей')