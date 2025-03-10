from gtts import gTTS
import pygame
import os

def tts():
    audio = 'speech.mp3'
    language = 'en'
    sentence = input("Enter the text to be spoken :- ")
    
    tts = gTTS(text=sentence, lang=language)
    tts.save(audio)
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        continue

    os.remove(audio)

if __name__ == "__main__":
    tts()
