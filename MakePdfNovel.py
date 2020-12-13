from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate
import requests
from bs4 import BeautifulSoup

#html novel

URL = 'https://readnovelfull.com/heaven-officials-blessing/chapter-1.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

result = soup.find(id = 'chr-content')

#print(Ntitle)

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']
story = []

story.append(Paragraph(soup.strong.text, styleH))

print("story created")

for i in soup.find_all('p'):
    #print(i.get_text())
    story.append(Paragraph(i.get_text(), styleN))
    story.append(Paragraph(" ",styleN))
 
doc = SimpleDocTemplate("HoB.pdf")
doc.build(story)  




##canvas = Canvas("Infi.pdf")    alt for creating pdf but only one page is created and extra txt is discarded
##f = Frame(inch, inch, 6*inch, 9*inch,showBoundary=0)
##f.addFromList(story,canvas)
##canvas.save()