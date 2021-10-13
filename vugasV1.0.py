from gtts import gTTS
import os

msg = "You Have been Hacked"
language = 'en'

obj = gTTS(text=msg, lang=language, slow=False)
obj.save('Virus.mp4')

os.system('mpg321 Virus.mp4')