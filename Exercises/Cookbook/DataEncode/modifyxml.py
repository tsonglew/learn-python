# -*- coding: utf-8 -*-

from xml.etree.ElementTree import parse, Element
doc = parse('pred.xml')
root = doc.getroot()
print(root)

# Remove some elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# Insert a new element
index = root.getchildren().index(root.find('nm'))

e = Element('spam')
e.text = 'This is a test'
root.insert(index+1, e)

# Write to file
doc.write('newpred.xml', xml_declaration=True)
