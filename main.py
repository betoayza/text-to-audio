from gtts import gTTS
import os

audios_path = "audios"
audios = os.listdir(audios_path)

if '.gitkeep' in audios:
    audios.remove('.gitkeep')

if len(audios) == 0:
    i = 1
else:
    i = len(audios)+1

is_running = True

print("Welcome to Text To Audio!\n")

while is_running: 
    audio = f"audios/audio{i}.mp3"
    language = 'en'
    text = input("Enter your text here [-1 to exit]: ")

    if text == "-1":
        is_running = False
    else:
        sp = gTTS(text, lang=language, slow=False)
        sp.save(audio)
        i += 1   

print("\nThanks for try me, see on!")