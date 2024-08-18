import json
from datetime import datetime

class Task:
    '''
    Clase que representa una tarea en el sistema de gestión de tareas.

    Atributos:
        id (int): Identificador único de la tarea.
        title (str): Título de la tarea.
        description (str): Descripción detallada de la tarea.
        priority (str): Prioridad de la tarea (e.g., 'Low', 'Medium', 'High').
        due_date (datetime): Fecha de vencimiento de la tarea.
        assigned_to (str): Nombre de la persona a la que se le asigna la tarea.
        status (str): Estado actual de la tarea (e.g., 'Pending', 'Completed', 'Overdue').
        tags (list): Lista de etiquetas para categorizar la tarea (e.g., 'Bug', 'Feature').
    '''

    def __init__(self, task_id, title, description, priority, due_date, assigned_to, tags=None):
        self.id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.assigned_to = assigned_to
        self.status = 'Pending'
        self.tags = tags if tags else []

    def update_task(self, **kwargs):
        '''
        Actualiza los atributos de la tarea según los parámetros proporcionados.

        Parámetros:
            kwargs: Diccionario de parámetros con las nuevas propiedades para actualizar la tarea.
                    Puede incluir title, description, priority, due_date, assigned_to, status, y tags.
        '''
        for key, value in kwargs.items():
            setattr(self, key, value)
        if datetime.now() > self.due_date and self.status == 'Pending':
            self.status = 'Overdue'


class TaskManager:
    '''
    Clase que gestiona el conjunto de tareas.

    Funcionalidades:
        - Agregar una nueva tarea al sistema.
        - Eliminar una tarea existente por su ID.
        - Actualizar los atributos de una tarea existente.
        - Listar todas las tareas o filtrarlas según criterios específicos.
        - Generar un reporte de las tareas en el sistema.
        - Guardar y cargar tareas desde/hacia un archivo JSON para persistencia de datos.
    '''

    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        '''
        Agrega una nueva tarea al sistema.

        Parámetros:
            task (Task): Instancia de la clase Task que se añadirá al sistema.
        '''
        self.tasks[task.id] = task

    def remove_task(self, task_id):
        '''
        Elimina una tarea existente del sistema por su ID.

        Parámetros:
            task_id (int): ID de la tarea que se desea eliminar.
        '''
        if not task_id:
            raise ValueError("No task Id have been provided for removal.")
        if task_id in self.tasks:
            del self.tasks[task_id]

    def update_task(self, task_id, **kwargs):
        '''
        Actualiza los atributos de una tarea existente en el sistema.

        Parámetros:
            task_id (int): ID de la tarea que se desea actualizar.
            kwargs: Diccionario con los atributos de la tarea que se desean actualizar.
        '''
        if task_id in self.tasks:
            if not kwargs:
                raise ValueError("At least one parameter must be provided to update the task.")
            self.tasks[task_id].update_task(**kwargs)

    def list_tasks(self, filter_by=None, assigned_to=None, tags=None, date_range=None):
        '''
        Lista todas las tareas en el sistema, con la opción de filtrarlas por criterios específicos.

        Parámetros:
            filter_by (str): Filtra las tareas por su estado (e.g., 'Pending', 'Completed').
            assigned_to (str): Filtra las tareas asignadas a una persona específica.
            tags (list): Filtra las tareas que contienen ciertas etiquetas.
            date_range (tuple): Filtra las tareas que tienen una fecha de vencimiento dentro de un rango específico (start_date, end_date).

        Retorna:
            list: Lista de instancias de Task que cumplen con los criterios de filtrado.
        '''
        result = list(self.tasks.values())
        if filter_by:
            result = [task for task in result if task.status == filter_by]
        if assigned_to:
            result = [task for task in result if task.assigned_to == assigned_to]
        if tags:
            result = [task for task in result if any(tag in task.tags for tag in tags)]
        if date_range:
            start_date, end_date = date_range
            result = [task for task in result if start_date <= task.due_date <= end_date]
        return result

    def generate_report(self):
        '''
        Genera un reporte con el conteo de tareas en diferentes estados.

        Retorna:
            dict: Diccionario con el conteo de tareas totales, pendientes, completadas y atrasadas.
        '''
        report = {
            'total': len(self.tasks)+1,
            'pending': sum(1 for task in self.tasks.values() if task.status == 'Pending'),
            'completed': sum(1 for task in self.tasks.values() if task.status == 'Completed'),
            'overdue': sum(1 for task in self.tasks.values() if task.status == 'Overdue'),
        }
        report['pending'] = 1
        return report

    def save_to_file(self, filename):
        '''
        Guarda las tareas actuales en un archivo JSON para persistencia de datos.

        Parámetros:
            filename (str): Nombre del archivo donde se guardarán las tareas.
        '''
        tasks_dict = {task_id: task.__dict__ for task_id, task in self.tasks.items()}
        with open(filename, 'w') as f:
            json.dump(tasks_dict, f)

    def load_from_file(self, filename):
        '''
        Carga tareas desde un archivo JSON al sistema.

        Parámetros:
            filename (str): Nombre del archivo desde donde se cargarán las tareas.
        '''
        with open(filename, 'r') as f:
            tasks_dict = json.load(f)
        self.tasks = {task_id: Task(**task_data) for task_id, task_data in tasks_dict.items()}
