class ProjectManager:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.projects = []  # Lista que contiene todos los proyectos

    def create_project(self, name, description, budget, members):
        current_user = self.user_manager.get_current_user()  # Obtenemos el usuario activo
        if not current_user:
            return False  # Si no hay usuario activo, no podemos crear el proyecto

        project_id = len(self.projects) + 1  # ID único basado en la longitud de la lista (número entero)
        project = {
            "id": project_id,  # Usamos un número entero como ID
            "name": name,
            "description": description,
            "budget": budget,
            "expenses": 0.0,  # El presupuesto inicial
            "members": members + [current_user],  # El creador del proyecto es parte del equipo
            "tasks": [],  # Inicialmente no hay tareas
            "suggestions": []  # No hay sugerencias aún
        }

        self.projects.append(project)  # Añadimos el proyecto a la lista de proyectos
        return project  # Devolvemos el proyecto creado con su ID

    def get_all_projects(self):
        return self.projects  # Devuelve la lista de todos los proyectos

    def get_project(self, name):
        for project in self.projects:
            if project['name'] == name:
                return project
        return None

    def get_project_by_id(self, project_id):
        # Ahora el ID es un número entero, así que comparamos como números
        for project in self.projects:
            if project['id'] == project_id:
                return project
        return None

    def modify_project(self, project_name, new_name, new_description, new_budget, new_expenses, new_members):
        project = self.get_project(project_name)
        if project:
            project["name"] = new_name
            project["description"] = new_description
            project["budget"] = new_budget
            project["expenses"] = new_expenses
            project["members"] = new_members
            return True
        return False

    def delete_project(self, project_id):
        for i, project in enumerate(self.projects):
            if project['id'] == project_id:
                del self.projects[i]
                return True  # Indica que el proyecto fue eliminado exitosamente
        return False  # Indica que no se encontró el proyecto
    
    def update_budget_and_expenses(self, project_name, new_expenses):
        project = self.get_project(project_name)
        if project:
            project["expenses"] = new_expenses
            # Actualiza el balance basado en el presupuesto y los gastos
            project["balance"] = project["budget"] - new_expenses
            return True
        return False

    def view_project_details(self, project_name):
        project = self.get_project(project_name)
        if project:
            details = (
                f"Nombre: {project['name']}\n"
                f"Descripción: {project['description']}\n"
                f"Presupuesto: {project['budget']}\n"
                f"Gastos: {project['expenses']}\n"
                f"Balance: {project['budget'] - project['expenses']}\n"  # Balance calculado correctamente
                f"Miembros del Equipo: {', '.join(project['members'])}\n"  # Usar 'members'
                f"Tareas Asignadas:\n"
            )

            # Muestra las tareas asignadas
            if project['tasks']:
                for task in project['tasks']:
                    details += f"- Tarea: {task['task']}, Equipo: {task['team']}\n"
            else:
                details += "No hay tareas asignadas aún.\n"

            return details
        return None

    # Método para asignar una tarea a un proyecto
    def assign_task_to_project(self, project_name, task, team):
        project = self.get_project(project_name)
        if project:
            # Asignamos la tarea al proyecto
            project['tasks'].append({
                "task": task,
                "team": team
            })
            return True
        return False
