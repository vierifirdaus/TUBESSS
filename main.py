from load import *
# from register import *
from buy_game import *
from ubah_stok import *

data_user=GetData("user.csv")
data_kepemilikan=GetData("kepemilikan.csv")
data_riwayat=GetData("riwayat.csv")
data_game=GetData("game.csv")
user=1
cek=True

while(cek) :
    perintah=input()

    if(perintah=="ubah_stok") :
        # ubah_stok(data_game) 
        data_game=ubah_stok(data_game)
        # print(data_game)
    elif(perintah=="buy_game"):
        
        (data_user,data_kepemilikan,data_game,data_riwayat)=buy(data_user,data_kepemilikan,data_riwayat,data_game,user)
        print(data_user)
        print(data_kepemilikan)
        print(data_game)
        print(data_riwayat)
    else :
        cek=False

