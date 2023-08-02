from lxml import etree
#cria um elemento XML <bookstore>
raiz = etree.Element("bookstore")

#cria elemento <book>
book = etree.Element("book")
#posicionado como filho do raiz
raiz.append(book)

title = etree.SubElement(book, "title")
title.text = "Aprendendo XML com Python"

print(etree.tostring(raiz))

with open('livros.xml', 'wb') as file:
    file.write(etree.tostring(raiz, pretty_print=True))