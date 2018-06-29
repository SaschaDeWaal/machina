import os
import re
from PIL import Image
path = os.getcwd()
g= open("train.txt","w")
for file in os.listdir("obj"):
        filename = file[:-4]+".jpg"
        filepath = path + "/obj/"+filename
        g.write(filepath+"\n")
g.close()
