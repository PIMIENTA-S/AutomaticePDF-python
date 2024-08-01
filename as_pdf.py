import aspose.words as aw
from fpdf import FPDF # type: ignore

doc = aw.Document()
builder = aw.DocumentBuilder(doc)

builder.insert_image("verde.jpg")

doc.save("put.pdf")