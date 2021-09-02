'''
Created on 16 de jul. de 2021
Conversor de Texto para Audio
@author: Fabricio Calvete Campos
'''
# -*- encoding: utf-8 -*-

import pyttsx3

texto = "Olá tudo bem com vocês hoje iremos um programa diferente"

pyt = pyttsx3.init()
voices = pyt.getProperty('voices')

for voice in voices:
    print(voice, voice.id)
    
pyt.setProperty('voice', voices[0].id) 

rate = pyt.getProperty('rate')
pyt.setProperty('rate', rate-25)

pyt.say(texto)
pyt.runAndWait()

print('Fi')   
    




