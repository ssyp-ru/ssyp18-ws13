#coding: utf-8
slovar = [] # список для словаря для удобства использования
q = 0
s = 0 # содаём переменные для циклов и слов
d = 0
az = " АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
word = ""
TrueWord = ""
mz = 0
nz = 0
res = '' 
spisk = []
w = open("input.txt", "r")
word = w.readline()
w.close
w = open("Slovar.txt","r") # открываем файл (словарь)

slovar = [str(i) for i in w.read().split('\n')] # считываем слова из файла и вносим их в список
w.close() # закрываем файл   
w = open("out.txt", "w")

for mz in range(len(slovar)-1):
    kword = slovar[mz]
    res = ''
    for nz in range(len(word)):
        kwordr = str(kword * 100)
        bu = word[nz]
        buk = kwordr[nz]
        bu = az.find(bu)
        buk = az.find(buk)
        n = bu - buk
        if n < 0:
            while n < 0:    
                n += len(az)
        res = res + az[n]
    w.write(res+'\n')
    print(res)
w.close
a=input('Enter')

