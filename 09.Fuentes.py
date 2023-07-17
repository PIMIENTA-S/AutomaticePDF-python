from fpdf import FPDF


pdf = FPDF(orientation='p', unit='mm', format='A4')

pdf.add_page()

'''
Fuentes de FPDF

Courier
Helvetica
Arial
Times
Symbol
ZapfDingbats
'''

# Para agregar una fuente externa se recurre a los siguientes parametros
'''
pdf.add_font(family='T', style='', fname='PDF/fuentes/Transformers Movie.ttf', uni=True)

pdf.set_font('T', '', 30)

pdf.cell(w=0, h=15, txt='Transformers', border=1, align='C', fill=0)
'''

pdf.add_font(family='Dreams', style='', fname='PDF/familyFuente/CaviarDreams.ttf', uni=True)

pdf.add_font(family='Dreams', style='B', fname='PDF/familyFuente/CaviarDreams_Bold.ttf', uni=True)

pdf.add_font(family='Dreams', style='I', fname='PDF/familyFuente/CaviarDreams_Italic.ttf', uni=True)

pdf.add_font(family='Dreams', style='BI', fname='PDF/familyFuente/CaviarDreams_BoldItalic.ttf', uni=True)


pdf.set_font('Dreams', 'BI', 17)

pdf.cell(w=0, h=15, txt='Prueba de caviar', border=1, align='C', fill=0)

pdf.output('Output.pdf/Fuente.pdf')
