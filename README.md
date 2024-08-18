# Ejercicio: Testeo de un Sistema de Gestión de Tareas

## 1. Introducción: ¿Qué es el sistema de gestión de tareas y qué hace?

El sistema de gestión de tareas es una aplicación desarrollada en Python que permite la creación, actualización y seguimiento de tareas asignadas a diferentes usuarios. Cada tarea tiene atributos como título, descripción, prioridad, fecha de vencimiento, y estado (por ejemplo, "Pending", "Overdue"). El sistema también incluye un mecanismo para verificar y actualizar el estado de las tareas automáticamente, asegurando que si una tarea no ha sido completada a tiempo, su estado cambie a "Overdue".

Este sistema es útil para gestionar proyectos y garantizar que todas las tareas se completen dentro de los plazos establecidos, proporcionando una estructura clara para la asignación y seguimiento de responsabilidades.

Encuentre toda la ayuda directamente en la librería de **[unittest](https://docs.python.org/3/library/unittest.html)**.

## 2. Descripción y Objetivo de la Actividad

El objetivo de esta actividad es evaluar las habilidades de los estudiantes en la creación y ejecución de pruebas unitarias utilizando la biblioteca `unittest` de Python. Los estudiantes deben diseñar y planificar casos de prueba que verifiquen la funcionalidad del sistema de gestión de tareas, asegurando que todas las características funcionen correctamente y que se manejen adecuadamente las situaciones de error.

## 3. Instrucciones

### 3.1 Diseño y Planeación de los Casos de Prueba

Cada caso de prueba debe estar bien definido y documentado. Asegúrate de incluir:

- **Precondiciones**: Describe el estado inicial del sistema o de los objetos involucrados antes de ejecutar el caso de prueba.
- **Acciones**: Detalla las acciones o métodos que se ejecutarán durante la prueba.
- **Poscondiciones**: Describe el estado final esperado del sistema o de los objetos involucrados después de ejecutar la prueba.

### 3.2 Requerimientos de Pruebas

1. **Prueba de Creación de Tareas**:
   - **Precondiciones**: El sistema de gestión de tareas está vacío.
   - **Acciones**: Crear una tarea con todos los campos válidos.
   - **Poscondiciones**: La tarea se crea correctamente con el estado "Pending".

2. **Prueba de Duplicación de ID de Tareas**:
   - **Precondiciones**: Existe una tarea con `task_id=1` en el sistema.
   - **Acciones**: Intentar agregar otra tarea con el mismo `task_id`.
   - **Poscondiciones**: Se lanza un `KeyError` indicando que la tarea ya existe.

3. **Prueba de Actualización de Tarea con Cambio de Estado a "Overdue"**:
   - **Precondiciones**: La tarea tiene una fecha de vencimiento pasada y su estado es "Pending".
   - **Acciones**: Intentar actualizar un atributo de la tarea.
   - **Poscondiciones**: El sistema debe cambiar el estado de la tarea a "Overdue".

4. **Prueba de Actualización de Atributos No Existentes**:
   - **Precondiciones**: Existe una tarea en el sistema.
   - **Acciones**: Intentar actualizar un atributo que no existe en la tarea (por ejemplo, `color`).
   - **Poscondiciones**: Se lanza un `AttributeError` indicando que el atributo no existe.

5. **Prueba de Creación de Tarea con Fecha de Vencimiento Pasada**:
   - **Precondiciones**: Ninguna.
   - **Acciones**: Intentar crear una tarea con una fecha de vencimiento anterior a la fecha actual.
   - **Poscondiciones**: Se lanza un `ValueError` indicando que la fecha de vencimiento debe estar en el futuro.
  
6. **Pruebas adicionales**
   - Añada las demás pruebas que sean necesarias para validar el correcto funcionamiento del sistema de gestión de tareas.

### 3.3 Implementación de las Pruebas

- Utiliza la biblioteca `unittest` para crear un conjunto de pruebas que cubra todos los casos mencionados.
- Las pruebas deben ser modulares, y cada una debe verificar un aspecto específico de la funcionalidad del sistema.

### 3.4 Ejecución de las Pruebas

- Ejecuta las pruebas y documenta los resultados, incluyendo cualquier fallo o comportamiento inesperado.

## 4. Entregables

1. **Código Fuente de las Pruebas**: El proyecto correctamente estructurado:

    ```text
    proyecto/
    ├── modules/
    │   ├── __init__.py
    │   └── tasks_manager.py
    ├── tests/
    │   ├── test_case_1.py
    │   ├── test_case_2.py
    │   └── test_case_n.py
    └── main.py
    ```

2. **Informe de Resultados**: Un documento que detalle los resultados de las pruebas, incluyendo:
   - Descripción de cada prueba.
   - Resultado de cada prueba (éxito o fallo).
   - Explicación de cualquier fallo encontrado.
   - Sugerencias de corrección o mejoras en el código si se encuentran errores.

3. **Entrega**: Entregue un archivo como sigue *apellido_nombre_psoftusb20242.zip*, que contenga el informe en pdf y el proyecto de testeo.

## 5. Ejecución de las Pruebas

Para ejecutar todas las pruebas de forma simultánea, utiliza el siguiente comando en la terminal:

```bash
$python -m unittest tests -v
```

Para ejecutar una prueba individual:

```bash
$python -m unittest tests/test_1.py -v
```

## 5. Criterios de Evaluación

- **Cobertura de Pruebas (40%)**: Grado en que las pruebas cubren todos los aspectos críticos de la funcionalidad del sistema.
- **Calidad del Código de Pruebas (20%)**: Claridad, organización y cumplimiento de las buenas prácticas en la implementación de las pruebas unitarias.
- **Documentación (20%)**: Calidad y claridad del informe de resultados, incluyendo descripciones detalladas de las pruebas, resultados obtenidos y análisis de cualquier fallo.
- **Ejecución y Resultados (20%)**: Correcta ejecución de las pruebas, incluyendo la identificación de cualquier error en el código y la precisión en los resultados reportados.

## 6. Fecha de entrega

Domingo 25, 23:59. Adjdunte su .zip en la carpeta "Entregas/caso de estudio 1".
