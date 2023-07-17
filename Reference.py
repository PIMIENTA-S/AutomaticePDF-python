def diccionary_colorful(color):
    coloful = {
        'black' : (0, 0, 0),
        'white' : (225, 225, 225),
        'green' : (96, 218, 117),
        'blue' : (96, 181, 218),
        'red' : (239, 71, 71),
        'gray' : (123, 125, 125),
        'lred' : (203, 67, 53)
    }
    return coloful[color]

def TrazosColor(pdf, color):
    r, g, b = diccionary_colorful(color)
    return pdf.set_draw_color(r, g, b)

def RellenoColor(pdf, color):
    r, g, b = diccionary_colorful(color)
    return pdf.set_fill_color(r, g, b)

def Textocolor(pdf, color):
    r, g, b = diccionary_colorful(color)
    return pdf.set_text_color(r, g, b)

def TextoFontSize(a, size):
    a.set_font_size(size)


def TextoFuente(pdf, fuente):
    pdf.set_font(fuente)