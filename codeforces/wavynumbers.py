def iswavy(number):
    str_number = str(number)
    if len(str_number) <=2:
        return True
    diff = int(str_number[0]) - int(str_number[1])
    for i,c in enumerate(str_number[1 : len(str_number)-1]):
        diff_ = (int(c) - int(str_number[i + 2]))
        if (diff_ * diff) >= 0:
            return False
        diff = diff_

    return True


def solve(n,k):
    number = n
    count = 0
    if n%100 ==0:
        return '-1'
    while(number < 1e14):
        count += iswavy(number)
        if count == k:
            return number
        number += n

    return '-1'


def main():
    inputs = input().split(' ')
    n,k = int(inputs[0]),int(inputs[1])
    print(solve(n,k))

main()