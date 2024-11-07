import os
from fpdf import FPDF

class ReportManager:
    def __init__(self):
        self.report_folder = "informes"  # Definir la carpeta de informes
        if not os.path.exists(self.report_folder):
            os.makedirs(self.report_folder)  # Crear la carpeta si no existe

    def generate_pdf_report(self, project):
        """
        Genera un informe PDF de un proyecto específico.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        pdf.set_font("Arial", size=14)
        pdf.cell(200, 10, txt="Informe del Proyecto", ln=True, align='C')

        pdf.ln(10)

        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Nombre: {project['name']}", ln=True)
        pdf.cell(200, 10, txt=f"Descripción: {project['description']}", ln=True)
        pdf.cell(200, 10, txt=f"Presupuesto: {project['budget']}", ln=True)
        pdf.cell(200, 10, txt=f"Gastos: {project['expenses']}", ln=True)
        pdf.cell(200, 10, txt=f"Miembros: {', '.join(project['members'])}", ln=True)

        pdf.ln(10)
        pdf.cell(200, 10, txt="Tareas:", ln=True)
        for task in project["tasks"]:
            pdf.cell(200, 10, txt=f" - {task}", ln=True)

        pdf.ln(10)
        pdf.cell(200, 10, txt="Sugerencias basadas en tendencias de mercado:", ln=True)
        pdf.cell(200, 10, txt=f"- {project.get('suggestion', 'No hay sugerencias disponibles.')}", ln=True)

        # Guardar el archivo en la carpeta "informes"
        filepath = os.path.join(self.report_folder, f"{project['name']}_informe.pdf")
        pdf.output(filepath)

        return filepath

    def create_specific_report(self, project_name, project_manager):
        """
        Crea un informe solo para el proyecto especificado.
        """
        # Buscar el proyecto por nombre
        project = project_manager.get_project(project_name)
        
        if project:
            # Si el proyecto existe, generar el informe
            report_file = self.generate_pdf_report(project)
            return report_file
        else:
            return None


