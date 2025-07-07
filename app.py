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

    context += summary

    return context

system_prompt = get_system_prompt_context()

print(system_prompt)
