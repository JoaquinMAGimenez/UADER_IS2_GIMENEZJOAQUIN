#tp2.py
#!/usr/bin/python
import sys
import openai
#……. [ mas Código de inicialización aqui ] …………
print('Hola soy la IA chatGPT quien contestara sus preguntas')       
try:
    consulta = input('ingrese un texto:')
    if not consulta:
          raise ValueError
except ValueError:
        print("no ingresaste ningun texto intente de nuevo")
        if len(consulta)==0:
            print("se necesita ingresar un texto")
            sys.exit()
        else:
            userText = "You: " + consulta    
        sys.exit() 
         
try:
    openai.api_key = "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"
    TOP_P=1
    FREQ_PENALTY=0
    PRES_PENALTY=0
    STOP=None
    MAX_TOKENS=1024
    TEMPERATURE=0.75
    NMAX=1
    MODEL_ENGINE = "text-davinci-003"        
        #…..[otra lógica necesaria – el texto del prompt debe colocarse en userText]….. 
        # Set up the model and prompt


    completion = openai.Completion.create(
        engine=MODEL_ENGINE,
        prompt=userText,
        max_tokens=MAX_TOKENS,
        n=NMAX,
        top_p=TOP_P,
        frequency_penalty=FREQ_PENALTY,
        presence_penalty=PRES_PENALTY,
        temperature=TEMPERATURE,
        stop=STOP)
    respuesta=completion.choices[0].text    
    print('ChatGPT'+respuesta) 
except:
       print("no puedo darte una respuesta")
             