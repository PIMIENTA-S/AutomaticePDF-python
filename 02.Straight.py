from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.set_font('Arial', 'I', 17)

# Crear Rectas

pdf.rect(x=60, y=70, w=60, h=65)
# Las variables x & y simbolizan el punto donde empezara el trazo
# x : Horizontal
# Y : Vertical
# W : Ancho
# H : Alto


# Crear Elipse

pdf.ellipse(x=25, y=30, w=40, h=40)
# Herencia de la clase Rectas


# Crear Lineas

pdf.line(50, 140, 160, 140)
#__________x1___y1___x2___y2
# Tener en cuenta la imagen "lines"


# Crear Lineas Entrecortadas

pdf.dashed_line(20, 40, 20, 80, dash_length=15, space_length=5)
# Herencia de Lineas
# dash : hace referencia a longitud de la linea
# space : espacio entre lineas