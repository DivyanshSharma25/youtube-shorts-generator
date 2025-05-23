from llm_model import lama_api,gemini_api
models={'lama': lama_api,'gemini':gemini_api}
def get_script(prompt,model_name):
        model=models[model_name]
        return model.get_script(prompt)
        

#print(data)