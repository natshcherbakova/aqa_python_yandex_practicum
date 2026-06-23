new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 

completed_tasks.append(new_tasks.pop(4))

new_tasks.remove(new_tasks[2])

print('Заказчик поднял приоритет, поэтому ' + (new_tasks[2]) + ' нужно будет взять в работу следующей')