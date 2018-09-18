# https://code.google.com/codejam/contest/10284486/dashboard#s=p0&a=2

def is_legal(number):
    # legal only if not divisible and does not contain a '9' digit
    number_str = str(number)
    if '9' in number_str:
        return False
    if sum(int(i) for i in number_str) %9 == 0:
        return False
    return True


def solve(F,L):
    return sum([is_legal(i) for i in range(F,L+1)])

def count_legal(A):
    begin = 0


    return


def solve_large(F,L):
    return count_legal(L) - count_legal(F) +1

def main():
    with open('in.in', 'r') as r:
        n = int(r.readline())
        Fs,Ls = [],[]
        for i in range(n):
            inputs = r.readline().split(" ")
            Fs.append(int(inputs[0]))
            Ls.append(int(inputs[1]))
    results = []
    for i, inputs in enumerate(zip(Fs,Ls)):
        F,L = inputs[0],inputs[1]

        results.append("Case #{}: {}\n".format(str(i + 1), solve(F,L)))
        print("Case #{} complete".format(str(i + 1)))
    with open('out.out', 'w') as w:
        [w.write(r) for r in results]
        # print(os.system("diff out1.out out.out"))
    return
main()