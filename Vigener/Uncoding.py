s=" АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
res=""
kod=input(" введите кодовое слово ")

myfile= open ('code.txt','r')
st=myfile.readline()
myfile.close()

orig=[ch for ch in st]
j=0
for i in range(len(orig)):
    n=s.find (orig [i])
    a=s.find (kod[j])
    if n-a>len (s):
        m=n-a-len(s)
    else:
        m=n-a
    res=res+s[m]
    if j==len (kod)-1:
        j=0
    else:
        j+=1
print (res)

ad=input(" нажмите enter чтобы выйти ")
