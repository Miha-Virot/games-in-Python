import paramiko, numpy as np, os

host = '192.168.0.2'
user = 'login'
secret = 'password'
port = 60666

n=int(8)
stroka=''
sdvig=0

YP=np.zeros((n,n))
NP=np.zeros((n,n))

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
            else:
                print("~", end=" ")
        print(sep=" ")

    print("НЕ ТВОЯ ХАТА")
    print("# A B C D E F G H")
    for i in range(8):
        print(i+1, end=" ")
        for j in range(8):
            if NP[j][i] != 0:
                print("@", end=" ")
            elif NP[j][i] == 2:
                print("#", end=" ")
            else:
                print("~", end=" ")
        print(sep=" ")

pole()
stroka=input("Координаты однопалубной шлюшки - ")
x, y= stroka[0], int(stroka[1])
chm = np.zeros((int(2),n))
chm=[["A", "B", "C", "D", "E", "F", "G", "H"],[1, 2, 3, 4, 5, 6, 7, 8]]
for i in range(8):
    if chm[0][i]==x:
        x=i+1
YP[x-1][y-1]=1
pole()

while sdvig==0:
    stroka1, stroka2=input("Координаты двупалубной шляндры - ").split()
    x1, y1= stroka1[0], int(stroka1[1])
    x2, y2= stroka2[0], int(stroka2[1])
    chm = np.zeros((int(2),n))
    chm=[["A", "B", "C", "D", "E", "F", "G", "H"],[1, 2, 3, 4, 5, 6, 7, 8]]
    for i in range(8):
        if chm[0][i]==x1:
            x1=i+1
        elif chm[0][i]==x2:
            x2=i+1
    if (abs(x1-x2)!=1 and y1==y2) or (abs(y1-y2)!=1 and x1==x2):
        YP[x1-1][y1-1]=2
        YP[x2-1][y2-1]=2
        sdvig=1
        pole()