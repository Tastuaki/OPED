import subprocess
import os
import codecs
import io
import glob

# tdata = []
# con = ""

os.chdir('../g')
# os.chdir('../p/down')

base = os.getcwd()
files_path = glob.glob(os.path.join(base,"*.mp3"))
files = [os.path.basename(i) for i in files_path]

# with open("../new",'w+', encoding='utf-8') as f:
with open("../p/game",'a+', encoding='utf-8') as f:
    for row in files:
        if("〜" in row):
            orow = row
            row = row.replace("〜","～")
            os.rename(base+"\\"+orow,base+"\\"+row)
        row =r"g/"+ row +"\n"
        f.writelines(row)

# out = subprocess.run(["dir","*.mp3","/b",">","++title.txt"],shell=True)

# git ls-tree -r --name-only HEAD > +title.txt
# out = subprocess.run(["git","ls-tree","-r","--name-only","HEAD",">","+title.txt"],shell=True)

# with open("++title.txt", "rb") as src, open("+title.txt", "wb") as dest:

#     # 変換ストリームを作成
#     stream = codecs.StreamRecoder(
#         src,
#         codecs.lookup("utf_8").encode, codecs.lookup("shift_jis").decode,
#         src_codec.streamreader, dest_codec.streamwriter,
#     )
#     reader = io.BufferedReader(stream)

#     while True:
#         data = reader.read1()
#         if not data:
#             break
#         dest.write(data)
#         dest.flush()

# with open("+title.txt","r+",encoding="utf-8") as f:
#     tdata=f.readlines()
#     f.truncate(0)
#     f.seek(0)
#     for con in tdata:
#         if "mp3" in con:
#             f.write(con.replace("\'",""))