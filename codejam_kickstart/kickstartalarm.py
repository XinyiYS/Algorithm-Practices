# https://code.google.com/codejam/contest/4384486/dashboard#s=p2&a=0
import os
def compute_A(x1,y1,C,D,E1,E2,F,N):
    X,Y = x1, y1
    A = [(x1+y1)%F]

    for i in range(2,N+1):
        Xnext = (C %F * X%F + D%F* Y%F + E1%F) %F
        Ynext = (D %F * X%F + C%F* Y%F + E2%F) %F
        X,Y = Xnext,Ynext
        A.append((Xnext %F +Ynext%F)%F)
    return A


def solve(K,A,N):
    power = 0

    for k in range(1,K+1):

        #length go from 1 to N
        for i in range(1,N+1):
            #starting index go from 0 to K-i+1 (not inclusive of K-i+1)
            for j in range(0, N-i+1):

                # formulate the subarrays
                subarray = A[j:j+i]
                power += sum([  element*((index+1)**k) for index, element in enumerate(subarray)])% (1e9+7)
    return int(power % (1e9+7))


def main():
    with open('in.in', 'r') as r:
        n = int(r.readline())
        firstlines = []
        for i in range(n):
            firstlines.append([int(i) for i in r.readline().split(" ")])
    results = []
    for i, firstline in enumerate(firstlines):
        N, K, x1, y1, C, D, E1, E2, F = firstline[0], firstline[1], firstline[2] ,firstline[3], firstline[4]\
            , firstline[5], firstline[6] ,firstline[7], firstline[8]

        A = compute_A(x1,y1,C,D,E1,E2,F,N)
        results.append("Case #{}: {}\n".format(str(i + 1), solve(K,A,N)))
    with open('out.out', 'w') as w:
        [w.write(r) for r in results]
        # print(os.system("diff out1.out out.out"))
    return
main()