import random
path='' #output file path here
d={}
with open(path, mode='r') as ff:
    l=[]
    n=0
    for s in ff:
        l.append(s.rstrip('\n'))
    for i in range(int(len(l)/2)):
        d[l[n]]=l[n+1]
        n=n+2
lm=[]
c=1
for i in range(int(len(l)/2)):
    lm.append(l[c])
    c=c+2
print("register:1,test:2")
x=int(input())
while x == 1 or x == 2:
    if x==1:
        print("new word:")
        a=input()
        print("the meaning:")
        b=input()
        d[a]=b
        
        print("register:1,test:2,quit:3")
        x=int(input())
    elif x==2:
        print("How many quastions do you want?")
        h=input()
        for i in range(int(h)):
            t=random.choice(list(d))
            print(t,"What's the meaning?")
            k=[]
            k.append(d[t])
            for i in range(2):
                while True:
                    kk=random.choice(list(d))
                    if d[kk] != k[i] and d[kk] != d[t]:
                        k.append(d[kk])
                        break                
            random.shuffle(k)
            s='1.'+k[0]+'\n'+'2.'+k[1]+'\n'+'3.'+k[2]
            print(s)
            q=input()
            if q=='':
                print("The answer:",d[t])
            elif k[int(q)-1]==d[t]:
                print("That's right!")
            else:
                print("That's wrong.")
                print("The answer:",d[t])
        print("register:1,test:2,quit:3")
        x=int(input())
    else:
        print("finish")
        break
with open(path, mode='w') as f:
    for i in d:
        f.write(i)
        f.write("\n")
        f.write(d[i])
        f.write("\n")
f.close()
