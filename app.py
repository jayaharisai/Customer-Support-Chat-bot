import streamlit as st
import json
from langchain_openai import OpenAI

import os

configuration_file_path = 'configuration.json'
templates_path = 'templates.json'

with open(configuration_file_path, 'r') as file:data = json.load(file)
with open(templates_path, 'r') as file:templatesdata = json.load(file)

menu = st.sidebar.radio("Menu", ["Chat", "Templates", "Configuration", "About"])

if menu == "Chat":
    if len(data["OpenAI Key"]) == 0:
        st.title("Chat")
        st.text("Open AI is not configured to chat, try to configire the Open AI key in configuration page.")

    else:
        os.environ["OPENAI_API_KEY"] = data["OpenAI Key"]

        left_column, right_column = st.columns([3,2])

        with left_column:
            st.title("Chat")
            
            question =  st.text_input("Ask me a question")
            

        with right_column:
            templates = [template for template in templatesdata]
            select_templete = st.radio("Select a color", templates)

        
        if len(question)> 0:
            llm = OpenAI(temperature=0.8)
            template = f"{templatesdata[select_templete]} question: {question}."
            ai_msg = llm.predict(template)

            st.write(ai_msg)


    
    

if menu == "Templates":
    
    st.title("Templates")
    left_column, right_column = st.columns([2,3])

    with left_column:
        st.subheader("Input Fields")
        title = st.text_input("Template name")
        large_text = st.text_area("Enter your text here:", height=200)
        if st.button("Double click to save"):
            if len(title) > 0:
                templatesdata[title] = large_text
                with open(templates_path, 'w') as file:
                    json.dump(templatesdata, file, indent=4)
            
        

    with right_column:
        for i in templatesdata:
            st.subheader(i)
            st.write(templatesdata[i])
            st.markdown("---")

    # Reset input values
    title = ""
    large_text = ""

    
if menu == "Configuration":
    st.title("Configuration")
    st.subheader("Configure OpenAI Key")

    if len(data['OpenAI Key']) == 0:
        st.text("Configure you open ai key to access the OPENAI API to chat with your own chat bot.")
        with st.form(key='user_form'):
            Openaikey = st.text_input("OpenAI Key")

            submit_button = st.form_submit_button(label='Double click to submit')
        data['OpenAI Key'] = Openaikey

        with open(configuration_file_path, 'w') as file:
            json.dump(data, file, indent=4)

        

    else:
        st.text(data['OpenAI Key'])
        edit = st.button("Edit")
        if edit:
            with st.form(key='user_form'):
                Openaikey = st.text_input("OpenAI Key")
                submit_button = st.form_submit_button(label='Submit')
            
            data['OpenAI Key'] = Openaikey

            with open(configuration_file_path, 'w') as file:
                json.dump(data, file, indent=4)
            st.rerun()

        
  
if menu == "About":
    st.title("About")
    st.subheader("Introduction")
    st.write("Welcome to our innovative project – a custom chatbot leveraging the power of the OpenAI API! Our endeavor aims to revolutionize conversational interfaces by offering a versatile platform where users can seamlessly interact with various prompt templates.")
    st.write("At the heart of our project lies a configurable system, allowing users to easily integrate their OpenAI API key, empowering them to harness the full potential of AI-driven conversations. Whether it's for customer service, creative writing, or educational purposes, our chatbot stands ready to adapt to diverse needs.")
    st.write("Our intuitive configuration page streamlines the setup process, ensuring a hassle-free experience for users. Once configured, the possibilities unfold in our interactive playground, where you can explore and test different prompt templates, experiencing firsthand the versatility and adaptability of our chatbot solution.")
    st.write("Join us as we embark on a journey to redefine the boundaries of human-AI interaction. Welcome to the future of conversational technology – welcome to our custom chatbot project powered by OpenAI.")

    st.title("Features")
    st.subheader("Configuration Page")
    st.write("The configuration page serves as the gateway to unlocking the full potential of our custom chatbot project. Here, users can seamlessly integrate their OpenAI API key, enabling the chatbot to access the robust capabilities of the OpenAI platform. With a user-friendly interface and intuitive controls, configuring the chatbot has never been easier. Say goodbye to complex setup procedures and hello to a streamlined experience, empowering users to harness the power of AI effortlessly.")

    st.subheader("Prompt Templates Playground")
    st.write("Step into our playground – a dynamic space where you can explore and test a myriad of prompt templates. Whether you're seeking inspiration for creative writing, fine-tuning responses for customer service scenarios, or experimenting with educational prompts, our playground provides the perfect environment to unleash your creativity. With real-time feedback and interactive controls, you can iterate, refine, and customize prompt templates to suit your specific needs. Get ready to immerse yourself in a world of possibilities as you embark on an interactive journey of discovery within our prompt templates playground.")