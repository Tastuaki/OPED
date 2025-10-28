import re
import urllib.request
from itertools import count

def indata(txt):
    t = ""
    ts = []
    txt = txt.replace("\r\n","")
    txt = txt.replace("\n","")
    # print(txt)
    for i in count():
        if "<" == txt[0]:
            txt = txt[txt.find(">")+1:]
            # print(txt)
        else:
            if ">" == txt[len(txt)-1]:
                txt = txt[:txt.rfind("</")]
                # print(txt) 
            else:
                if ">" in txt:
                    t,txt = txt.split("<",1)
                    txt = "<"+txt
                    ts.append(t)
                    continue
                else:
                    if len(ts) > 0:
                        ts.append(txt)
                    break
    # print(ts)
    if len(ts) > 1:
        txt = ""
        for t in ts:
            txt += t + "\n"
    return txt

def title_load(title):
    nosave=["\\","/",":","*","?",'"',"<",">","|"]
    oksave=["⧹","⧸","：","＊","？",'＂',"＜","＞","｜"]

    for ns in nosave:
        title = title.replace(ns,oksave[nosave.index(ns)])
    return title

burl="https://www.animatetimes.com/tag/details.php?id=5947"

try:
    all = urllib.request.urlopen(burl).readlines()
except urllib.error.URLError:
    print("\""+burl+"\""+" Not Found")
for h in range(len(all)):
    all[h] = all[h].decode("utf-8")

id = []
idm = ""
tin = []
end = False
la = len(all)
mtitle = []
for i,data in enumerate(all):
    if "アニメ一覧目次</h2>" in data:
        for j in range(i,la):
            if "</div>" in all[j]:
                # end = True
                break
            elif "<li>" in all[j] and "（再放送）" not in all[j]:
                id.append(all[j][all[j].find("\"#")+2:all[j].find("\">")])
                tis = indata(all[j]).replace("\n","").replace("\r","")
                tis = re.sub(" ([2-99]+)期","第\\1期",tis)
                tis = re.sub("第([2-99]+)クール","第\\1期",tis)
                tin.append(title_load(tis))
                # print(tis)
    # elif re.search("id=\"[1-"+idm+"]+\"",data):
    elif "c-heading-h2" in data:
        # print("id = "+data[data.find("id=")+4:data.find("\">")])
        idx = data[data.find("id=")+4:data.find("\">")]
        for sid,d in enumerate(id):
            if d == idx:
                # print(tin[sid])
                md = False
                for k in range(i,la):
                    if "</table>" in all[k]:
                        break
                    elif "OP：" in all[k]:
                        mtitle.append(title_load(tin[sid]+" OP("+indata(all[k][all[k].rfind("「")+1:all[k].rfind("」")])+") ||"+indata(all[k][all[k].rfind("」")+1:all[k].rfind("<br")])).replace("\n","")+"\n")
                    elif "ED：" in all[k]:
                        mtitle.append(title_load(tin[sid]+" ED("+indata(all[k][all[k].rfind("「")+1:all[k].rfind("」")])+") ||"+indata(all[k][all[k].rfind("」")+1:all[k].rfind("公開開始年＆季節")])).replace("\n","")+"\n")
                break
    if end:
        break

# print(mtitle[len(mtitle)-1])
# print(id)
# exit()
# print(title)
with open("all","r",encoding="UTF-8",newline="\n") as f:
    all_data = f.readlines()

wd = []
for ad in all_data:
    for ti in tin:
        if ti in ad:
            wd.append(ad)

with open("now","w+",encoding="UTF-8",newline="\n") as f:
    f.writelines(wd)

print("update now")

for w in wd:
    for m in mtitle:
        if w[:w.rfind(".")] == m.rstrip():
            mtitle.remove(m)
            break

with open("url","a+",encoding="UTF-8",newline="\n") as f:
    f.writelines(mtitle)

print("update url")