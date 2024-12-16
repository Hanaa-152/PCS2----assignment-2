def genotype_probability(k, N):
    p = 0.25  
    n = 2 ** k  

    probability = 0
    for i in range(N, n + 1):
        comb = 1
        for j in range(i):
            comb *= (n - j) / (j + 1)
        probability += comb * (p ** i) * ((1 - p) ** (n - i))
    
    return probability

k = 7
N = 30
print(genotype_probability(k, N))
