# a^2 + b^2 =c^2
# and a+b+c = 1000

import math


a = [x for x in range(1,1001)]
b = [x for x in range(1,1001)]
c = [x for x in range(1,1001)]

trip = []

for i in range(190, len(a)):
    for j in range(i, len(b)):
        for k in range(1, len(c)):
            if(a[i]+b[j]+c[k]==1000):
                if (a[i]**2 + b[j]**2 ==c[k]**2):
                    trip.append((a[i],b[j],c[k]))
                    print('[INFO]->{}, {}'.format((a[i],b[j],c[k]), (a[i]*b[j]*c[k])))
                    break
    print(i)

print(trip)
