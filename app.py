import os, json # os is run to system commands and json is to handle json files 

from dotenv import load_dotenv # this file is to load .env variables

from openai import OpenAI

from pypdf import PdfReader
import gradio as gr 

load_dotenv(override = True)

