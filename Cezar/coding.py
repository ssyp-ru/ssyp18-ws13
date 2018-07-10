#incoding utf-8
import random
s=" АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
res=""
f = open('inp.txt','r')
orig=f.read()
f.close()
key=random.randint(1,len(orig))-1
for i in range (len (orig)):
    num=s.find (orig [i])
    if num+key>=len (s):
        res=res+s[num+key-len(s)-1]
    else:
        res=res+s[num+key]
f = open('out.txt','w')
f.write(res)
f.close()


