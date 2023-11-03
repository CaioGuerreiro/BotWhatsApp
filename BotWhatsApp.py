# importar bibliotecas nescessárias
import pywhatkit
import time
import keyboard
from datetime import datetime
# definir para quais contatos as mensagens irão ser enviadas

contatos = ['number1','number2'] 
cont = 0
# definir intervalo de envio

while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0],'Hello, World', datetime.now().hour, datetime.now().minute + 1)
    del contatos[0+cont]
    cont += 1
    time.sleep(1)
    keyboard.press_and_release('ctrl + w')
# teste