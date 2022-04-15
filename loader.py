def Length(x) :
    if(type(x)==type(1)) :
        temp=x
        length=0

        while(temp>0) :
            length+=1
            temp=temp//10
    else :
        length=0
        for i in x :
            length+=1
    return length


def cek_int(string) :
    cek=True

    for i in string :
        if(i<'0' or i>'9') :
            cek=False 

    return cek
    
def convert_string(list) :
    list_n=[]
    len=Length(list)
    index=0
    temp=0
    for i in range(1,len) :
        
        if(i==len-1) :
            list_n+=[list[temp:i]]

            if(list[-1:]!="\n"):
                list_n[index]=list_n[index]+list[len-1]

            if(cek_int(list_n[index])) :
                list_n[index]=int(list_n[index])
                        
        else:
            if(list[i]==';') :
                index+=1
                string=list[temp:i]
                if(cek_int(string)) :
                    list_n=list_n+[int(string)]
                else :
                    list_n=list_n+[string]
                temp=i+1
    return list_n
def GetData(file) :
    f=open(file).readlines()
    data=[]
    for i in f :
        data=data+[convert_string(i)]
    return data
