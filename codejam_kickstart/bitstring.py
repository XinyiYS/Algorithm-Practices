# https://code.google.com/codejam/contest/10284486/dashboard#s=p1&a=1

def solve_small(N,K,P,ABs):
    if N==K:
        return '1'*N
    arr = [0] *N
    for AB in ABs:
        arr[AB[0]-1] = 1
    while(P > N-K):
        for j in range(N-1,-1,-1):
            if arr[j] == 0:
                arr[j]=1
                break
        P/=N-K
        K+=1
        if N == K:
            return '1' * N
    for j in range(N-1, -1, -1):
        if arr[j] == 0:
            arr[j] = 1
            break

    return "".join([str(i) for i in arr])


def solve_large(F,L):
    return

def main():
    with open('in.in', 'r') as r:
        n = int(r.readline())
        Ns,Ks,Ps = [],[],[]
        AB_inputs = []
        for i in range(n):
            firstline = [ int(i) for i in r.readline().split(" ")]
            Ns.append(firstline[0])
            Ks.append(firstline[1])
            Ps.append(firstline[2])
            AB_input = []
            for k in range(Ks[-1]):
                AB_input.append( [int(i) for i in r.readline().split(" ")] )
            AB_inputs.append(AB_input)
    results = []
    for i, inputs in enumerate(zip(Ns,Ks,Ps,AB_inputs)):
        N,K,P,ABs = inputs[0],inputs[1],inputs[2],inputs[3]

        results.append("Case #{}: {}\n".format(str(i + 1), solve_small(N,K,P,ABs )))
        print("Case #{} complete".format(str(i + 1)))
    with open('out.out', 'w') as w:
        [w.write(r) for r in results]
        # print(os.system("diff out1.out out.out"))
    return
main()