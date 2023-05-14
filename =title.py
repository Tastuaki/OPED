import subprocess
import os
import codecs

tdata = []
con = ""
# git ls-tree -r --name-only HEAD > +title.txt
path = os.getcwd()
print(path)
out = subprocess.run(["dir","*.mp3","/b",">","++title.txt"],shell=True)
# out = subprocess.run(["git","ls-tree","-r","--name-only","HEAD",">","+title.txt"],shell=True)
with codecs.open("++title.txt", "r", "shift_jis") as s:
    data = s.readlines()
    with codecs.open("+title.txt", "w", "utf-8") as u:
        for row in data:
            u.write(row)
# with open("+title.txt","r+",encoding="utf-8") as f:
#     tdata=f.readlines()
#     f.truncate(0)
#     f.seek(0)
#     for con in tdata:
#         if "mp3" in con:
#             f.write(con.replace("\'",""))