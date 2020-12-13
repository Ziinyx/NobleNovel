from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate
import requests
from bs4 import BeautifulSoup

#html novel

URL = 'any.html'#Copy paste any url to scrape hehe
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

#To find id in html
result = soup.find(id = 'chr-content')

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']
story = []

story.append(Paragraph(soup.strong.text, styleH))

for i in soup.find_all('p'):
    #print(i.get_text())
    story.append(Paragraph(i.get_text(), styleN))
    story.append(Paragraph(" ",styleN))
 
#Name of pdf
doc = SimpleDocTemplate("HoB.pdf")
doc.build(story)  
