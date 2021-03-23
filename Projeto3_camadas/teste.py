import numpy as np

head = [bytes([0]) for i in range(10)]
head[4] = bytes([255])


#if head[4] == 255:

def cria_datagrama(is_handshake = False):
    head = [bytes([0]) for i in range(10)]
    EOP = [bytes([170]) for i in range(4)]
    payload = []
    if is_handshake:
        head[4] = bytes([2])
    datagrama = head + payload + EOP
    return np.asarray(datagrama)

print(cria_datagrama(is_handshake=True))



