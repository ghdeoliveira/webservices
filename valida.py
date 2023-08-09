from lxml import etree

# indicar um documento XML
arquivo = "atividade.xml"

# difinir um PARSER XML 
parser = etree.XMLParser(dtd_validation=True)

# executar a validação
try:
    etree.parse(arquivo, parser)
    print("Documento XML é válido!")
except Exception as error:
    print("Documento XML não é válido!")
    print(error)