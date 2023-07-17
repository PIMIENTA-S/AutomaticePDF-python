from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('PDF/imagenes/UnalLogo.jpg', x=10, y=10, w=53.6, h=22.8)
        # Se define tipo de letra
        self.set_font('Arial', 'B', 11)
        # Titulo
        self.cell(w=65, h=24, border=0, align='L', fill=0)
        self.multi_cell(w=0, h=6, txt='Universidad Nacional de Colombia - sede Medellín\nFacultad de Minas\nDepartamento de Ciencias de la Computación\nNombre de la clase', border=0, align='L',fill=0)
        # Separacion del texto con el encabezado
        self.ln(5)

    def footer(self):
        # Posicion de abajo hacia arriba, numbre negative
        self.set_y(-20)
        # Tipo de letra
        self.set_font('Arial', '', 8)
        # Page number
        self.cell(w=0, h=10, txt='      {nb}' + " "*140 +'Universidad Nacional de Colombia - Sede Medellín', border=1, align='L', fill=0)


pdf = PDF()
# Es necesario para que funcione /{nb}, total de paginas
pdf.alias_nb_pages()
pdf.add_page()
# Cuerpo del archivo

pdf.set_font('Times', '', 12)

for i in range(1,81):
    pdf.cell(w=0, h=10, txt='Tabla numero: '+ str(i), border=1,ln=1, align='C', fill=0)

pdf.output('Output.pdf/Header.pdf', 'F')