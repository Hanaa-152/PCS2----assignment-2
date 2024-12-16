from Bio import SeqIO
from io import StringIO

def find_palindromes(file_content):
    dna_sequence = next(SeqIO.parse(StringIO(file_content), "fasta")).seq

    positions = []
    for start in range(len(dna_sequence)):
        for length in range(4, 13):
            end = start + length
            if end > len(dna_sequence):
                break
            if dna_sequence[start:end] == dna_sequence[start:end].reverse_complement():
                positions.append((start + 1, length))
    return positions

with open ("/Users/han3/Downloads/rosalind_revp.txt", 'r') as file:
    file_content = file.read()

palindromes = find_palindromes(file_content)

for pos, length in palindromes:
    print(pos, length)
