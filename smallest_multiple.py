# Find smallest no which is divided by all nos from 1 to 20

p = 0
z = 200000000
def chk(x):
    for i in range(1,21):
        if x%i !=0:
            return False
            break
    return True

while p==0:
    print(z)
    ch = chk(z)
    if ch == True:
        p = z
        print("hi")
        break

    z+=10

# 232792560
