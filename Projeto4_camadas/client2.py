from enlace import *
import time
import numpy as np
from tkinter.filedialog import askopenfilename
from funcoes import *


serialName = "/dev/ttyACM0"      

nome_arquivo = askopenfilename()
imageR = nome_arquivo 
def main():
    try:
        com1 = enlace(serialName)
        
        com1.enable()

        imagem = open(imageR, 'rb').read()
        lista_payload = divide_pacotes(imagem)
        for i in lista_payload:
            print(i,"\n")
        lista_pacotes = cria_pacotes(lista_payload)
        for pacotes in lista_pacotes:
            print(pacotes,"\n")
            print(len(pacotes))
        handshake = cria_handshake(len(lista_payload))
        print(f"ESSE É O HANDSHAKE: {handshake}")




        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()

main()