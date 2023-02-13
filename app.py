#pip install streamlit
#pip install google-cloud-speech
#pip install speechRecognition
#pip install pipwin
#pipwin install pyaudio

import streamlit as st 
import pickle as pkl  
#import Credentials
#from google.oauth2.credentials import Credentials

# loading in the model to predict on the data  
pickle_in1 = open('lrmodel_new.pckl', 'rb')  
classifier1 = pkl.load(pickle_in1)  

def prediction1(raw_text):    
    prediction1 = classifier1.predict([raw_text])  
    return prediction1

def main():
    st.title("Intelligent Language translator")
    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    
    if choice == "Home":
        #st.subheader("Home")
        with st.form(key="myform"):

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
                text_input = st.text_input("Enter some text:")
                output_text = "You entered: " + text_input
            elif input_type == "File":
                file = st.file_uploader("Upload a file:")
                if file:
                    file_content = file.read().decode("utf-8")
                    output_text  = file_content
            elif input_type == "Voice":
                text_input = st.text_input("Enter some text:")
                output_text = "You entered: " + text_input   
                
            raw_text = st.text_area("Source Language Text", output_text)
            submitted = st.button("Submit")
            if submitted:
            	langage_iden = st.button("Language Identification")
                if langage_iden:
                    result2 = prediction1 (raw_text)
    else:
        st.subheader("About")

if __name__ == '__main__':
	main()
