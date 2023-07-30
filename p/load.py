import argparse
from yt_dlp import YoutubeDL
import subprocess
import time
import os
# import ffmpeg

parser = argparse.ArgumentParser()
parser.add_argument("-u","--url",default="url.txt")
args = parser.parse_args()

def title_load(res):
    nosave=["\\","/",":","*","?",'"',"<",">","|"]
    oksave=["⧹","⧸","：","＊","？",'＂',"＜","＞","｜"]

    title = res['title']
    for ns in nosave:
        title = title.replace(ns,oksave[nosave.index(ns)])
    return title

def mp3_converter(res):
    com = "ffmpeg -i \""+title+".webm\" -vn -ab 128k -ar 44100 -y -hide_banner -loglevel error \""+title+"_.mp3\""
    p = subprocess.Popen(com,shell=True)
    print("mp3に変換中",end="")
    while p.poll() == None:
        print(".",end="",flush=True)
        time.sleep(1)
    os.remove(title+".webm")
    print("成功!")

    # stream = ffmpeg.input(title+'.webm')
    # stream = ffmpeg.output(stream, title+'.mp3', format='mp3')
    # ffmpeg.run(stream)

    com = "ffmpeg -i \""+title+"_.mp3\" -vn -af volumedetect -hide_banner -f null -"
    res = subprocess.run(com,shell=True,capture_output=True)
    log = res.stderr.decode("utf-8")
    log = log[log.find("mean_volume")+13:]
    log = log[:log.find(" dB")]

    vodb = 10**((-19.8-(float(log)))/20)
    com = "ffmpeg -i \""+title+"_.mp3\" -vn -af volume="+str(vodb)+" -hide_banner -loglevel error \"down/"+title+".mp3\""
    p = subprocess.Popen(com,shell=True)
    print("音量調整中",end="")
    while p.poll() == None:
        print(".",end="",flush=True)
        time.sleep(1)
    os.remove(title+"_.mp3")
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
        res = ydl.extract_info(url)
        title = title_load(res)
        mp3_converter(title)
    with open("URL.txt",'w') as f:
        f.write("")
