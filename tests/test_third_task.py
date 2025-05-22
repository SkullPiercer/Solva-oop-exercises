def test_add_task(todo):
    todo.add_task('Купить хлеб')
    assert 'Купить хлеб' in todo.tasks

def test_show_tasks(todo):
    todo.add_task('Погулять с собакой')
    todo.add_task('Сделать ДЗ')
    output = todo.show_tasks()
    assert output == 'Погулять с собакой\nСделать ДЗ'

def test_remove_existing_task(todo):
    todo.add_task('Прочитать книгу')
    todo.remove_task('Прочитать книгу')
    assert 'Прочитать книгу' not in todo.tasks

def test_remove_nonexistent_task(todo):
    todo.add_task('Убрать комнату')
    todo.remove_task('Позаниматься спортом')
    assert todo.tasks == ['Убрать комнату']

def test_tasks_count(todo):
    for task_num in range(10):
        todo.add_task(f'Убрать комнату {task_num}')
    assert len(todo.tasks) == 10
    
    for task_num in range(10):
        todo.remove_task(f'Убрать комнату {task_num}')
    assert len(todo.tasks) == 0
