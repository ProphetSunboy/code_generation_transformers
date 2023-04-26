import keyboard
import pyperclip
import time
import PIL.Image
import pystray
from threading import Thread

from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "Salesforce/codegen-350M-multi"

model = AutoModelForCausalLM.from_pretrained(checkpoint)

tokenizer = AutoTokenizer.from_pretrained(checkpoint)

def generate_code(text, max_tokens, temperature):
    completion = model.generate(**tokenizer(text, return_tensors="pt"),
                                max_new_tokens=max_tokens,
                                temperature=temperature)              
    return tokenizer.decode(completion[0])