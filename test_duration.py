import json

def get_audio_duration(file_path):
    """返回音频文件的时长，单位为秒"""
    with open(file_path,"r") as f:
        js=json.loads(f.read())
        duration=js['voice_activity'][-1][-1]


    # audio = AudioSegment.from_file(file_path)
    # return len(audio) / 1000  # 返回时长，单位为秒
    return duration

if __name__=="__main__":
    file="/mnt/data/user/fan_xiaoran/librilight/small/100/sea_fairies_0812_librivox_64kb_mp3/01_baum_sea_fairies_64kb.json"
    print(get_audio_duration(file))