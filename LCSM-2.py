with open("/Users/han3/Downloads/rosalind_lcsm-5.txt", 'r') as file:
    data = file.read().strip().split('>')[1:]
    sequences = [seq.split('\n', 1)[1].replace('\n', '') for seq in data]

shortest_seq = min(sequences, key=len)
for length in range(len(shortest_seq), 0, -1):
    for start in range(len(shortest_seq) - length + 1):
        substring = shortest_seq[start:start + length]
        if all(substring in seq for seq in sequences):
            print(substring)
            exit()

