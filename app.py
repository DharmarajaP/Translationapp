#pip install streamlit
#pip install google-cloud-speech
#pip install speechRecognition
#pip install pipwin
#pipwin install pyaudio

import streamlit as st 
import string 
import random 
import pickle as pkl  
import io
import os
from io import StringIO
from google.cloud import speech_v1
from google.cloud.speech_v1 import types
#from google.cloud.speech_v1 import enums
from google.cloud.speech_v1.types import RecognitionAudio

import speech_recognition as sr
import wave
import numpy as np
# loading in the model to predict on the data  
pickle_in1 = open(r'C:\Users\Dharma\lrmodel_new.pckl', 'rb')  
classifier1 = pkl.load(pickle_in1)  

from google.cloud import speech
import io
import json
import os

# Load the private key as a JSON file
private_key_file = r'C:\Users\Dharma\folkloric-ocean-377504-674432cd7e4a.json'
with open(private_key_file) as f:
    private_key = json.load(f)

# Set the environment variable for the private key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = private_key_file
# create client instance 
client = speech.SpeechClient()


def transcribe_voice_input1(file_name):
        #the path of your audio file
        file_name1 = r'C:\Users\Dharma\OSR_us_000_0010_8k.wav'
                       
        st.write(file_name)
        with io.open(file_name1, "rb") as audio_file:
            content = audio_file.read()
            audio = speech.RecognitionAudio(content=content)
            
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            enable_automatic_punctuation=True,
            audio_channel_count=1,
            language_code="en-US",
        )

        # Sends the request to google to transcribe the audio
        response = client.recognize(request={"config": config, "audio": audio})
        # Reads the response
        output = ""
        for result in response.results:
            #print("Transcript: {}".format(result.alternatives[0].transcript))
            #st.write("Transcript: {}".format(result.alternatives[0].transcript))
            output += format(result.alternatives[0].transcript)
                      
        return output
    
def french_to_englis_translat(term):
    result = term.upper()
    return result

def prediction1(raw_text):    
     
    prediction1 = classifier1.predict([raw_text])  
    print(prediction1)  
    return prediction1

def transcribe_audio(audio_content):
    client = speech_v1.SpeechClient()

    # The language of the supplied audio
    language_code = "en-US"

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 44100

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }
    audio = {"content": audio_content}

    response = client.recognize(config, audio)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        return result.alternatives[0].transcript


def transcribe_voice_input():
    # Record audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            audio = r.listen(source)
            transcribed_text = r.recognize_google(audio)
            if transcribed_text.lower() == "stop":
                break
        st.write(transcribed_text)
    return transcribed_text


        
def main():
    st.title("Intelligent Language translator")
    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    
    if choice == "Home":
        #st.subheader("Home")
        #form
        with st.form(key="myform",clear_on_submit=True):

            input_type = st.empty()
            input_type_value = st.empty()

        if input_type_value.empty:
            input_type = st.radio("Choose input type:", ["Text", "Audio", "File", "Voice"], key='input_type')
            input_type_value = input_type
            output_text = ""
            st.write("input_type_value:", input_type_value)
            
            if input_type == "Text":
                text_input = st.text_input("Enter some text:")
                output_text = "You entered: " + text_input

            elif input_type == "Audio":
                audio_file = st.file_uploader("Upload an audio file:", type=["wav", "mp3"])
                st.write(audio_file)
                if audio_file is not None:
                    path_in = audio_file.name
                    folder_path = r"C:\Users\Dharma\\"
                    output_text = transcribe_voice_input1 (folder_path+path_in)
            elif input_type == "File":
                file = st.file_uploader("Upload a file:")
                if file:
                    file_content = file.read().decode("utf-8")
                    output_text  = file_content
            elif input_type == "Voice":
                #import speech_recognition as sr

                #r = sr.Recognizer()

                #st.write("Say something:")
                #with sr.Microphone() as source:
                    #audio = r.listen(source)

                #recognized_text = r.recognize_google(audio)
                #st.write("You said:", recognized_text)
                #output_text = "You said: " + recognized_text
                transcribed_text = transcribe_voice_input()
                st.write("Transcribed Text:", transcribed_text)    
                
            st.text_area("Output", output_text)
            
                      
            
            raw_text = ""
                                           
            result2 = ""
            st.write(1)
            langage_iden = st.form_submit_button("Language Identification")
            st.write(2)
            if langage_iden:
                st.write(3)                        
                result2 = prediction1 (raw_text)
            
            col1, col2 = st.columns(2)
            
            with col1:
                source_task_choice = st.selectbox("Source Language",result2)
            with col2:
                target_task_choice = st.selectbox("Targat Language",result2)
                
            submit_button = st.form_submit_button("Translate")
            if submit_button:
                #result = prediction1 (raw_text)   
                #raw_text1 = st.text_area("Translated language text")
                
                if target_task_choice == "French":
                    results = french_to_englis_translat(raw_text)
                    #title = st.text_input('Translated language text')
                    title = st.text_area('Translated language text', value=results, height=None, max_chars=None, key=None)
                    #title = st.text_input('Translated language text')
                    #st.write(title)
 
    else:
        st.subheader("About")

if __name__ == '__main__':
	main()