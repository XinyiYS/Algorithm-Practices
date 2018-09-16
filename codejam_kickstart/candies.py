# https://code.google.com/codejam/contest/6364486/dashboard#s=p0
import sys
import queue

def solve(S,N,D,O):
    i, j, total, odd, result = 0, 0, 0, 0, -sys.maxsize
    while i < N and j < N:
        if total+S[j] <= D and odd + S[j]%2 <= O:
            total += S[j]
            odd += S[j]%2
            result = max(total, result)
            j += 1
        else:
            odd -= S[i]%2
            total -= S[i]
            i += 1
    return result if result > -sys.maxsize else 'IMPOSSIBLE'

def solve_q(S,N,D,O):
    q = queue.Queue()
    odd,curr_result,final_result = 0, 0, -sys.maxsize

    for candy in S:

        # NEED TO DEQUEUE THE BEGINNING OF THE FIRST, IF IT IS AN EMPTY ONE AND THERE IS MORE AFTER

        if (candy % 2 + odd <= O and candy + curr_result <= D):
            q.put(candy)
            odd += candy % 2
            curr_result += candy
            final_result = max(final_result, curr_result)

        else:
            while not q.empty() and (not candy % 2 + odd <= O and candy + curr_result <= D ):
                out_candy = q.get()
                odd -= out_candy%2
                curr_result -= out_candy


            if (candy % 2 + odd <= O and candy + curr_result <= D):
                q.put(candy)
                odd += candy % 2
                curr_result += candy
                final_result = max(final_result, curr_result)

    return final_result if final_result > -sys.maxsize else 'IMPOSSIBLE'

    
def compute_S(X1,X2,N,A,B,C,L,M):
    X = [0]* N
    X[0],X[1] = X1,X2
    S = [0]* N
    S[0],S[1] = X1+L, X2+L
    for i in range(2,N):
        X[i] = ((A % M * X[i - 1] % M)%M + (B % M * X[i-2]%M)%M + C%M)%M
        S[i] = X[i]+L
    return S

def main():
    with open('in.in', 'r') as r:
        n = int(r.readline())
        firstlines,secondlines = [],[]
        for i in range(n):
            firstlines.append( [int(i) for i in r.readline().split(" ")] )
            secondlines.append( [int(i) for i in r.readline().split(" ")] )
    results = []
    for i, inputs in enumerate(zip(firstlines,secondlines)):
        firstline, secondline = inputs[0],inputs[1]
        N,O,D = firstline[0],firstline[1],firstline[2]
        X1,X2,A,B,C,M,L = secondline[0],secondline[1],secondline[2],secondline[3],secondline[4],secondline[5],secondline[6]
        S = compute_S( X1=X1,X2=X2,A=A,B=B,C=C,M=M,L=L,N=N )
        results.append("Case #{}: {}\n".format(str(i + 1), solve_q(S,N,D,O)))
    with open('out.out', 'w') as w:
        [w.write(r) for r in results]
    return

main()