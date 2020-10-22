import os, random, time, numpy as np, keyboard
m = int(input("HEIGHT= "))
n = int(input("WIDTH= "))

matrix = np.zeros((m,n))

x=random.randint(0, n-1) #горизонталь
y=random.randint(0, m-1) #вертикаль
x1=random.randint(0, n-1)   #горизонталь еды
y1=random.randint(0, m-1)   #вертикаль еды

while x==x1 and y==y1:
    x1=random.randint(0, n-1)
    y1=random.randint(0, m-1)


boel = 1 #стопор
vektor=0 #направление движения
up='w'
down='s'
left='a'
right='d'
esc='p'

size = 1 #размер змеи


while boel == 1:
    time.sleep(0.1)

    os.system('cls')

    if keyboard.is_pressed(esc):
        boel=2

    if x1 < x:
        vektor=1 #вверх
    elif x1 > x:
        vektor=2 #вниз
    elif y1 < y:                    #У НЕЁ ЕСТЬ МОЗГИ
        vektor=3 #влево
    elif y1 > y:
        vektor=4 #вправо

    if vektor==1:
        x -=1
        if x<0:
            x=m-1
    elif vektor==2:
        x +=1
        if x>m-1:
            x=0
    elif vektor==3:
        y -=1
        if y<0:
            y=n-1
    elif vektor==4:
        y +=1
        if y>n-1:
            y=0

    for i in range (0, m):
        for j in range (0,n):

            if matrix[i][j]>0:
                matrix[i][j]+=1
            if matrix[i][j]>size:
                matrix[i][j]=0
            
            if x==x1 and y==y1:
                size+=1
                x1=random.randint(0, n-1)   #горизонталь еды, обновление
                y1=random.randint(0, m-1)
                while matrix[x1][y1]!=0:
                    x1=random.randint(0, n-1)
                    y1=random.randint(0, m-1)

            matrix[x][y] = 1
            matrix[x1][y1] = -1
            if matrix[i][j] == 1:
                print("@", end=" ") #1
            elif matrix[i][j] == 0:
                print("*", end=" ") #0
            elif matrix[i][j]>1:
                print("0", end=" ")
            elif matrix[i][j]==-1:
                print("&", end=" ")

            if j==n-1:
                print(sep=" ")


     
print("GAME OVER", x, y, size - 1)



"""    if keyboard.is_pressed(up):
        vektor=1 #вверх
    elif keyboard.is_pressed(down):
        vektor=2 #вниз                  
    elif keyboard.is_pressed(left):
        vektor=3 #влево
    elif keyboard.is_pressed(right):
        vektor=4 #вправо"""