import subprocess

tdata = []
data = []
# git ls-tree -r --name-only HEAD > -title.txt
out = subprocess.run(["git","ls-tree","-r","--name-only","HEAD",">","-title.txt"])
with open("-title.txt","r+") as f:
    tdata=f.readlines()
    for i in range(len(tdata)):
        if tdata[i] in "mp3":
            data.append(tdata[i])
    
    print(data)
    f.writelines(data)