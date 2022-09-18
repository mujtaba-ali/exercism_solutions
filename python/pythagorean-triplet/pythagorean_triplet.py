def triplets_with_sum(number):
    c, m = 0, 2
    triplets = []
    while c < number:
        for n in range(1, m):
            a = m*m-n*n
            b = 2*m*n
            c = m*m+n*n
            if c > number:
                break
            if a+b+c == number:
                triplets.append(sorted([a,b,c]))
        m = m+1
    return triplets
