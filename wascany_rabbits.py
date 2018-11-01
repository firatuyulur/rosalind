def fiboRabs(n,k):
    rabz=[1,1]
    #rabz[n] = rabz[n-1] + k.rabz[n-2]
    while len(rabz) < n:
        for i in range(2,n):
            rabz.append(rabz[i-1]+rabz[-2]*k)
    return rabz


def fib(n, k):
    if n < 2:
        return n
    return k*fib(n-2, k) + fib(n-1, k)
