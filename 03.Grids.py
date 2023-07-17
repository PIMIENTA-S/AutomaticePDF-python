from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.set_font('Arial', '', 18)


# Border 
'''
0 = no | 1 = si | T = top | B = abajo | L = left | R = rigth

Align

C = centro | L = left | R = rigth

Fill

Relleno | 0 = no | 1 = si

Lineas

ln = 1 Renglon 1
ln = 2 Renglon 2
Si no se especifica la ln todo quedara en la misma linea

Link

Los parametros .cell pueden aceptar links
'''
text = 'Why cant i catch that stupid red dot thinking longingly about tuna brineLounge in doorway. Attack the child. Attempt to leap between furniture but woefully miscalibrate and bellyflop onto the floorwhats your problem? i meant to do that now i shall wash myself intently demand to be let outside at once, and expect owner to wait for me as i think about it so sleep over your phone and make cute snoring noises sit by the fire. Use lap as chair nyaa nyaa leave hair on owners clothes. I hate cucumber pls dont throw it at me grass smells good or paw at beetle and eat it before it gets away yet whatever, but bite the neighbors bratty kid i like fish purr while eating.\nFind box a little too small and curl up with fur hanging out suddenly go on wild-eyed crazy rampage eat too much then proceed to regurgitate all over living room carpet while humans eat dinner for chill on the couch table. Dismember a mouse and then regurgitate parts of it on the family room floor whos the baby vommit food and eat it again for meow to be let in. Attack dog, run away and pretend to be victim. I cry and cry and cry unless you pet me, and then maybe i cry just for fun meow meow or annoy owner until he gives you food say meow repeatedly until belly rubs, feels good litter kitter kitty litty little kitten big roar roar feed me be a nyan cat, feel great about it, be annoying 24/7 poop rainbows in litter box all day ooh'

# Linea 1

pdf.cell(w=50, h=10, txt='Pimienta', border=1, align='C', fill=0)
pdf.cell(w=30, h=10, txt='Projec 1', border=1, align='C', fill=0)
pdf.cell(w=50, h=10, txt='lorem ipsum', border=1, align='C', fill=0)
pdf.multi_cell(w=0, h=10, txt='lorem', border=1, align='C', fill=0)

# Linea 2

pdf.cell(w=50, h=10, txt='Pimienta', border=1, align='C', fill=0)
pdf.cell(w=30, h=10, txt='Projec 1', border=1, align='C', fill=0)
pdf.cell(w=50, h=10, txt='lorem ipsum', border=1, align='C', fill=0)
pdf.multi_cell(w=0, h=10, txt='lorem', border=1, align='C', fill=0)

# Linea 3

pdf.cell(w=50, h=10, txt='Pimienta', border=1, align='C', fill=0)
pdf.cell(w=30, h=10, txt='Projec 1', border=1, align='C', fill=0)
pdf.cell(w=50, h=10, txt='lorem ipsum', border=1, align='C', fill=0)
pdf.multi_cell(w=0, h=10, txt='lorem', border=1, align='C', fill=0)

# Cuando los parametros w o h son 0 cubriran toda la linea especificada

pdf.multi_cell(w=0, h=10, txt=text, border=1, align='L', fill=0)
