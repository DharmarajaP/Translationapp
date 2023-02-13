#pip install streamlit
#pip install google-cloud-speech
#pip install speechRecognition
#pip install pipwin
#pipwin install pyaudio

import streamlit as st 

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
                text_input = st.text_input("Enter some text:")
                output_text = "You entered: " + text_input
            elif input_type == "File":
                text_input = st.text_input("Enter some text:")
                output_text = "You entered: " + text_input
            elif input_type == "Voice":
                text_input = st.text_input("Enter some text:")
                output_text = "You entered: " + text_input   
                
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
                    title = st.text_input('Translated language text')
 
    else:
        st.subheader("About")

if __name__ == '__main__':
	main()
