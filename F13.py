from load import *
data_game=GetData("riwayat.csv")
def maxs(x,y) :
    if(x>y) :
        return x 
    else :
        return y
def print_data(data) :
    max=[0 for i in range(Length(data[0]))]

    for i in range(Length(data)) :
        if(i==0) :
            for j in range(Length(data[0])) :
                max[j]=Length(str(data[i][j]))
        else :
            for j in range(Length(data[0])) :
                max[j]=maxs(max[j],Length(data[i][j]))

    for i in range(Length(data)) :
        print(f"{(i+1)}. ",end='')
        for j in range(Length(data[0])) :
            if(j==0) :
                print(f"{data[i][j] : <{max[j]}} ",end='')
            else :
                print(f"| {data[i][j] : <{max[j]}} ",end='')
        print()

def riwayat(data,user) :

    list=[]

    for i in range(1,Length(data)) :

        if(data[i][3]==user) :
            list+=[[data[i][0],data[i][1],data[i][2],data[i][4]]]
    
    if(list==[]) :
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    else :
        
        print("Daftar game: ")
        print_data(list)

riwayat(data_game,1)

