#importação da biblioteca
from lxml import etree

filename = "books.xml"
parser = etree.XMLParser()
tree = etree.parse(filename, parser)

titulos = tree.xpath(".//book[price>30.00]/title/text()")
#titulos = tree.xpath(".//book/title/text()")

for titulo in titulos:
    print(titulo)