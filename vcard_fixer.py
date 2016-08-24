#https://github.com/eventable/vobject
import vobject

def open_file(self, file_name, path = './', mode = 'r'):
    try:
        opened_file = open(path + '\\' + file_name, mode)
        return opened_file
    except IOError:
        return None

vcard_file = open(".\in\Jon Doe.vcf")
vcard_text = vcard_file.read(-1)
vcard_file.close()

j = vobject.readOne(vcard_text)
j.prettyPrint()

print
print "Family name: " + j.n.value.family
print "Given name: " + j.n.value.given

#exchange given and family names for fixing sake
j.n.value.family, j.n.value.given = j.n.value.given, j.n.value.family

j.prettyPrint()

#serialize() requires at least 1 FN field 
j.add('fn')
#print j.serialize()

#store reworked file
file_out =  open(".\out\Jon Doe.vcf", "w")
file_out.write(j.serialize())
file_out.close()

if __name__ == '__main__':
    pass

#TODO: remove empty lines from out-files