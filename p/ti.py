import os
import glob
from itertools import count

tdata = []
sdata = [[],[],[],[],[],[]]
sym = ["前奏曲"," OP"," ED","劇中曲","挿入歌","主題歌"]
i = 0
j = 0
k = 0
lb = 0

def ex(s,data,p):
    l = 0
    od = []
    l = len(data)
    for i in range(p,l):
        if s in data[i][:data[i].find("(")]:
            od.append(data[i])
    return od

os.chdir('../')
base = os.getcwd()
files_path = glob.glob(os.path.join(base,"*.mp3"))
files = [os.path.basename(i) for i in files_path]
max = len(files)
# print(max)

with open("p/all",'w+', encoding='utf-8') as f:
    for i in range(max):
        if i == j:
            # print(str(i)+":"+str(j))
            bdata = []
            for j in count(i):
                if j < max - 1:
                    if "〜" in files[j]:
                        orow = files[j]
                        files[j] = files[j].replace("〜","～")
                        os.rename(base+"\\"+orow,base+"\\"+files[i])
                    files[j] += "\n"
                    bdata.append(files[j])
                    b = files[j][:files[j].find("(")]
                    a = files[j+1][:files[j+1].find("(")]
                    b = b[:b.rfind(" ")]
                    a = a[:a.rfind(" ")]
                    if a != b:
                        print("a:"+a+"|b:"+b)
                        j += 1
                        break
                    # elif j+1 == max-1:
                    #     bdata.append(files[max-1] + "\n")
                elif j == max-1:
                    bdata.append(files[max-1] + "\n")
                else:
                    break
            print(bdata)
            lb = len(bdata)
            if lb != 1:
                k = 0
                while(k < lb):
                    # print(str(k)+":"+bdata[k])
                    for s in sym:
                        if s in bdata[k]:
                            if k+1 < lb:
                                if s in bdata[k+1]:
                                    sdata[sym.index(s)] = ex(s,bdata,k)
                                    k += len(sdata[sym.index(s)]) - 1
                                else:
                                    sdata[sym.index(s)] = [bdata[k]]
                            else:
                                sdata[sym.index(s)] = [bdata[k]]
                                break
                    k += 1
            else:
                for s in sym:
                    if s in bdata[0]:
                        sdata[sym.index(s)] = [bdata[0]]
                        break
            # print(sdata)
            # for s in sym:
            #     for l in range(len(sdata)):
            #         if sdata[l]:
            #             if s in sdata[l][0]:
            #                 tdata.extend(sdata[l])
            for l in range(len(sdata)):
                if sdata[l]:
                    print(sdata[l])
                    if len(sdata[l]) > 2:
                        ls = len(sdata[l])
                        mn = []
                        im = []
                        for s in sdata[l]:
                            at,n=s.split(sym[l])
                            at += sym[l]
                            mn.append(n)
                            im.append(int(n[:n.find("(")]))
                        im.sort()
                        sdata[l] = []
                        for i in im:
                            for na in mn:
                                if na[:na.find("(")] == str(i):
                                    sdata[l].append(at+na)
                        print(sdata[l])
                    tdata.extend(sdata[l])
            sdata = [[],[],[],[],[],[]]
            # print(tdata)
            f.writelines(tdata)
            tdata = []