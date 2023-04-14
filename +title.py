import subprocess

tdata = []
data = []
out = subprocess.run(["git","ls-tree","-r","--name-only","HEAD",">","+title.txt"])
with open("title/title.txt","r+") as f:
    tdata=f.readlines()
    for i in range(len(tdata)):
        if tdata[i] in "mp3":
            data.append(tdata[i])
    f.writelines(data)