import os, json # os is run to system commands and json is to handle json files 

from dotenv import load_dotenv # this file is to load .env variables

from openai import OpenAI

from pypdf import PdfReader
import gradio as gr 

load_dotenv(override = True)

def get_system_prompt_context():
    reader = PdfReader("./me/Profile.pdf")
    context = "Linkedin Profile: \n \n"
    for page in reader.pages:
        text = page.extract_text()
        if text:
            context += text + "\n\n\n"

    summary = open("./me/summary.txt", 'r').read()
    
    context += "Dilina Perera Summary: \n\n"

    context += summary + "\n\n"

    context += "INSTRUCTIONS:\n\n\n"

    context += "You will be acting as Dilina Perera and you will answer questions on behalf of him. you will be integrated into a his website and you will answer questions as him"

    return context

system_prompt = get_system_prompt_context()

# setup openai-client
client = OpenAI()

messages = [
    {'role' : 'system', 'content' : system_prompt},
    {'role' : 'user' , 'content' : "What's your name?"}
]

response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)

print (response.choices[0].message.content)