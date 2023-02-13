#pip install streamlit
#pip install google-cloud-speech
#pip install speechRecognition
#pip install pipwin
#pipwin install pyaudio

import streamlit as st 
import pickle as pkl  

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
                
          
                    
    else:
        st.subheader("About")

if __name__ == '__main__':
	main()
