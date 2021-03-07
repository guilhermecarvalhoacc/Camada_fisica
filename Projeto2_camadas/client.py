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
imageR = 'img/boneco.png' 
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
        
        #txBuffer = imagem em bytes!
    

    
        #faça aqui uma conferência do tamanho do seu txBuffer, ou seja, quantos bytes serão enviados.
       
            
        #finalmente vamos transmitir os tados. Para isso usamos a funçao sendData que é um método da camada enlace.
        #faça um print para avisar que a transmissão vai começar.
        print('A transmição vai começar')
        #tente entender como o método send funciona!
        #Cuidado! Apenas trasmitimos arrays de bytes! Nao listas!
          

  
        txBuffer = open(imageR, 'rb').read()

        lista_pacotes = []
        p = 100
        inteiro = int(len(txBuffer)/p)
        resto = len(txBuffer)%p
        for i in range(0,len(txBuffer),p):
            lista_pacotes.append(txBuffer[i:i+100])
            print(i)
            print("coisei o pacote")
            print(f"O pacote {i} \n{txBuffer[i:i+100]}\n")
        print(len(lista_pacotes))

        
        
        # A camada enlace possui uma camada inferior, TX possui um método para conhecermos o status da transmissão
        # Tente entender como esse método funciona e o que ele retorna
        #Agora vamos iniciar a recepção dos dados. Se algo chegou ao RX, deve estar automaticamente guardado
        #Observe o que faz a rotina dentro do thread RX
        #print um aviso de que a recepção vai começar.
        print('A recepção vai começar')
        
        #Será que todos os bytes enviados estão realmente guardadas? Será que conseguimos verificar?
        #Veja o que faz a funcao do enlaceRX  getBufferLen
      
        #acesso aos bytes recebidos
        txLen = len(txBuffer)
        print(txLen)

        contador = 1
        for pacote in lista_pacotes:
            com1.sendData(np.asarray(pacote))
            time.sleep(0.5)
            print(f"Pacote {contador} enviado!")
            contador += 1

        print("Todos os pacotes enviados")
        
        #Resp = com1.getData(4)
        
    
        # Encerra comunicação
        tamanho_voltou = com1.tx.getBufferLen()
        print(tamanho_voltou)
        #if tamanho_voltou == txLen:
        print("-------------------------")
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
