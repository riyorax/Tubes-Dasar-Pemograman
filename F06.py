import random
import tools
from list_data import *

def bangun():
    if role == "jin_pembangun":
        pasir = random.randint(1,5)
        batu = random.randint(1,5)
        air = random.randint(1,5)
        if int(bahan_bangunan[1][2])- pasir < 0 or int(bahan_bangunan[2][2])- batu < 0 or int(bahan_bangunan[3][2])- air < 0:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
        else:
            a = int(bahan_bangunan[1][2])
            a -= pasir
            b = int(bahan_bangunan[2][2])
            b -= batu
            c = int(bahan_bangunan[3][2])
            c -= air
            bahan_bangunan[1][2] = str(a)
            bahan_bangunan[2][2] = str(b)
            bahan_bangunan[3][2] = str(c)
            id_candi = tools.id_candi(candi)
            flag = False
            for i in range(101):
                if candi[i] == "-":
                    flag = True
            if flag:
                tools.write_array_candi(candi,id_candi,username,pasir,batu,air)
    else:
        print("Maaf anda tidak memiliki akses untuk fungsi tersebut")