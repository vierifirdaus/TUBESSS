from load import *
# from main import *

def GetDataGame(data_game,games) :
    len_game=Length(data_game)
    game=[]
    cek=False
    for i in range(1,len_game) :
        if(data_game[i][0]==games) :
            cek=True
            game=data_game[i]
    if(cek) :
        return game
    else :
        return []

def GetDataUser(data_user,user) :
    len_user=Length(data_user)
    saldo=0

    for i in range(1,len_user) :
        if(data_user[i][0]==user) :
            saldo=data_user[i][5]

    return saldo

def GetDataKepemilikan(data_kepemilikan,user) :
    len_kepemilikan=Length(data_kepemilikan)
    game=[]

    for i in range(1,len_kepemilikan-1) :
        if(data_kepemilikan[i][1]==user) :
            game=game+[data_kepemilikan[i][0]]

    return game

def buy(data_user,data_kepemilikan,data_riwayat,data_game,user) :
    game=input("Masukkan ID Game: ")
    ada=False
    data=GetDataGame(data_game,game)
    saldo=GetDataUser(data_user,user)
    list_game=GetDataKepemilikan(data_kepemilikan,user)
    if(data==[]) :
        print("Game tersebut tidak ada")
    else :

        stok=data[5]
        harga=data[4]
        for i in list_game :
            if(i==game) :
                
                ada=True
        if(stok<1) :
            print("Stok game Tersebut sedang habis")
        else :
            if(saldo<harga) :
                print("Saldo anda tidak cukup untuk membeli Game tersebut!")
            else :
                if(ada) :
                    print("Anda sudah memiliki Game tersebut!")
                else :
                    print(f"Game {game} berhasil dibeli!")

                    data_user=save_user(data_user,user,harga)
                    data_kepemilikan=save_kepemilikan(data_kepemilikan,user,game)
                    data_game=save_game(data_game,game)
                    data_riwayat=save_riwayat(data_riwayat,game,data[1],data[2],harga,user,2022)

        return (data_user,data_kepemilikan,data_riwayat,data_game)

def save_user(data_user,user,harga) :
    for i in range(1,Length(data_user)) :
        if(data_user[i][0]==user) :
            data_user[i][5]-=harga
    return data_user

def save_kepemilikan(data_kepemilikan,user,game) :
    data=data_kepemilikan
    data=data+[[game,user]]
    return data

def save_game(data_game,game) :
    for i in range(1,Length(data_game)) :
        if(data_game[i][0]==game) :
            data_game[i][5]-=1
    return data_game

def save_riwayat(data_riwayat,game_id,nama,kategori,harga,user_id,tahun_beli) :
    data_riwayat+=[[game_id,nama,kategori,harga,user_id,tahun_beli]]
    return data_riwayat

