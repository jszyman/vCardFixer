#https://github.com/eventable/vobject
import vobject

def open_file(self, file_name, path = './', mode = 'r'):
    try:
        opened_file = open(path + '\\' + file_name, mode)
        return opened_file
    except IOError:
        return None

vcard_file = open("Name Lastname.vcf")
vcard_text = vcard_file.read(-1)
vcard_file.close()

j = vobject.readOne(vcard_text)
j.add('fn')
j.prettyPrint()
print
print j.n.value.family
print j.n.value.given

#exchange given and family names for fixing sake
j.n.value.family, j.n.value.given = j.n.value.given, j.n.value.family

j.prettyPrint()

print j.serialize()

if __name__ == '__main__':
    pass