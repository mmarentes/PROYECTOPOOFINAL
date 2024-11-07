import tkinter as tk
from tkinter import messagebox, scrolledtext
from user_manager import UserManager
from project_manager import ProjectManager
from report_manager import ReportManager
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import random
import os
from errores import UsuarioMuyCortoError, LongitudContrasenaInvalidaError, ContrasenaInvalidaError
from tkinter import simpledialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter



# Lista de tareas y equipos audiovisuales
TASKS = [
    "Grabar video en exteriores",
    "Editar video promocional",
    "Diseño gráfico de portada",
    "Revisión de audio",
    "Montaje de set para grabación",
    "Creación de efectos especiales",
    "Producción de cortometraje",
    "Realización de animaciones 2D",
    "Creación de guion para comercial",
    "Grabación de voz en off",
    "Gestión de cámaras para evento",
    "Dirección de fotografía",
    "Grabación de música para fondo",
    "Edición de video para redes sociales",
    "Creación de storyboard",
    "Revisión y post-producción de audio",
    "Asesoría en colorimetría",
    "Desarrollo de software para edición",
    "Planificación de rodaje",
    "Diseño de vestuario para película"
]

TEAMS = [
    "Equipo de cámaras",
    "Equipo de edición",
    "Equipo de diseño gráfico",
    "Equipo de sonido",
    "Equipo de post-producción",
    "Equipo de dirección",
    "Equipo de animación",
    "Equipo de efectos visuales",
    "Equipo de producción",
    "Equipo de guion",
    "Equipo de fotografía",
    "Equipo de locución",
    "Equipo de maquillaje",
    "Equipo de vestuario",
    "Equipo de iluminación",
    "Equipo de movimiento de cámaras",
    "Equipo de música",
    "Equipo de planificación",
    "Equipo de grabación"
]

