import PyPDF2 as pdf

# Se crea un objeto para leer el pdf
# Toma dos parametros, la ruta y el modo de lectura, en este caso lectura binaria(rb)

#pdf_file_obj = open('Horario_del_Alumno.pdf', 'rb')

# ----------------Leer el pdf------------------

path = 'Horario_del_Alumno.pdf'

pdf_reader = pdf.PdfReader(path)
page = pdf_reader.pages[0]

# text = page.extract_text().replace('\n', ' ').split(' ')
text = page.extract_text().split('\n')



def horarioSort(text):
    codi = []
    for lines in text:
        if '[' in lines:
            if lines not in codi and lines.count('(')== 0:
                codi.append(lines)
    
    one = codi[0]
    index = one.find('[')
    if index != -1:
        codi[0] = one[index:]
        
        # for a in lines:
        #     if a == '[':
        #         boole = True
        #     if boole == True:
        #         codi.append(a)
        #     if a == ']':
        #         boole = False
    
    
    return codi

    



# print(text)
print(horarioSort(text))
# print(pdf_reader.getNumPages())

