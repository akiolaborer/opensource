import elementpath
import xml.etree.ElementTree as et

tree = et.parse("*.xml")
root = tree.getroot()

list = root.findall('tag')
root.findall("path")

rank = list.find('contents').text
#contents
list.get('name')
list.attrib['name']
#child
elem = et.SubElement(root, 'contents')
elem = et.SubElement(root, 'contents', attrib={'name':'Liechtenstein'})

#edit
for content in root.find('contents'):
    rank = int(content.find('rank'))
    if rank > 50:
        root.remove(content)

#output
tree = et.ElementTree(root)
tree.write('filename', encoding="utf-8", xml_declaration=True)

