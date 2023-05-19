from pydub import AudioSegment
import random
import os
from glob import glob
import datetime


bgm_dir = os.getcwd()

bgm_dir+="/bgm1"

path_list = glob(os.path.join(bgm_dir, "*.mp3"))
word="bgm"

for i,path in enumerate(path_list):
    #dirnameはdataが入っているdir,fileは処理するfile名
    dirname, file = os.path.split(path)
    audiofile="bgm1/"+file

    #オーディオ読み込み
    sourceAudio = AudioSegment.from_mp3(audiofile)
    #長さ取得
    AudioLength = sourceAudio.duration_seconds
    #幾つのクリップ作るか
    clips =  round(AudioLength/45)

    for number in range(clips):
        x=random.random()*(AudioLength-15)*1000
        #切り取る長さ
        sep_time=(random.random()*8+7)*1000
        #音声を切り取る
        processedAudio = sourceAudio[x:x+sep_time]
        #音声ファイル出力
        processedAudio.export(f"bgm/bgm{i+1}_{number+1}.wav", format='wav')





