from modules import Task, TaskManager
from datetime import datetime

task_manager = TaskManager()
task1 = Task(1, 'Task 1', 'Description 1', 'High', datetime(2024, 8, 20), 'Alice', tags=['Feature'])
task2 = Task(2, 'Task 2', 'Description 2', 'Medium', datetime(2024, 8, 15), 'Bob', tags=['Bug'])

task_manager.add_task(task1)
task_manager.add_task(task2)

print("Report after adding tasks:")
print(task_manager.generate_report())