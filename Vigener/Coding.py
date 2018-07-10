#coding utf-8
s=" АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
res=""

kod=input(" введите кодовое слово ")
orig=input(" введите текст для шифровки ")
j=0
for i in range (len(orig)):
    n=s.find (orig [i])
    a=s.find (kod[j])
    if n+a>=len (s):
        m=n+a-len(s)
    else:
        m=n+a
    res=res+s[m]
    if j==len (kod)-1:
        j=0
    else:
        j+=1
myfile=open("code4.txt",'w')      
myfile.write(res)
myfile.close()
ad=input(" нажмите enter чтобы выйти ")
