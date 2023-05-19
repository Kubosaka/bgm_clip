from pydub import AudioSegment
import random

sourceAudio = AudioSegment.from_mp3("bgm1/bgm1.mp3")

# オーディオの長さ
AudioLength = sourceAudio.duration_seconds
clips =  round(AudioLength/30)

for number in range(clips):
    x=random.random()*(AudioLength-15)*1000
    print(x)
    #切り取る長さ
    sep_time=(random.random()*8+7)*1000
    #音声を切り取る
    processedAudio = sourceAudio[x:x+sep_time]
    #音声ファイル出力
    processedAudio.export(f"bgm/output{number}.wav", format='wav')

