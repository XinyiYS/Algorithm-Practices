# Street Checker https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edb/00000000001707b9

# Given a number X, find the number of even divisors and number of odd divisors efficiently in O(log(X))

#
Preprocessing:
	1. find all prime numbers smaller than sqrt(R) in O(NlogN), since to factorize X we only need to consider up to sqrt(X)

Computing: for each X in [L,R]
	2. find prime factorizations of number X in O(log X)
	3. find the number of even divisors and odd divisors from the prime factorization in O(1)


N = sqrt(R), where 1 <= R <= 1e9
N = 3e4, roughly
NlgN = 4e5, roughly, sufficiently efficient for the case
O(NlogN) + O((R-L)logX)
nlogn is too slow

import math 
n = math.sqrt(1e9)
print(n, math.log(n,2))
print( n* math.log(n,2)  )
exit()


def even_divisibility(high,n):
	return sum([n%(2*i)==0 for i in range(1,  min(int(high)//2,n))])

def odd_divisibility(high,n):
	return sum([n%(2*i-1)==0 for i in range(1,min(int(high)//2,n))])

high = 1e5
for n in range(0,int(1e5),1000):
	print('testing', n,end=' ')
	even =even_divisibility(high,n)
	odd = odd_divisibility(high,n)
	print(even, odd, abs(even - odd))