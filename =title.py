import subprocess
import os
import codecs
import io
import glob
from itertools import count

tdata = []
# con = ""

base = os.getcwd()
files_path = glob.glob(os.path.join(base,"*.mp3"))
files = [os.path.basename(i) for i in files_path]

with open("+title.txt",'w+', encoding='utf-8') as f:
    for i in len(files):
        tdata = []
        for j in count(i):
            if("〜" in files[j]):
                orow = files[j]
                files[j] = files[j].replace("〜","～")
                os.rename(base+"\\"+orow,base+"\\"+files[i])
            files[j] += "\n"
            tdata.append(files[j])
            b = files[j][:files[j].find("(")]
            b = b[:b.rfind(" ")]
            a = files[j+1][:files[j+1].find("(")]
            a = a[:a.rfind(" ")]
            print("a: "+ a,end="|")
            print("b: "+ b,end="|\n")
            if(a != b):
                i = j
                break
        tdata.reverse()
        f.writelines(tdata)