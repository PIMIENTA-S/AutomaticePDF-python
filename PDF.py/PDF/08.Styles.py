from fpdf import FPDF
from Reference import *

pdf = FPDF(orientation='p', unit='mm', format='A4')



pdf.add_page()

'''
Estilos de letras

U : Subrayado
B : Negrita
I : Italica
Se pueden combinar
'''
pdf.set_font('Arial', '', 18)

'''
Cambiar el color del texto o relleno

Texto 
pdf.set_text_color(r=160, g= 220, b=225)


Relleno
pdf.set_fill_color(r=160, g= 220, b=225)


Trazos y bordes
pdf.set_draw_color(r=160, g= 220, b=225)
Aplica para cualquier tipo de trazo

Estilos de los Circulos y cuadrados

F : Fill  // con esto el color que le dé al relleno se aplicara al circulo
D : Draw  // este es el estilo predefinido

Lineas

Las lineas se les puede cambiar estilo solo al trazo, debido a que no cuetan con relleno

'''
TrazosColor(pdf, 'black')
RellenoColor(pdf, 'gray')
pdf.ellipse(x=40, y=50, w=40, h=40, style='DF')

pdf.dashed_line(40, 50, 100, 110, space_length=5, dash_length=7)

TextoFuente(pdf, 'Times')
TrazosColor(pdf, 'green')

pdf.cell(w=0, h=15, txt= 'Example', border=1, align='C', fill=0)

pdf.output('Output.pdf/Styles.pdf')