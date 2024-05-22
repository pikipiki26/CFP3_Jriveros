
#setuptools ==> 

#pip install apeechRecognition
#pip install setuptools
#pip install pyaudio



import speech_recognition as sr
#creamos instancia de recognizer,que es la clase principal para reconocimiento de voz

r= sr.Recognizer()
#USAR el microfono como fuente de audio 

with sr.Microphone() as sourse:
    #imprime un mensaje indicando que el programa esta escuchando
    print("estoy escunchando....")
    #escucha el audio desde el microfono
    audio= r.listen(sourse)
    
          
try:
    #intentamos reconocer el audio usando el servidor de reconocimiento de google
    #especificar que el audio es epañol
    text=  r.recognize_google(audio,languaje='es-ES')
    print("transcripcion exitosa: {}" .format(text))
          
except:
    print("no se pudo reconocer el audio")           




