from list_data import *
def hitung_candi ():
    global candi
    count_candi = 0 
    i = 0
    while True :
        if candi[i] != "-" :
            count_candi += 1 
            i += 1
        else :
            return count_candi

def ayamberkokok ():
    global candi
    if hitung_candi(candi) < 100 :
        print("Kukuruyuk.. Kukuruyuk..")
        print("Jumlah Candi: ", hitung_candi(candi))
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
        exit()
    else :
        print("Kukuruyuk.. Kukuruyuk..")
        print("Jumlah Candi: ", hitung_candi(candi))
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        exit()