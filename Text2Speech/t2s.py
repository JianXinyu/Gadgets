#!/usr/bin/python
# -*- coding: utf-8 -*-

from google.cloud import texttospeech
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:\key.json"

import re
# from langdetect import detect
import langid # higher accuracy than langdetect, can select from desired languages

def t2s(lang, text, filename):
        # Instantiates a client
        client = texttospeech.TextToSpeechClient()

        # Set the text input to be synthesized
        synthesis_input = texttospeech.types.SynthesisInput(text=text)

        # Build the voice request, select the language code ("en-US") and the voice type
        # https://cloud.google.com/text-to-speech/docs/voices
        if lang == "en":
            voice = texttospeech.types.VoiceSelectionParams(
                language_code="en-US",
                name='en-US-Wavenet-C')
        elif lang == "zh":
            voice = texttospeech.types.VoiceSelectionParams(
                language_code="cmn-CN",
                name = 'cmn-CN-Wavenet-A')

        # Select the type of audio file you want returned
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(synthesis_input, voice, audio_config)

        # The response's audio_content is binary.
        with open(filename+'.mp3', 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "'+filename+'.mp3"') 

# Logic:
# Read file text 
# Split paragraph
# Recognize language
# Turn each paragraph into speech
# Merge voice files
# Delete temporary files
if __name__ == "__main__":
    
    p=re.compile('\n',re.S)
    fileContent=open('test.txt','r',encoding='utf8').read() # Read file text
    paraList=p.split(fileContent) # split the text by line break

    for paraIndex in range(len(paraList)): # traverse the sliced text list
        langid.set_languages(['zh', 'en']) # ISO 639-1 codes, set language pool
        lang, score = langid.classify(paraList[paraIndex]) # recognize language
        
        if lang == "en" or lang == "zh":
            # text to speech, save each paragraph as a single .mp3 file
            t2s(lang, paraList[paraIndex], str(paraIndex))
        else: 
            # if something wrong, write the text to file to check
            # print(paraList[paraIndex], lang, score)
            fileWriter=open(str(paraIndex)+'.txt','a',encoding='utf8')
            fileWriter.write(paraList[paraIndex]) 
            fileWriter.close() 

    # Merge all .mp3 files into a single one
    # Delete temporary .mp3 files
    mp3_write = open('test.mp3', 'wb')
    for paraIndex in range(len(paraList)):
        f_read = open(str(paraIndex)+'.mp3', 'rb')
        mp3_write.write(f_read.read())
        f_read.close()
        os.remove(str(paraIndex)+'.mp3')
    mp3_write.flush()
    mp3_write.close()
    print('finished')
