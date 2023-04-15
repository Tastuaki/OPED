import subprocess

tdata = []
data = []
# git ls-tree -r --name-only HEAD > -title.txt
out = subprocess.run(["git","ls-tree","-r","--name-only","HEAD",">","+title.txt"])
# with open("+title.txt","r+") as f:
#     tdata=f.readlines()
#     for i in range(len(tdata)):
#         if "mp3" in tdata[i]:
#             data.append(tdata[i])
#     f.truncate(0)
#     print(data)
#     f.writelines(data)