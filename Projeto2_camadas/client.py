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
serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)

#Interface grafica implementada para achar o arquivo img, codigo referente ao stackoverflow.
from tkinter.filedialog import askopenfilename
nome_arquivo = askopenfilename()
print(nome_arquivo)
imageR = nome_arquivo 
def main():
    try:
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com1 = enlace(serialName)
    
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        com1.enable()
        #Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        print('A comunicação foi aberta com sucesso!')
        
        #aqui você deverá gerar os dados a serem transmitidos. 
        #seus dados a serem transmitidos são uma lista de bytes a serem transmitidos. Gere esta lista com o 
        #nome de txBuffer. Esla sempre irá armazenar os dados a serem enviados.
  
        txBuffer = open(imageR, 'rb').read()
        num_bytes = (len(txBuffer)).to_bytes(4, byteorder='big')

        #print(len(txBuffer))

        com1.sendData(num_bytes)

        lista_pacotes = []
        p = 100
        inteiro = int(len(txBuffer)/p)
        resto = len(txBuffer)%p
        for i in range(0,len(txBuffer),p):
            lista_pacotes.append(txBuffer[i:i+100])
            time.sleep(0.2)
        
        tempo_inicio = time.time()
        contador = 1
        for pacote in lista_pacotes:
            com1.sendData(np.asarray(pacote))
            time.sleep(0.5)
            print(f"Pacote {contador} enviado!")
            contador += 1

        print("Todos os pacotes enviados")

        print("deu bom")

        time.sleep(0.5)
        
        rxbuffer, nrxbuffer = com1.getData(4) 

        #print(nrxbuffer)
        #print(rxbuffer)
        #print(f"recebi 4 bytes")

        rxbuffer_inteiro = int.from_bytes(rxbuffer, byteorder='big')

        #print(rxbuffer_inteiro)
        #print(len(txBuffer))
        
        if rxbuffer_inteiro == len(txBuffer):   
            print("Recebi mesmo tamanho que enviei!")
            # Encerra comunicação
            #if tamanho_voltou == txLen:
            print("-------------------------")
            tempo_final = time.time()
            tempo_gasto = tempo_final - tempo_inicio
            print(f"TEMPO GASTO PARA ENVIO E RECEBIMENTO: {tempo_gasto}")
            taxa_bytes = len(txBuffer)/(tempo_final-tempo_inicio)
            print(f"TAXA DE BYTES: {taxa_bytes}")
            
            print("Comunicação encerrada")
            print("-------------------------")
            com1.disable()
    
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
