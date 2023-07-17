from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.set_font('Arial', '', 18)

'''
Individual 

pdf.set_top_margin(50)
pdf.set_left_margin(50)
pdf.set_right_margin(50)

Grupo

pdf.set_margins(left=50, top=50, right=50)
'''
pdf.text(x=30, y=20,txt='Hola soy un parrafo')

pdf.add_page()

# Salto de linea
# Todo que se ponga aqui estara en otra hoja del archivo

pdf.text(x=20, y=50, txt='Otra hoja')