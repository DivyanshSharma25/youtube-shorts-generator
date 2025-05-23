import google.generativeai as genai
import os,re
import pandas as pd
import voiceover

def get_script(prompt):
        
        genai.configure(api_key="your api key")
        model = genai.GenerativeModel("gemini-1.5-flash")
        chat = model.start_chat(
            history=[
            ]
        )

        response = chat.send_message(prompt)

        text=response.text
        try:
                open('raw.txt','w').write(text)
        except:
                print("failed to save the scrip in a text file")
        if text.find('**Voiceover:**  ')!=-1:
                data=text[text.find('**Voiceover:**  ')+len('**Voiceover:**  '):]
        else:
                data=text

        pattern = r"\(.*?\)"
        cleaned_text = re.sub(pattern, "", data)

        cleaned_text = cleaned_text.strip()
        cleaned_text=cleaned_text.replace('*','')
        cleaned_text=cleaned_text.replace('�','')
        cleaned_text=cleaned_text.replace('  ',' ')
        cleaned_text=cleaned_text.replace(',',' ')
        try:
                open('cleaned.txt','w').write(cleaned_text)
        except:
                print("failed to save the scrip in a text file")
        
        return cleaned_text
