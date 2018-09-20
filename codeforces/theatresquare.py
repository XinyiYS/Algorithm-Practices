# http://codeforces.com/problemset/problem/1/A
import math
def solve(n,m,a):
    return  int(math.ceil(n/a) * int(math.ceil(m/a)))

def main():
    inputs = [int(i) for i in input().split(" ")]
    n,m,a = inputs[0],inputs[1],inputs[2]
    print(solve(n,m,a))
    return

main()

