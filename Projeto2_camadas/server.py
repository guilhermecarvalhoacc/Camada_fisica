#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação
####################################################


#esta é a camada superior, de aplicação do seu software de comunicação serial UART.
#para acompanhar a execução e identificar erros, construa prints ao longo do código! 


from enlace import *
import time
import numpy as np

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
serialName = "/dev/ttyACM1"           # Ubuntu (variacao de)
imageW = './img/recebidaCopia.jpg'
def main():
    try:
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com2 = enlace(serialName)
        
    
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        com2.enable()
        #Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        print('A comunicação foi aberta com sucesso!')
        
        #tamanho = com2.rx.getBufferLen()

        rxbuffer, nrxbuffer = com2.getData(4)
        print("Recebi 4 bytes")
        com2.sendData(rxbuffer)
        print("enviei pro client")
        valor1 = int.from_bytes(rxbuffer, byteorder='big') 
        rxBuffer,nrxBuffer = com2.getData(valor1)
        print("recebi tudo!")

       # while tamanho < 760:
        #    tamanho = com2.rx.getBufferLen()

 
        print('Salvando dados dos arquivos: ')
        f = open(imageW, 'wb')
        f.write(rxBuffer)
            
    
        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com2.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com2.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
