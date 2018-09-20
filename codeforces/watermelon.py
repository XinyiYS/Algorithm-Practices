# http://codeforces.com/problemset/problem/4/A

def main():
    n = int(input())
    if n < 4:
        print("NO")
    elif (n-2) %2 ==0:
        print("YES")
    else:
        print("NO")

    return

main()