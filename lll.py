#!/usr/bin/python3

def LLL(n):
    B = [[0, 1]]
    k = 1
    while k < n:
        for i in range(k):
            if (B[i][0] * B[k][0] - B[i][1] * B[k][1]) % n == 0:
                B[i][0] = (B[i][0] + B[k][0]) % n
                B[i][1] = (B[i][1] + B[k][1]) % n
                k -= 1
                break
        else:
            k += 1
            B.append([k, 1])
    for i in range(k):
        if B[i][0] != 0:
            return gcd(B[i][0], n)
    return None

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(LLL(20))
