from xml.dom import minidom
import xml.etree.ElementTree as et





doc = minidom.parse('data.xml')

print(doc.nodeName)
print(doc.firstChild.tagName)



my_tree = et.parse('data.xml')
my_root = my_tree.getroot()
print("L'élément racine : ", my_root.tag)





# la balise du premier enfant de l'élément racine
print("Le premier enfant de la racine : ", my_root[0][1].tag)

# afficher toutes les balises
print("\nLes balise sont : ")
for a in my_root[0]:
    print(a.tag, a.text)
    for b in a :
        print(b.tag, b.text)
    





print ("-----------------------------------------------------------------------------")

print("Le premier élément enfant :", my_root[0].tag)

# Les attributs du premier élément enfant
print("\nTous les attributs du premier élément enfant: ")
for a in my_root[0]:
    print(a.attrib)


print("\nLes textes du premier sub-élément : ")
for a in my_root[0]:
    print(a.text)

print("\nLes textes du second sub-élément : ")
for a in my_root[0]:
    print(a.tag,a.attrib,a.text)

