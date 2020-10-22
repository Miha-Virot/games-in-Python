import paramiko, numpy as np, os

host = '192.168.0.2'
user = 'login'
secret = 'password'
port = 60666

n=int(8)
stroka=''

YP=np.zeros((n,n))
NP=np.zeros((n,n))

def pole():
    os.system("cls")
    print("ТВАЯ ХАТА")
    print("# A B C D E F G H")
    for i in range(8):
        print(i+1, end=" ")
        for j in range(8):
            if YP[j][i] != 0:
                print("@", end=" ")
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
            else:
                print("~", end=" ")
        print(sep=" ")

pole()
stroka=input("Координаты однопалубной шлюшки ")
x, y= stroka[0], int(stroka[1])

chm = np.zeros((int(2),n))
chm=[["A", "B", "C", "D", "E", "F", "G", "H"],[1, 2, 3, 4, 5, 6, 7, 8]]
for i in range(8):
    if chm[0][i]==x:
        x=i+1

YP[x-1][y-1]=1
pole()
