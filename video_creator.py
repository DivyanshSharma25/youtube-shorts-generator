from enum import Enum
import script_extractor
import voiceover
from random import randint
import time_stamps
from moviepy import VideoFileClip, TextClip, CompositeVideoClip ,AudioFileClip,CompositeAudioClip
import math
import os,random
def get_random_file_path(folder_path):
    files = os.listdir(folder_path)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    random_file = random.choice(files)
    return os.path.join(folder_path, random_file)


class font(Enum):
        roboto='fonts\Roboto\static\Roboto_SemiCondensed-ExtraBoldItalic.ttf'
        montserrat='fonts\Montserrat\static\Montserrat-SemiBoldItalic.ttf'
        banger='fonts\Bangers\Bangers-Regular.ttf'

prompts=['for a viral youtube short write just one complete 30-40 second script, the video is about a space fact write just the voiceover, it should contain an initial hook dont write anything else than the fact .your reply message should only contain the fact do not write the whole script',
            'write a just one complete script for a intresting facts about fitness for a viral 30-40 second youtube short video write just the thing to say dont write anything else it should have an intial hook .your reply message should only contain the fact do not write the whole script' ,
            'write a just one complete script for a intresting useless fact containing some naughty or funny element for a viral 30-40 second youtube short video write just the thing to say dont write anything else it should have an intial hook  .your reply message should only contain the fact do not write the whole script',
            'write a just one complete intresting useless facts for a viral 20-40 second youtube short video write just the thing to say dont write anything other than the fact it should have an intial hook  .your reply message should only contain the fact do not write the whole script',
            'say anything funny naughty for around 70 words and should contain an very strong intial hook',
            ]

def make_video(prompt,video_file_name):

    audio_file='result.wav'

    print("getting scripts .........")

    script=script_extractor.get_script(prompt=prompt,model_name='gemini')

    print("got scripts succesfully.........")
    print(script)

    print("getting voiceover .........")
    voic=voiceover.voiceover()
    voic.make_audio(script,audio_file)

    print("got voiceover succesfully.........")
    print("getting timstamps .........")

    words=time_stamps.get_timestamp(audio_file)

    print("got timstamps succesfully.........")
    print("getting everthing together .........")


    audioclip = AudioFileClip(audio_file)

    clip = VideoFileClip(get_random_file_path("clips")).with_volume_scaled(0.8)
    st=random.randrange(0,math.floor(clip.duration-audioclip.duration))
    clip=clip.subclipped(st,st+audioclip.duration)
    width, height = clip.size

    clip.audio=audioclip


    txt_clips=[]
    for i in words:
        a=1 if (words.index(i)+1)!=len(words) else 0
        txt_clip = TextClip(
            font=font.banger.value,
            text=i.word,
            font_size=150,
            color='white',
            stroke_color='black',
            stroke_width=8,
            text_align='center'
            
        ).with_duration(words[words.index(i)+a].start-i.start).with_start(i.start).with_position(('center',height*0.6))
        
        txt_clips.append(txt_clip)

    final_video = CompositeVideoClip([clip]+txt_clips)
    final_video.write_videofile(video_file_name)

    print("got video succesfully.........")
    
    data=script
    data+='\n'+script_extractor.get_script(f"'{script}' give me title and description for this youtube video in the formate 'title: the title \n description: the description'",'gemini')
    file=open(video_file_name.split(".")[0]+"_details.txt",'w')
    file.write(data)
    file.close()

# for i in range(5):
#     make_video(prompts[4]+"seed:"+str(random.random()),'final/v'+str(i)+'.mp4')

# for i in range(5):
#     make_video(prompts[4],'final/v'+str(i)+'.mp4')

make_video('''tell me something random and funny
''','final/v'+'v10.mp4')