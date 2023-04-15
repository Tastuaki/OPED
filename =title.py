import subprocess

tdata = []
con = ""
# git ls-tree -r --name-only HEAD > +title.txt
out = subprocess.run(["git","ls-tree","-r","--name-only","HEAD",">","+title.txt"])
with open("+title.txt","r+") as f:
    tdata=f.readlines()
    f.truncate(0)
    f.seek(0)
    for con in tdata:
        if "mp3" in con:
            f.write(con)