IMPROVEMENTS = [
    "Mejorar la calidad del sonido",
    "Utilizar mejores cámaras",
    "Optimizar la iluminación",
    "Mejorar el enfoque de las tomas",
    "Ajustar la edición para un ritmo más dinámico",
    "Incluir más transiciones en el video",
    "Mejorar el storyboard",
    "Usar música original",
    "Incorporar efectos especiales",
    "Reforzar la narrativa del guion",
    "Utilizar mejor el espacio en el set",
    "Añadir tomas más variadas",
    "Usar software de edición más avanzado",
    "Ajustar la colorimetría",
    "Incorporar animaciones",
    "Mejorar el flujo de la grabación",
    "Utilizar un formato de video más eficiente",
    "Incluir más ángulos en la grabación",
    "Añadir más detalles en los vestuarios",
    "Reducir los tiempos de producción"
]

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chamber Foto - Gestión de Proyectos")
        self.geometry("600x600")

        # Inicializa los gestores de usuarios y proyectos
        self.user_manager = UserManager()
        self.project_manager = ProjectManager(self.user_manager)
        self.report_manager = ReportManager()

        self.create_login_register()

    def create_login_register(self):
        self.clear_window()
        
        tk.Label(self, text="Usuario", font=("Arial", 12)).pack(pady=10)
        self.username_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Contraseña", font=("Arial", 12)).pack(pady=10)
        self.password_entry = tk.Entry(self, show="*", font=("Arial", 12), width=30)
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Iniciar Sesión", font=("Arial", 12), command=self.login).pack(pady=10)
        tk.Button(self, text="Registrar", font=("Arial", 12), command=self.register).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Los campos no pueden estar vacíos.")
            return

        if self.user_manager.login(username, password):
            self.main_menu()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Los campos no pueden estar vacíos.")
            return

        try:
            self.user_manager.register_user(username, password)
            messagebox.showinfo("Registro Exitoso", "Usuario registrado correctamente.")
            self.create_login_register()
        except UsuarioMuyCortoError as e:
            messagebox.showerror("Error", str(e))
        except LongitudContrasenaInvalidaError as e:
            messagebox.showerror("Error", str(e))
        except ContrasenaInvalidaError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", "El nombre de usuario ya existe.")

    def main_menu(self):
        self.clear_window()

        current_user = self.user_manager.get_current_user()
        tk.Label(self, text=f"Bienvenido, {current_user}", font=("Arial", 16)).pack(pady=20)

        tk.Button(self, text="Crear Proyecto", font=("Arial", 12), command=self.create_project).pack(pady=10)
        tk.Button(self, text="Modificar Proyecto", font=("Arial", 12), command=self.modify_project).pack(pady=10)
        tk.Button(self, text="Eliminar Proyecto", font=("Arial", 12), command=self.delete_project).pack(pady=10)
        tk.Button(self, text="Ver Proyecto", font=("Arial", 12), command=self.view_project).pack(pady=10)
        tk.Button(self, text="Generar Informe", font=("Arial", 12), command=self.generate_report).pack(pady=10)
        tk.Button(self, text="Cerrar Sesión", font=("Arial", 12), command=self.logout).pack(pady=10)

    def create_project(self):
        self.clear_window()
        tk.Label(self, text="Nombre del Proyecto", font=("Arial", 12)).pack(pady=10)
        self.project_name_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.project_name_entry.pack(pady=5)

        tk.Label(self, text="Descripción del Proyecto", font=("Arial", 12)).pack(pady=10)
        self.project_description_entry = scrolledtext.ScrolledText(self, font=("Arial", 12), width=30, height=5)
        self.project_description_entry.pack(pady=5)

        tk.Label(self, text="Presupuesto Total", font=("Arial", 12)).pack(pady=10)
        self.project_budget_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.project_budget_entry.pack(pady=5)

        tk.Label(self, text="Miembros del Equipo (separados por coma)", font=("Arial", 12)).pack(pady=10)
        self.project_members_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.project_members_entry.pack(pady=5)

        # Casilla de tareas asignadas
        tk.Label(self, text="Tareas Asignadas", font=("Arial", 12)).pack(pady=10)
        self.task_label = tk.Label(self, font=("Arial", 12))
        self.task_label.pack(pady=5)
        
        # Asignación de tareas y equipos
        self.assign_random_tasks_and_teams()

        tk.Button(self, text="Crear", font=("Arial", 12), command=self.save_new_project).pack(pady=10)
        tk.Button(self, text="Regresar al Menú Principal", font=("Arial", 12), command=self.main_menu).pack(pady=10)

    def assign_random_tasks_and_teams(self):
        # Asigna 2 tareas aleatorias
        assigned_tasks = random.sample(TASKS, 2)
        self.task_label.config(text=f"Tareas Asignadas: {assigned_tasks[0]}, {assigned_tasks[1]}")

        # Asigna 2 equipos aleatorios para las tareas
        assigned_teams = random.sample(TEAMS, 2)
        self.assigned_teams = dict(zip(assigned_tasks, assigned_teams))

    
    def save_new_project(self):
        name = self.project_name_entry.get().strip()
        description = self.project_description_entry.get("1.0", tk.END).strip()
        try:
            budget = float(self.project_budget_entry.get())
        except ValueError:
            messagebox.showerror("Error", "El presupuesto debe ser un número válido.")
            return

        members = [m.strip() for m in self.project_members_entry.get().split(",")]

        project = self.project_manager.create_project(name, description, budget, members)

        assigned_tasks_data = []
        for task, team in self.assigned_teams.items():
            improvement = random.choice(IMPROVEMENTS)
            task_data = {'task': task, 'team': team, 'improvement': improvement}
            assigned_tasks_data.append(task_data)

        project['tasks'] = assigned_tasks_data  # Guardamos las tareas asignadas en el proyecto

        messagebox.showinfo("Proyecto Creado", f"El proyecto ha sido creado correctamente. ID: {project['id']}")
        self.main_menu()



    def modify_project(self):
        self.clear_window()

        tk.Label(self, text="ID del Proyecto a Modificar", font=("Arial", 12)).pack(pady=10)
        self.project_id_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.project_id_entry.pack(pady=5)

        tk.Button(self, text="Buscar Proyecto", font=("Arial", 12), command=self.load_project_to_modify).pack(pady=10)
        tk.Button(self, text="Regresar al Menú Principal", font=("Arial", 12), command=self.main_menu).pack(pady=10)

    def load_project_to_modify(self):
        project_id = self.project_id_entry.get().strip()

        if not project_id.isdigit():
            messagebox.showerror("Error", "El ID del proyecto debe ser un número válido.")
            return

        project = self.project_manager.get_project_by_id(int(project_id))

        if project:
            self.modify_project_details(project)
        else:
            messagebox.showerror("Error", "Proyecto no encontrado.")

    def modify_project_details(self, project):
        self.clear_window()
        tk.Label(self, text="Modificar Proyecto", font=("Arial", 16)).pack(pady=10)
    
    # Mostrar campos editables
        tk.Label(self, text="Nombre del Proyecto", font=("Arial", 12)).pack(pady=10)
        self.project_name_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.project_name_entry.insert(0, project['name'])
        self.project_name_entry.pack(pady=5)

        tk.Label(self, text="Descripción del Proyecto", font=("Arial", 12)).pack(pady=10)
        self.project_description_entry = scrolledtext.ScrolledText(self, font=("Arial", 12), width=30, height=5)
        self.project_description_entry.insert("1.0", project['description'])
        self.project_description_entry.pack(pady=5)

        tk.Label(self, text="Presupuesto Total", font=("Arial", 12)).pack(pady=10)
        self.project_budget_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.project_budget_entry.insert(0, str(project['budget']))
        self.project_budget_entry.pack(pady=5)

        tk.Label(self, text="Miembros del Equipo (separados por coma)", font=("Arial", 12)).pack(pady=10)
        self.project_members_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.project_members_entry.insert(0, ", ".join(project['members']))
        self.project_members_entry.pack(pady=5)

    # Sección para gastos
        tk.Label(self, text="Gastos del Proyecto (concepto: cantidad)", font=("Arial", 12)).pack(pady=10)
    
    # Asegurar que los gastos sean una lista; si no, inicializar como lista vacía
        expenses = project.get('expenses', [])
        if not isinstance(expenses, list):
            expenses = []
    
        self.project_expenses_entry = scrolledtext.ScrolledText(self, font=("Arial", 12), width=30, height=5)
        expenses_text = "\n".join([f"{expense['concept']}: ${expense['amount']}" for expense in expenses])
        self.project_expenses_entry.insert("1.0", expenses_text)
        self.project_expenses_entry.pack(pady=5)

    # Cálculo de balance (solo lectura)
        self.update_balance_label(project)

        tk.Button(self, text="Guardar Cambios", font=("Arial", 12), command=lambda: self.save_project_changes(project)).pack(pady=10)
        tk.Button(self, text="Regresar al Menú Principal", font=("Arial", 12), command=self.main_menu).pack(pady=10)

    def update_balance_label(self, project):
    # Obtener el presupuesto
        budget = project.get('budget', 0)
    
    # Obtener los gastos, asegurándonos de que sea una lista de diccionarios
        expenses = project.get('expenses', [])
        if not isinstance(expenses, list):
            expenses = []  # Si no es una lista, inicializar como lista vacía
    
    # Calcular el total de gastos
        total_expenses = sum(expense.get('amount', 0) for expense in expenses if isinstance(expense, dict))

    # Calcular balance
        balance = budget - total_expenses

    # Mostrar el balance en la interfaz (solo lectura)
        balance_text = f"Balance: ${balance:.2f} (Presupuesto: ${budget:.2f} - Gastos: ${total_expenses:.2f})"
        if hasattr(self, 'balance_label'):
            self.balance_label.config(text=balance_text)
        else:
            self.balance_label = tk.Label(self, text=balance_text, font=("Arial", 12))
        self.balance_label.pack(pady=10)


    def save_project_changes(self, project):
        name = self.project_name_entry.get().strip()
        description = self.project_description_entry.get("1.0", tk.END).strip()
        try:
            budget = float(self.project_budget_entry.get())
        except ValueError:
            messagebox.showerror("Error", "El presupuesto debe ser un número válido.")
            return

        members = [m.strip() for m in self.project_members_entry.get().split(",")]
        
        # Guardar gastos (parsear de texto a lista de diccionarios)
        expenses_text = self.project_expenses_entry.get("1.0", tk.END).strip().split("\n")
        expenses = []
        for line in expenses_text:
            if line.strip():
                try:
                    concept, amount = line.split(":")
                    expenses.append({"concept": concept.strip(), "amount": float(amount.strip().replace("$", ""))})
                except ValueError:
                    messagebox.showerror("Error", "Formato de gasto incorrecto. Use 'concepto: cantidad'")
                    return

        project['name'] = name
        project['description'] = description
        project['budget'] = budget
        project['members'] = members
        project['expenses'] = expenses

        self.update_balance_label(project)
        messagebox.showinfo("Proyecto Modificado", "Los cambios se han guardado correctamente.")
        self.main_menu()

    # Modificar `generate_report` para incluir gastos y balance

    def delete_project(self):
        self.clear_window()

        tk.Label(self, text="ID del Proyecto a Eliminar", font=("Arial", 12)).pack(pady=10)
        self.project_id_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.project_id_entry.pack(pady=5)

        tk.Button(self, text="Eliminar Proyecto", font=("Arial", 12), command=self.confirm_delete_project).pack(pady=10)
        tk.Button(self, text="Regresar al Menú Principal", font=("Arial", 12), command=self.main_menu).pack(pady=10)

    def confirm_delete_project(self):
        project_id = self.project_id_entry.get().strip()

        if not project_id.isdigit():
            messagebox.showerror("Error", "El ID del proyecto debe ser un número válido.")
            return

        project_id = int(project_id)

    # Intentar eliminar el proyecto usando el método de ProjectManager
        if self.project_manager.delete_project(project_id):
            messagebox.showinfo("Proyecto Eliminado", "El proyecto ha sido eliminado correctamente.")
            self.main_menu()
        else:
            messagebox.showerror("Error", "Proyecto no encontrado.")

    def view_project(self):
        self.clear_window()

        tk.Label(self, text="ID del Proyecto para Ver", font=("Arial", 12)).pack(pady=10)
        self.project_id_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.project_id_entry.pack(pady=5)

        tk.Button(self, text="Ver Proyecto", font=("Arial", 12), command=self.display_project).pack(pady=10)
        tk.Button(self, text="Regresar al Menú Principal", font=("Arial", 12), command=self.main_menu).pack(pady=10)

    def display_project(self):
        project_id = self.project_id_entry.get().strip()

        if not project_id.isdigit():
            messagebox.showerror("Error", "El ID del proyecto debe ser un número válido.")
            return

        project = self.project_manager.get_project_by_id(int(project_id))

        if project:
            self.show_project_details(project)
        else:
            messagebox.showerror("Error", "Proyecto no encontrado.")

    def show_project_details(self, project):
        self.clear_window()

        tk.Label(self, text=f"Detalles del Proyecto: {project['name']}", font=("Arial", 16)).pack(pady=10)
        tk.Label(self, text=f"Descripción: {project['description']}", font=("Arial", 12)).pack(pady=5)
        tk.Label(self, text=f"Presupuesto: ${project['budget']:.2f}", font=("Arial", 12)).pack(pady=5)
        tk.Label(self, text="Miembros del equipo:", font=("Arial", 12)).pack(pady=5)
        tk.Label(self, text=", ".join(project['members']), font=("Arial", 12)).pack(pady=5)

    # Mostrar tareas asignadas
        tk.Label(self, text="Tareas Asignadas:", font=("Arial", 12)).pack(pady=5)
        for task_data in project['tasks']:
            task = task_data['task']
            team = task_data['team']
            improvement = task_data.get('improvement', "Ninguna mejora recomendada")
            tk.Label(self, text=f"- {task} (Equipo: {team}) - Mejora: {improvement}", font=("Arial", 12)).pack(pady=2)

    # Calcular gastos totales y balance
        expenses = project.get('expenses', [])
        total_expenses = sum(expense['amount'] for expense in expenses if isinstance(expense, dict))
        balance = project['budget'] - total_expenses

    # Mostrar balance y gastos en la vista de proyecto
        tk.Label(self, text=f"Gastos Totales: ${total_expenses:.2f}", font=("Arial", 12)).pack(pady=5)
        tk.Label(self, text=f"Balance: ${balance:.2f}", font=("Arial", 12)).pack(pady=5)

        tk.Button(self, text="Regresar al Menú Principal", font=("Arial", 12), command=self.main_menu).pack(pady=10)


    def generate_report(self):
        # Solicitar ID de proyecto al usuario
        project_id = tk.simpledialog.askstring("Informe de Proyecto", "Ingresa el ID del Proyecto para el informe:")

        if not project_id:
            return

        # Cargar el proyecto
        project = self.project_manager.get_project_by_id(int(project_id))
        if not project:
            messagebox.showerror("Error", "Proyecto no encontrado.")
            return

        # Cargar y calcular gastos
        expenses = project.get('expenses', [])
        if not isinstance(expenses, list):
            expenses = []

        total_expenses = sum(expense.get('amount', 0) for expense in expenses if isinstance(expense, dict))
        budget = project.get('budget', 0)
        balance = budget - total_expenses

        # Directorio de informes
        os.makedirs("informes", exist_ok=True)
        filename = f"Informe_Proyecto_{project_id}.pdf"
        pdf_path = os.path.join("informes", filename)

        # Crear el PDF
        c = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter
        c.setFont("Helvetica", 12)

        # Agregar título y datos principales
        c.drawString(100, height - 50, f"Informe del Proyecto ID: {project_id}")
        c.drawString(100, height - 80, f"Nombre: {project['name']}")
        c.drawString(100, height - 110, f"Descripción: {project['description']}")
        c.drawString(100, height - 140, f"Presupuesto Total: ${budget:.2f}")
        c.drawString(100, height - 170, f"Gastos Totales: ${total_expenses:.2f}")
        c.drawString(100, height - 200, f"Balance: ${balance:.2f}")

        # Listar miembros
        c.drawString(100, height - 230, "Miembros del equipo:")
        y_position = height - 260
        for member in project['members']:
            c.drawString(120, y_position, f"- {member}")
            y_position -= 20

        # Listar tareas asignadas con mejoras
        c.drawString(100, y_position - 20, "Tareas Asignadas:")
        y_position -= 50
        for task_data in project['tasks']:
            task = task_data['task']
            team = task_data['team']
            improvement = task_data.get('improvement', "Ninguna mejora recomendada")
            c.drawString(120, y_position, f"- {task} (Equipo: {team}) - Mejora: {improvement}")
            y_position -= 30
            if y_position < 50:  # Evita que el texto se salga de la página
                c.showPage()
                y_position = height - 50

        # Listar gastos detallados
        c.drawString(100, y_position - 20, "Gastos Detallados:")
        y_position -= 50
        for expense in expenses:
            concept = expense.get('concept', 'Desconocido')
            amount = expense.get('amount', 0)
            c.drawString(120, y_position, f"- {concept}: ${amount:.2f}")
            y_position -= 20
            if y_position < 50:  # Controlar el desbordamiento de texto
                c.showPage()
                y_position = height - 50

        # Guardar el archivo PDF
        c.save()
        messagebox.showinfo("Informe Generado", f"El informe se ha guardado en {pdf_path}")

    def logout(self):
        self.user_manager.logout()
        self.create_login_register()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
