def sum_of_multiples(limit, multiples):
    return sum(set([j for i in multiples if i!=0 for j in range(1, limit) if j%i==0]))
                
