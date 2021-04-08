
from enlace import *
import time
import numpy as np
serialName = "/dev/ttyACM1"           
imageW = './img/recebidaCopia.jpg'
com2 = enlace(serialName)
com2.enable()


def recebe_heade():
    r_header, len_r_header = com2.getData(10)
    return r_header,len_r_header


def recebe_handshake():
    recebe_handshake = com2.getData(14)[0]
    print(recebe_handshake)


def main():
    try:

        # f = open(imageW, 'wb')
        # f.write(rxBuffer)
        
        recebe_handshake()
    
        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com2.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com2.disable()
        
if __name__ == "__main__":
    main()