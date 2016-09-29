#-*- coding: utf-8 -*-


def sieve(n):
    before_sieve = [1] * (n+1)
    before_sieve[0] = 0
    before_sieve[1] = 0
    for i in range(2, (n+1)/2):
        j = 2
        while(j*i < n+1):
            before_sieve[j*i] = 0
            j += 1
    return before_sieve

def main(n):
    after_sieve = sieve(n)
    for i in range(n+1):
        if after_sieve[i] == 1:
            print '%d ' % i,

main(100)
