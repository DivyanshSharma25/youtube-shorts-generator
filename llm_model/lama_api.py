import requests
import json
def get_script(prompt):
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer your api key",
    },
    data=json.dumps({
        "model": "meta-llama/llama-3.1-8b-instruct:free", # Optional
        "messages": [
        {
            "role": "user",
            "content": prompt,
        }
        ]
        
    })
    )
    
    return response.json()['choices'][0]['message']['content'].strip('"').replace('.',',')