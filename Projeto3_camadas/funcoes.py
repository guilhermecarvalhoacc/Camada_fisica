
import math

EOP = 2863311530
EOP_bytes = (EOP).to_bytes(4, byteorder='big')

zero_bytes = (0).to_bytes(2, byteorder='big')
zero_bytes_id = (0).to_bytes(4, byteorder='big')


print(EOP_bytes)

def cria_head(Id,Num_pacotes,tamanho_payload,tipo_msg):
    return Id + Num_pacotes + tamanho_payload + tipo_msg


def Datagrama(img):
    lista_datagrama = []

    Id = 1

    p = 114
    Num_pacotes = math.ceil(len(img)/p)
    Num_pacotes_bytes = (Num_pacotes).to_bytes(2, byteorder='big')

    tipo_msg = 10 #Client para server
    tipo_msg_bytes = (tipo_msg).to_bytes(2, byteorder='big')

    for i in range(0,len(img),p):
        Id_byte = (Id).to_bytes(4, byteorder='big')
        payload = img[i:i+p] 
        tamanho_payload = len(payload)
        print(f"esse eh o tamanho do payload:{tamanho_payload}")
        tamanho_payload_bytes = (tamanho_payload).to_bytes(2, byteorder='big')
        head = cria_head(Id_byte,Num_pacotes_bytes,tamanho_payload_bytes,tipo_msg_bytes)
        lista_datagrama.append(head + payload + EOP_bytes)
        Id += 1
    return lista_datagrama


def Handshake():
    tipo_msg_handshake = (2).to_bytes(2, byteorder='big')
    head = cria_head(zero_bytes_id,zero_bytes,zero_bytes,tipo_msg_handshake)
    return head + EOP_bytes



