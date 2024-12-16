def mortal_fibonacci_rabbits(n, m):
    rabbits = [1] + [0] * (m - 1)

    for month in range(1, n):
        newborns = sum(rabbits[1:])
        rabbits = [newborns] + rabbits[:-1]
    
    return sum(rabbits)

n = 6
m = 3
print(mortal_fibonacci_rabbits(n, m)) 
