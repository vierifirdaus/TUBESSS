import os
from load import *
def IsGetDataValid(data) :

    if(data==[] or Length(data)==1) :
        return True
    else :
        return False


def IsStockNeg(x) :
    if(x<0) :
        return True 
    else :
        return False 

def ubah_stok(data) :
    len=Length(data)
    id=input("Masukkan ID game: ")
    
    ada=False

    for i in range(1,len) :
        if(data[i][0]==id) :
            ada=True
            index=i  
    
    if(ada) :
        jumlah=int(input("Masukkan jumlah: "))
        if(IsStockNeg(data[index][5]+jumlah)) :
            print(f"Stok game {data[index][1]} gagal dikurangi karena stok kurang. Stok sekarang: {data[index][5]}")
        else :
            if(jumlah>0):
                data[index][5]=data[index][5]+jumlah
                print(f"Stok game {data[index][1]} berhasil ditambah. Stok sekarang: {data[index][5]}")
            elif(jumlah<=0) :
                data[index][5]=data[index][5]+jumlah
                print(f"Stok game {data[index][1]} berhasil dikurang. Stok sekarang: {data[index][5]}")
            
    else :
        print("Tidak ada game dengasn ID tersebut!")
    return data