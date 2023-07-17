from fpdf import FPDF

'''
P : Portrait (vertical)
L : Landscape (horizontal)

A4 : 210x297mm
'''

pdf = FPDF(orientation='p', unit='mm', format='A4')

pdf.add_page()

pdf.set_font('Arial', '', 18)

# Texto

pdf.text(x=60, y=40, txt='Angell Pimienta')


# Imagenes (jpg.png)

# url = 'https://github.com/PIMIENTA-S'
# pdf.image('PDF/llegna.png', x=10, y=10, w=40, h=40, link=url)

pdf.output("Output.pdf/Primer.pdf")