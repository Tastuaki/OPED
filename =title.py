import subprocess

tdata = []
data = []
# git ls-tree -r --name-only HEAD > -title.txt
out = subprocess.run(["git","ls-tree","-r","--name-only","HEAD",">","+title.txt"])
with open("+title.txt","r+") as f:
    tdata=f.readlines()
    print(tdata)
    for i in range(len(tdata)):
        if "mp3" in tdata[i]:
            data.append(tdata[i])
    print(data)
    f.writelines(data)