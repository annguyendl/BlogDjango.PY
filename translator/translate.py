from googletrans import Translator
import os

def translate(text):
    translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.com.vn',
    ])    
    translation = translator.translate(text, dest='vi')

    return translation.text