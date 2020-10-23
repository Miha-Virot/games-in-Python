import paramiko, numpy as np, os

host = '192.168.0.2'
user = 'login'
secret = 'password'
port = 60666

n=int(8)
stroka=''
n=8

YP=np.zeros((n,n))
NP=np.zeros((n,n))
chm = np.zeros((int(2),n))
chm=[["A", "B", "C", "D", "E", "F", "G", "H"],[1, 2, 3, 4, 5, 6, 7, 8]]


def pole():
    os.system("cls")
    print("ТВАЯ ХАТА")
    print("# A B C D E F G H")
    for i in range(8):
        print(i+1, end=" ")
        for j in range(8):
            if YP[j][i] == 1:
                print("@", end=" ")
            elif YP[j][i] == 2:
                print("#", end=" ")
            elif YP[j][i]==3:
                print("%", end=" ")
            elif YP[j][i] == 4:
                print("$", end=" ")                
            else:
                print("~", end=" ")
        print(sep=" ")

    print("НЕ ТВОЯ ХАТА")
    print("# A B C D E F G H")
    for i in range(8):
        print(i+1, end=" ")
        for j in range(8):
            if NP[j][i] == 1:
                print("@", end=" ")
            elif NP[j][i] == 2:
                print("#", end=" ")
            elif NP[j][i]==3:
                print("%", end=" ")
            elif NP[j][i] == 4:
                print("$", end=" ")                
            else:
                print("~", end=" ")
        print(sep=" ")

p1=0
p2=0
p3=0
p4=0
e = 0

def shlup():
    global e, p1, p2, p3, p4
    n1=int(input("Сколько палуб у шлюхи? "))
    if p1 == 4 and p2 == 3 and p3 == 2 and p4 == 1: 
        return 1
    if n1 == 1 and p1 < 4 or n1 == 2 and p2 < 3 or n1 == 3 and p3 < 2 or n1 == 4 and p4 < 1:
        if n1==1:
            stroka=input("Координаты однопалубной шлюшки - ")
            x, y= stroka[0], int(stroka[1])
            for i in range(8):
                if chm[0][i]==x:
                    x=i+1
            YP[x-1][y-1]=1
            p1+=1
            pole()
            return 0
            
        if n1>1:
            if n1==2:
                stroka1, stroka2=input("Координаты двупалубной шляндры - ").split()
            elif n1==3:
                stroka1, stroka2=input("Координаты трёхпалубной шляпы - ").split()
            elif n1==4:
                stroka1, stroka2=input("Координаты четырёхпалубной швабры - ").split()

            x1, y1= stroka1[0], int(stroka1[1])
            x2, y2= stroka2[0], int(stroka2[1])
            for i in range(8):
                if chm[0][i]==x1:
                    x1=i+1
                if chm[0][i]==x2:
                    x2=i+1
            if n1==2:
                if (x1==x2 or y1==y2) and abs(x1-x2)==1 or abs(y1-y2)==1:
                    p2+=1
                    YP[x1-1][y1-1]=2
                    YP[x2-1][y2-1]=2
            elif n1==3:
                if (x1==x2 or y1==y2) and abs(x1-x2)==2 or abs(y1-y2)==2:
                    p3+=1
                    if x1-x2 == 0:
                        if y1 > y2:
                            YP[x1-1][y1-1]=3
                            YP[x1-1][y1-2]=3
                            YP[x2-1][y2-1]=3
                        else:
                            YP[x1-1][y1-1]=3
                            YP[x1-1][y2-2]=3
                            YP[x2-1][y2-1]=3
                    else:
                        if x1 > x2:
                            YP[x1-1][y1-1]=3
                            YP[x1-2][y1-1]=3
                            YP[x2-1][y2-1]=3
                        else:
                            YP[x1-1][y1-1]=3
                            YP[x2-2][y2-1]=3
                            YP[x2-1][y2-1]=3
                else:
                    print("Поздравляю, ты долбоёб. Введи нормально")
                    return 0
            elif n1==4:
                if (x1==x2 or y1==y2) and abs(x1-x2)==3 or abs(y1-y2)==3:
                    p4+=1
                    if x1-x2 == 0:
                        if y1 > y2:
                            YP[x1-1][y1-1]=4
                            YP[x1-1][y1-2]=4
                            YP[x1-1][y1-3]=4
                            YP[x2-1][y2-1]=4
                        else:
                            YP[x1-1][y1-1]=4
                            YP[x1-1][y2-2]=4
                            YP[x1-1][y2-3]=4
                            YP[x2-1][y2-1]=4
                    else:
                        if x1 > x2:
                            YP[x1-1][y1-1]=4
                            YP[x1-2][y1-1]=4
                            YP[x1-3][y1-1]=4
                            YP[x2-1][y2-1]=4
                        else:
                            YP[x1-1][y1-1]=4
                            YP[x2-2][y2-1]=4
                            YP[x2-3][y2-1]=4
                            YP[x2-1][y2-1]=4
                else:
                    print("Поздравляю, ты долбоёб. Введи нормально")
                    return 0
            pole()
            return 0
    else:
        print('Многовато желаешь, милок')
        return 0
pole()

while shlup()==0:
    n=n

