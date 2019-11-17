num = int(input ("Masukan nilai n:"))

from random import random
a = random()

jumlah = num +1
start=0
stop=jumlah
step=1
for i in range (start,stop,step):
    print("Data ke :", i , "Lebih dari",  (a))
