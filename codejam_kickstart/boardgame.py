# https://code.google.com/codejam/contest/4394486/dashboard#s=p2

import itertools

def divide(nine_values):
    ordered_sums = set()
    for first_three in itertools.combinations(nine_values,3):
        remaining_six = set(nine_values)- set(first_three)
        for second_three in itertools.combinations(remaining_six,3):
            last_three = set(remaining_six) - set(second_three)
            ordered_sums.add( tuple( (sum(first_three),sum(second_three),sum(last_three))))
    return ordered_sums

def compete(n,sums1,sums2):
    return sum([sum1 > sum2 for sum1,sum2 in zip(sums1,sums2)]) > n/2

def solve(n,Us,As):
    perc = 0
    bahus,balas = divide(Us), divide(As)
    for U in bahus:
        perc = max(perc,sum(compete(n, U, A) for A in balas) / len(bahus))
    return perc

def main():
    with open('in.in', 'r') as r:
        n = int(r.readline())
        N,Bahu,Bala = [], [],[]
        for i in range(n):
            N.append(int(r.readline()))
            Bahu.append( [int(i) for i in r.readline().split(" ")] )
            Bala.append( [int(i) for i in r.readline().split(" ")] )
    results = []
    for i, inputs in enumerate(zip(N,Bahu,Bala)):
        n, bahu, bala= inputs[0], inputs[1], inputs[2]
        results.append("Case #{}: {}\n".format(str(i + 1), solve(n,bahu,bala)))
        print(i+1)
    with open('out.out', 'w') as w:
        [w.write(r) for r in results]
    return
main()