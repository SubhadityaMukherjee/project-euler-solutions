

# What is the 10 001st prime number?

def candidate_range(n):
    cur = 5
    incr = 2
    while cur < n+1:
        yield cur
        cur += incr
        incr ^= 6

def sieve(end):
    prime_list = [2, 3]
    sieve_list = [True] * (end+1)
    for each_number in candidate_range(end):
        if sieve_list[each_number]:
            prime_list.append(each_number)
            for multiple in range(each_number*each_number, end+1, each_number):
                sieve_list[multiple] = False
    return prime_list

z = []
n = 96000
while len(z)<=10001:
    z = sieve(n)
    if n%1000==0:
        print(n, len(z))
    n+=1
print(z[-2])


# 104743
