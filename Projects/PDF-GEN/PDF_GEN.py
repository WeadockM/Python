# importing modules
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from DOCX_READ import text1, text2
from reportlab.lib.units import inch, mm, cm, pica

# initializing variables with values
fileName = 'PurchaseOrder.pdf'
documentTitle = 'sample'
# title = 'Purchase Order'
subTitle = 'The largest thing now!!'
textLines1 = [
	text1,
	text2,
]
textLines2 = [
	'Status:',
	'Date:',
	'4D Systems LLC',
	'QUOTE#',
	'Renewal Date:',
	'P.O. Date:',
	'',
	'Company Name:',
	'Company Address Line 1',
	'Company Address Line 2',
]
image = 'logo.jpg'

# creating a pdf object
pdf = canvas.Canvas(fileName)

# setting the title of the document
pdf.setTitle(documentTitle)

# registering a external font in python
pdfmetrics.registerFont(
	TTFont('abc', 'SakBunderan.ttf')
)

# creating the title by setting it's font
# and putting it on the canvas
# pdf.setFont('abc', 36)
# pdf.drawCentredString(450, 770, title)

# creating the subtitle by setting it's font,
# colour and putting it on the canvas
# pdf.setFillColorRGB(0, 0, 255)
# pdf.setFont("Courier-Bold", 24)
# pdf.drawCentredString(290, 720, subTitle)

# drawing a line
def box():
	pdf.setFillColorRGB(0,.1,.3)
	pdf.rect(100, 580, 400, 20, fill=1)
box()
pdf.line(100, 600, 500, 600)
pdf.line(100, 580, 500, 580)
pdf.line(100, 560, 500, 560)
pdf.line(500, 560, 500, 600)
pdf.line(100, 560, 100, 600)
pdf.line(233, 560, 233, 600)
pdf.line(367, 560, 367, 600)

# creating a multiline text using
# textline and for loop
#text = pdf.beginText(40, 680)
#text.setFont("Courier", 12)
#text.setFillColor(colors.black)
#for line in textLines1:
	#text.textLine(line)
#pdf.drawText(text)

text = pdf.beginText(400, 750)
text.setFont("Courier", 8)
text.setFillColor(colors.black)
ys = [600,590,580,570,560,550]
width = pdf._pagesize[0]
padding = 20 * mm
for line in textLines2:
	text.textLine(line)
pdf.drawText(text)

text = pdf.beginText(238, 592)
text.setFont("Courier-Bold", 9)
text.setFillColor(colors.white)
text.textLine('Delivery Date')
pdf.drawText(text)

text = pdf.beginText(372, 592)
text.textLine('Payment Terms')
pdf.drawText(text)

text = pdf.beginText(268, 568)
text.setFont("Courier", 12)
text.setFillColor(colors.black)
text.textLine('Delivery Date')
pdf.drawText(text)

text = pdf.beginText(400, 568)
text.textLine('Payment Terms')
pdf.drawText(text)

# pdf.drawString(width - padding, 500, 'Testing:')

# drawing a image at the
# specified (x.y) position
pdf.drawInlineImage(image, 80, 770)

# saving the pdf
pdf.save()
