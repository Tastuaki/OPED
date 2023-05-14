import subprocess
import os

tdata = []
con = ""
# git ls-tree -r --name-only HEAD > +title.txt
path = os.getcwd()
print(path)
out = subprocess.run(["dir","/b",">","+title.txt"],shell=True)
# out = subprocess.run(["git","ls-tree","-r","--name-only","HEAD",">","+title.txt"],shell=True)
with open("+title.txt","r+") as f:
    tdata=f.readlines()
    f.truncate(0)
    f.seek(0)
    for con in tdata:
        if "mp3" in con:
            f.write(con.replace("\'",""))