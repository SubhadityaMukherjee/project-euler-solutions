#largest prime factor of 600851475143?

import math
for i in range(int(math.sqrt(600851475143)),1,-1):
    # print(i)
    if 600851475143 % i ==0:
        flag = False
        for y in range(int(math.sqrt(i)),1,-1):
            if(i % y ==0):
               flag = True
        if(flag!=True):
            print(i)
            break
