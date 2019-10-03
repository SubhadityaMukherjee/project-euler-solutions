# Even fibonacci numbers values < 4*10^6

x = [0,1]
s = 0
while(x[-1]<4*(10**6)):
    x.append(x[-1]+x[-2])
    if x[-1]%2==0:
        s+=x[-1]

print(s)
