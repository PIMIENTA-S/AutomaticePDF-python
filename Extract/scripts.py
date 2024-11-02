import PyPDF2 as pdf

# Se crea un objeto para leer el pdf
# Toma dos parametros, la ruta y el modo de lectura, en este caso lectura binaria(rb)
pdf_file_obj = open('Horario_del_Alumno.pdf', 'rb')

# Leer el pdf

pdf_reader = pdf.PdfReader(pdf_file_obj)
print(pdf_reader.metadata)
# print(pdf_reader.getNumPages())

