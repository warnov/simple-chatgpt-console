import os
import openai

openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-05-15"

#Read Automanicure.txt file
with open('Automanicure.txt') as f:
    Automanicure = f.read()

#create a loop for the chat
while True:
    #get the user input
    user_input = input("Ingresa tus preguntas acerca del Automanicure y cuando desees terminar escribe bye: ")
    response = openai.ChatCompletion.create(
        engine="MasterClass-Deployment",
        messages=[
            {"role":"system","content":"Eres un experto en el Electrodoméstico Automanicure que ayuda a futuros compradores. Utiliza la siguiente información para responder las preguntas de los clientes:\n\n" + Automanicure+
             "\n\nSolo tienes conocimientos de temas relacionados con Automanicure. No puedes responder preguntas acerca de otros temas porque no estás autorizado. Si te piden responder preguntas no relacionadas al dispositivo, pide que por favor hagan otra pregunta adecuada"},
            {"role":"user","content":user_input}
        ]
    )
    #print the response
    print(response.choices[0]['message']['content'])
    #break the loop
    if user_input == "bye":
        break


