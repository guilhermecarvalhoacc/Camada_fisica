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
import math 

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)

#Interface grafica implementada para achar o arquivo img, codigo referente ao stackoverflow.
from tkinter.filedialog import askopenfilename
from funcoes import *
nome_arquivo = askopenfilename()
print(nome_arquivo)
imageR = nome_arquivo 

certo = (9).to_bytes(2, byteorder='big')
errado =(7).to_bytes(2, byteorder='big')

def main():
    try:


        com1 = enlace(serialName)
    
        com1.enable()

        print('A comunicação foi aberta com sucesso!')
        
        txBuffer = open(imageR, 'rb').read()

        com1.sendData(cria_handshake(is_handshake=True))
        time_start = time.time()
        time.sleep(0.2)
        recebeu_resp_servidor = False
        while not recebeu_resp_servidor:
            time_over = time.time()
            if (time_over - time_start) >=5:
                mandar_dnv = input("mandar dnv?? (sim/nao): ")
                if mandar_dnv == "sim":
                    com1.sendData(cria_handshake(is_handshake=True))
                    time_start = time.time()
                elif mandar_dnv == "nao":
                    print("parar o codigo")

            recebeu_resposta = com1.rx.getBufferLen() != 0
            if recebeu_resposta == True:
                recebeu_resp_handshake = com1.getData(14)[0]
                recebeu_resp_servidor = True
                print(f"resposta do server:{recebeu_resposta}")
            

        time.sleep(0.5)


        lista_datagrama = Datagrama(txBuffer)
        contador = 1
        for pacote in lista_datagrama:
            com1.sendData(np.asarray(pacote))
            print(f"ESSE EH O PACOTE:  {pacote}")
            time.sleep(0.5)
            resposta_total_servidor = com1.getData(14)[0]
            print(f"ESSA EH A RESPOSTA TOTAL MESMO DO SERVIDOR:{resposta_total_servidor} ")
            resposta_servidor = resposta_total_servidor[8:10]
            print(f"ESSA EH A RESPOSTA DO SERVIDOR:{resposta_servidor} ")
            while resposta_servidor != certo:
                com1.sendData(np.asarray(pacote))
                resposta_servidor = com1.getData(14)[0]
            print(f"Pacote {contador} enviado!")
            contador += 1

        print("Todos os pacotes enviados")

        print("deu bom")

        time.sleep(0.5)
        
        com1.disable()
    
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
