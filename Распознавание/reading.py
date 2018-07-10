#coding: utf-8

key=''#распознанная строка
myfile = open('inp.txt','r') #файл с шифрами
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
