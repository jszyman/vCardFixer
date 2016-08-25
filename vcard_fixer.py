#https://github.com/eventable/vobject
import vobject
import os
import errno

input_dir = "./in"
output_dir = "./out"

#list all files in IN directory
onlyfiles = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

if not os.path.exists(output_dir):
    try:
        print
        print "Creating output directory..."
        os.makedirs(output_dir)
        print "...out"
    except OSError as exc: # Guard against race condition
        print "Output directory exists already!"
        if exc.errno != errno.EEXIST:
            raise

print 
print "Processing name exchange..."

for fi in onlyfiles: 
    print "..." + str(fi)
    vcard_f = open(input_dir + "/" + fi)
    vcard_t = vcard_f.read(-1)
    vcard_f.close()
    vcard_o = vobject.readOne(vcard_t)
    
    #exchange given and family names
    vcard_o.n.value.family, vcard_o.n.value.given = vcard_o.n.value.given, vcard_o.n.value.family
    #serialize() requires at least 1 FN field 
    vcard_o.add('fn')
    
    file_out =  open(output_dir + "/" + fi, "w")
    file_out.write(vcard_o.serialize())
    file_out.close()



if __name__ == '__main__':
    pass

#TODO: remove empty lines from out-files