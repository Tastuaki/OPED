import argparse
from yt_dlp import YoutubeDL
import subprocess
import time
import os
# import ffmpeg

parser = argparse.ArgumentParser()
parser.add_argument("-u","--url",default="url.txt")
args = parser.parse_args()

def title_load(title):
    nosave=["\\","/",":","*","?",'"',"<",">","|","\n"]
    oksave=["⧹","⧸","_","＊","？",'＂',"＜","＞","｜"," "]

    for ns in nosave:
        title = title.replace(ns,oksave[nosave.index(ns)])
    return title

def mp3_converter(res,title=""):
    btitle = res['title']
    btitle = title_load(btitle)
    if title == "":
        title = btitle
    else:
        title = title_load(title)
    com = "ffmpeg -i \""+btitle+".webm\" -vn -ab 128k -ar 44100 -y -hide_banner -loglevel error \""+btitle+"_.mp3\""
    p = subprocess.Popen(com,shell=True)
    print("mp3に変換中",end="")
    while p.poll() == None:
        print(".",end="",flush=True)
        time.sleep(1)
    os.remove(btitle+".webm")
    print("成功!")

    # stream = ffmpeg.input(title+'.webm')
    # stream = ffmpeg.output(stream, title+'.mp3', format='mp3')
    # ffmpeg.run(stream)

    com = "ffmpeg -i \""+btitle+"_.mp3\" -vn -af volumedetect -hide_banner -f null -"
    res = subprocess.run(com,shell=True,capture_output=True)
    log = res.stderr.decode("utf-8")
    log = log[log.find("mean_volume")+13:]
    log = log[:log.find(" dB")]

    vodb = 10**((-19.8-(float(log)))/20)
    com = "ffmpeg -i \""+btitle+"_.mp3\" -vn -af volume="+str(vodb)+" -hide_banner -loglevel error \"down/"+title+".mp3\""
    p = subprocess.Popen(com,shell=True)
    print("音量調整中",end="")
    while p.poll() == None:
        print(".",end="",flush=True)
        time.sleep(1)
    os.remove(btitle+"_.mp3")
    print("成功!")

options={
    'outtmpl' : '%(title)s'+'.webm',
    'format':'bestaudio'
}
ydl = YoutubeDL(options)
if args.url != "url.txt":
    res = ydl.extract_info(args.url)
    title = title_load(res)
    mp3_converter(title)
else:
    with open("URL.txt",encoding="UTF-8") as f:
        data = f.readlines()
    for url in data:
        url = url.replace("\n","")
        title = url[url.find(" ")+1:]
        url = url[:url.find(" ")]
        res = ydl.extract_info(url)
        mp3_converter(res,title)
    with open("URL.txt",'w') as f:
        f.write("")
