from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import mm, inch
from reportlab.pdfgen import canvas

pagesize = (57 * mm, 150 * mm)  # 20 inch width and 10 inch height.
# doc = SimpleDocTemplate('Null.pdf', pagesize=pagesize)



# def drawMyRuler(Pdf):
#     pdf.drawString(100, 810, "")
#     pdf.drawString(200, 810, '')
#     pdf.drawString(300, 810, '')
#     pdf.drawString(400, 810, '')
#     pdf.drawString(500, 810, '')
#
#     pdf.drawString(10, 100, '')
#     pdf.drawString(10, 200, '')
#     pdf.drawString(10, 300, '')
#     pdf.drawString(10, 400, '')
#     pdf.drawString(10, 500, '')
#     pdf.drawString(10, 600, '')
#     pdf.drawString(10, 700, '')
#     pdf.drawString(10, 800, '')


# content
fileName = 'Null.pdf'
documentTitle = 'Null.pdf'

title = 'invoice'
subTitle = 'Inv#00304_2021_00001'
subTitle1 = 'PO#RAA_00043_2021_00010'
subTitle2 = 'Delivery Person: Umer Hafeez     Customer: Raahim Naeem'
subTitle3 = 'Delivery Datetime: 11-03-2021 12:01       Delivery Address: Civil Line, Sheikhupura'
# subTitle4 = 'Product                 Quantity                   UnitPrice                VAT                  Amount'
# subTitle5 = "Chilgozy                  50                              16.64                      5.82                " \
#             "   " \
#             " 22.46 "
# subTitle6 = "Coconut                   30                              63.25                     12.65               " \
#             "   75.9 "

# create document

pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)
pdf.setPageSize(pagesize)

# drawMyRuler(pdf)
# Title :: SET Font
# for font in pdf.getAvailableFonts():
#    print(font)
pdf.drawString(0, 0, title)

# Sub title
pdf.setFont("Helvetica-Bold", 7)
pdf.drawString(230, 750, subTitle)
pdf.drawString(210, 730, subTitle1)
pdf.drawString(180, 710, subTitle2)
pdf.drawString(140, 690, subTitle3)
# pdf.drawString(140, 670, subTitle4)
# pdf.drawString(140, 650, subTitle5)
# pdf.drawString(140, 640, subTitle6)


# Draw a line
pdf.line(130, 660, 420, 660)

flow_obj = []
data = [['Product', 'Quantity', 'UnitPrice', 'VAT', 'Amount']]


for i in range(2):
    data.append([0, 1, 2])

print(data)
t = Table(data, colWidths=[40 for i in range(1,6)], rowHeights=[40 for i in range(1,4)])
# tstyle = TableStyle([("BOX", (0, 0), (-1, -1), 1, colors.red),
#                      ("GRID", (0, 0), (-1, -1), 1, colors.blue),
#                      ("VALIGN", (0, 0), (-1, -1), "MIDDLE")])

# t.setStyle(tstyle)
flow_obj.append(t)
# pdf.build(flow_obj)
pdf.save()



