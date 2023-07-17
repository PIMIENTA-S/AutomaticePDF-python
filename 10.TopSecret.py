from fpdf import FPDF

from Reference import *

class PDF(FPDF):
    def header(self):

        self.image('PDF/imagenes/redconfidencial.jpg', x=10, y=10, w=30, h=30)

        self.set_font('Arial','', 15)

        TextoFontSize(self, 45)

        self.cell(w=0, h=20, txt='Reporte', border=0, ln=1, align='C',fill=0)

        TextoFontSize(self, 10)

        self.cell(w=0, h=10, txt='ID : 344679154 - 2020/04/25', border=0, ln=1, align='C', fill=0)

        self.ln(5)

    def footer(self):
        self.set_y(-20)

        self.set_font('Arial', 'I', 12)

        self.cell(w=0, h=10, txt='Pagina ' + str(self.page_no()) + '/{nb}', border=0, ln=1, align='R', fill=0)


pdf = PDF(orientation='P', unit='mm', format='A4')

pdf.alias_nb_pages()

pdf.add_page()

# Se declara el estilo y tamaño del texto

pdf.set_font('Arial', '', 15)

# Primer encabezado

pdf.set_font('Arial', 'B', 17)

RellenoColor(pdf, 'red')
pdf.multi_cell(w=0, h=15, txt='Gerente', border=0, align='C', fill=1)

pdf.set_font('Arial', '', 13)


# Espacio
pdf.ln(3)

# Fila 1
TextoFontSize(pdf, 13)
Textocolor(pdf, 'gray')
pdf.cell(w=47.5, h=13, txt='Caso(s):', border=0, align='R', fill=0)
Textocolor(pdf, 'black')
pdf.cell(w=47.5, h=13, txt='007-1H', border=0, align='L', fill=0)
Textocolor(pdf, 'gray')
pdf.cell(w=47.5, h=13, txt='Estado:', border=0, align='R', fill=0)
Textocolor(pdf, 'black')
pdf.multi_cell(w=47.5, h=13, txt='Cerrado', border=0, align='L', fill=0)

# Fila 2
Textocolor(pdf, 'gray')
pdf.cell(w=47.5, h=13, txt='Implicado(s):', border=0, align='R', fill=0)
Textocolor(pdf, 'black')
pdf.cell(w=47.5, h=13, txt='Nombre persona(s)', border=0, align='L', fill=0)
Textocolor(pdf, 'gray')
pdf.cell(w=47.5, h=13, txt='Codigo penal:', border=0, align='R', fill=0)
Textocolor(pdf, 'black')
pdf.multi_cell(w=47.5, h=13, txt='111-76', border=0, align='L', fill=0)

# Fila 3

Textocolor(pdf, 'gray')
pdf.cell(w=47.5, h=13, txt='Fecha Ocurrencia:', border=0, align='R', fill=0)
Textocolor(pdf, 'black')
pdf.cell(w=47.5, h=13, txt='MM/DD/AA', border=0, align='L', fill=0)
Textocolor(pdf, 'gray')
pdf.cell(w=47.5, h=13, txt='Prioridad:', border=0, align='R', fill=0)
Textocolor(pdf, 'black')
pdf.multi_cell(w=47.5, h=13, txt='Media', border=0, align='L', fill=0)

TrazosColor(pdf, 'red')
pdf.rect(x=10, y=60, w=190, h=45.5)

# Separador
pdf.ln(10)

# Tablas
pdf.set_font('Arial', 'B', 17)
RellenoColor(pdf, 'red')
pdf.multi_cell(w=0, h=15, txt='Implicados', border=0, align='C', fill=1)


pdf.set_font('Arial', '', 13)
TrazosColor(pdf, 'black')
pdf.cell(w=10, h=13, txt='G', border='TBL', align='C', fill=0)
pdf.cell(w=60, h=13, txt='Nombre', border='TB', align='C', fill=0)
pdf.cell(w=70, h=13, txt='Correo', border='TB', align='C', fill=0)
pdf.multi_cell(w=0, h=13, txt='Numero de concrato', border='TBR', align='C', fill=0)



# Datos

with open("Clientes.txt", "r") as listaDatos:
    lineas = listaDatos.readlines()
    for datos in lineas:
        datos = datos.replace("\n", "").split(", ")
        if datos[3] == "4442061" or datos[3] == "4442955" or datos[3] == "4447892":
            pdf.cell(w=10, h=10, txt=datos[1], border='RLB', align='C', fill=0)
            pdf.cell(w=60, h=10, txt=datos[0], border='RB', align='C', fill=0)
            pdf.cell(w=70, h=10, txt=datos[2], border='RB', align='C', fill=0)
            pdf.multi_cell(w=0, h=10, txt= datos[3], border='RLB', align='C', fill=0)
        elif datos[3]=="4443190" or datos[3]=="4446469":
            pdf.cell(w=10, h=10, txt=datos[1], border='RLT', align='C', fill=0)
            pdf.cell(w=60, h=10, txt=datos[0], border='RT', align='C', fill=0)
            pdf.cell(w=70, h=10, txt=datos[2], border='RT', align='C', fill=0)
            pdf.multi_cell(w=0, h=10, txt= datos[3], border='RLT', align='C', fill=0)
        else:
            pdf.cell(w=10, h=10, txt=datos[1], border='RL', align='C', fill=0)
            pdf.cell(w=60, h=10, txt=datos[0], border='R', align='C', fill=0)
            pdf.cell(w=70, h=10, txt=datos[2], border='R', align='C', fill=0)
            pdf.multi_cell(w=0, h=10, txt= datos[3], border='RL', align='C', fill=0)


pdf.output('Output.pdf/TopSecret.pdf', 'F')