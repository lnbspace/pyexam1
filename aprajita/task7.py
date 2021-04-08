pip install gTTS
pip install os
f=open('Song.txt')
x=f.read()
language='en'
audio=gTTS(text=x,lang=language,slow=false)
audio.save("task7.wav")
os.system