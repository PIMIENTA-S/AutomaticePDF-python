from fpdf import FPDF

# Metadatos

pdf = FPDF(orientation='p', unit='mm', format='A4')

# Titulo
pdf.set_title(title='Titulo de la presentacion')

# Autor
pdf.set_author(author='AngellPimienta')

# Creador
pdf.set_creator('Aplicacion')

# Palabras clave
pdf.set_keywords(keywords='Hoja, prueba, metadatos')

# Asunto
pdf.set_subject(subject='Que son los metadatos')
