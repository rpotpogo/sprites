import json
import os
from shutil import copyfile

mydir = "D:\pogo\sprites\icons_large"
#mydir = "D:\pogo\sprites\\no_border"
with open("D:\pogo\sprites\code\pokemon.json", "r") as read_file:
    data = json.load(read_file)
    #print (data)
    for pokedex in range(1,1000):
        try:
            forms =  data[str(pokedex)]['forms']
            #print (forms)
            for i in range(len(forms)):
                if forms[i]['nameform'] == 'Normal':
                    protoform = forms[i]['protoform']
                    print (pokedex, protoform)
                    filenameoriginal = "{}.png".format(pokedex)
                    filename = "{}-{}.png".format(pokedex,protoform)
                    if os.path.exists(os.path.join(mydir, filename)):
                        print ("file {} already exists".format(filename))
                    else:
                        print ("file {} missing.".format(filename))
                        copyfile(os.path.join(mydir, filenameoriginal), os.path.join(mydir, filename))
                    break;
        except KeyError:
            continue

#for file in os.listdir(mydir):
#    if file.endswith(".png"):
#        print(os.path.join(mydir, file))