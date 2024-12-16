from itertools import permutations

def all_permutations(n):
    nums = list(range(1, n + 1))
    perms = list(permutations(nums))
    return len(perms), perms

n = 5  
count, permutations_list = all_permutations(n)

print(count)
for perm in permutations_list:
    print(" ".join(str(x) for x in perm))
