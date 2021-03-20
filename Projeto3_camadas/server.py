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
        
        recebe_handshake = com2.getData(14)[0]
        print("recebeu handshake")
        print(f"esse eh o hankdshake: {recebe_handshake}")
        tipo_msg_handshake = recebe_handshake[8:10]
        print("recebeu tipo de msg")
        print(f"esse aqui eh o tipo de msg: {tipo_msg_handshake}")

        if tipo_msg_handshake == (2).to_bytes(2, byteorder='big'):
            print("Handshake recebido com sucesso! Comunicação operacional")


        comando = True
        lista_payload = bytearray()
        while comando:
            time.sleep(0.5)
            recebe_head = com2.getData(10)[0]
            print(recebe_head)
            recebe_id = recebe_head[0:4]
            print(f"esse eh o id:{recebe_id}")
            recebe_num_pacotes = recebe_head[4:6]
            print(f"esse eh o num de pacotes: {recebe_num_pacotes}")
            recebe_tamanho_payload = recebe_head[6:8]
            recebe_tipo_msg = recebe_head[8:10]

            tamanho_payload_int = int.from_bytes(recebe_tamanho_payload, byteorder='big')
            print(f"esse eh o tamanho do payload em inteiro:{tamanho_payload_int}")
            recebe_payload = com2.getData(tamanho_payload_int)[0]
            recebe_EOP = com2.getData(4)[0]
            print(f"esse eh o EOP: {recebe_EOP}")
            lista_payload.extend(recebe_payload)
            recebe_id_int  = int.from_bytes(recebe_id, byteorder='big')
            recebe_num_pacotes_int  = int.from_bytes(recebe_num_pacotes, byteorder='big')
            if recebe_id_int == recebe_num_pacotes_int:
                comando = False
            
        print("saiu do loop")
        print(lista_payload)


        print('Salvando dados dos arquivos: ')
        f = open(imageW, 'wb')
        f.write(lista_payload)
            
    
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
