# coding utf-8
fail=open("inp3.txt","r")
f = fail.read()
fail.close()
result = []
i = 0
a = 0
b = 0
c = 5
d = 0
sifr=0
"""
Ввод шифра и создание нужных переменных
"""

for i in range(len(f)):
    for j in range(len(f[i])):
        if ord(f[i][j])<=ord('я') and ord(f[i][j])>=ord('а'):
            result = result+["0"]
        elif ord(f[i][j])<=ord('z') and ord(f[i][j])>=ord('a'):
            result = result+["0"]
        elif ord(f[i][j])<=ord('Я') and ord(f[i][j])>=ord('А'):
            result = result+["1"]
        elif ord(f[i][j])<=ord('Z') and ord(f[i][j])>=ord('A'):
            result = result+["1"]
    j+=1
i+=1
"""
Цикл, что распознаёт строчные и заглавные буквы в словах и даёт
заглавным буквам значение 1, а строчным - 0
"""

f=[]
for a in range(0,len(result)):
        sifr = sifr + int(result[a])*(2**(4-a%5))
        if a%5==4:
            f=f+[sifr]
            sifr=0        
a = 0
result = ''
for i in range(len(f)):
    result = result + chr(ord('а') + (f[i]))
    
print(result)
p=input('Введи Enter')