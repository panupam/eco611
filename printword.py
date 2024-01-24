a=int(input("Enter Number: "))
b=''
d={0:'Zero',1:'One',2:'Two',3:"Three",4:"Four",5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
while a >0 :
    b=d[a%10]+" "+b
    a=a//10


print(b)