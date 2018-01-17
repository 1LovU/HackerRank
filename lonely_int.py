# https://www.hackerrank.com/challenges/lonely-integer-fill-the-key-line/problem


def lonely_integer(a):
    answer = 0
    for x in a:
        answer^=x
    return answer

if __name__ == '__main__':
    a = int(raw_input())
    b = map(int, raw_input().strip().split(" "))
    print lonely_integer(b)
