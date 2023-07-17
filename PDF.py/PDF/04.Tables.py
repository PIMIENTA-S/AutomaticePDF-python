from fpdf import FPDF 

pdf = FPDF(orientation='p', unit='mm', format='A4')
pdf.add_page()
pdf.set_font('Arial', '', 15)

pdf.cell(w=0, h=12, txt='Reporte', border=1, ln=1, align='C', fill=0)

# Encabezado

pdf.cell(w=60, h=15, txt='Nombre', border=1, align='C', fill=0)
pdf.cell(w=10, h=15, txt='G', border=1, align='C', fill=0)
pdf.cell(w=70, h=15, txt='Correo', border=1, align='C', fill=0)
pdf.multi_cell(w=0, h=15, txt='Numero de concrato', border=1, align='C', fill=0)


# Datos

with open("Clientes.txt", "r") as listaDatos:
    lineas = listaDatos.readlines()
    for datos in lineas:
        datos = datos.replace("\n", "").split(", ")
        pdf.cell(w=60, h=10, txt=datos[0], border=1, align='C', fill=0)
        pdf.cell(w=10, h=10, txt=datos[1], border=1, align='C', fill=0)
        pdf.cell(w=70, h=10, txt=datos[2], border=1, align='C', fill=0)
        pdf.multi_cell(w=0, h=10, txt= datos[3], border=1, align='C', fill=0)
        


pdf.output("Output.pdf/Tabla 1.pdf")