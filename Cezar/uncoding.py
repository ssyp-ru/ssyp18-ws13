#coding utf-8
S = " АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

f=open('out.txt','r')
shifr = f.readline()
f.close()
f=open('all_out.txt','w')
for code in range(0,34):
    i = 0
    res=''
    while i<len(shifr):
        n=S.find(shifr[i])+code-1
        if n>32:
            n=n-35
        res=res+S[n]
        i+=1
    
    f.write(res+'\n')
    print(res)
f.close()
a=input('Пауза')
key=''#распознанная строка
myfile = open('all_out.txt','r') #файл с шифрами
for code in myfile.read().split('\n'):
    words = [code for code in code.split()]#список слов из очередного закодированного сообщения
    count=0
    myf = open('dict.txt','r') #файл словаря
    for word_dict in myf.read().split('\n'):
        for word in words:
            if word==word_dict:
                count+=1
    if count>0:
        key=code

myfile.close()
print(key)
a=input('Нажми Enter')

