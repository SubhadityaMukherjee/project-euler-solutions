# (1^2+2^2+...+100^2) - (1+2+..100)^2
import numpy as np
n = 100

s2 = np.sum([x for x in range(1, 101)])
s2 = s2**2

s3 = np.sum([x**2 for x in range(1, 101)])

print(s3-s2)

# 25164150
