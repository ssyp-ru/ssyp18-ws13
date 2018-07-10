myfile= open ('inp1.txt','r')
s=myfile.readline()
myfile.close()

l=len(s)
d=[]
i=2

#ищем все делители числа l
while i<=l//2:
    if l%i==0:
        d=d+[i]
    i+=1    
#строим матрицу и выбираем символы по строкам
for i in d:
    st=[]
    k=l//i
    j=0
    n=0
    while j<k:
        st=st+[s[n:n+i]]
        j=j+1
        n=n+i
    result=''
    for j in range(i):
        for m in range(k):
            result=result+st[m][j]
    print(result)
a=input('Введите Enter')    
