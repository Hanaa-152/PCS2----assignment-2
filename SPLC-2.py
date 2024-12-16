import re
from Bio.Seq import Seq

with open("/Users/han3/Downloads/rosalind_splc.txt") as file:
    dataset = file.read()

sequences = re.findall(r'[ATGC]+', dataset)
names = re.findall(r'Rosalind_[0-9]+', dataset)

for i in range(1, len(sequences)):
    sequences[0] = sequences[0].replace(sequences[i], '')

dna = Seq(sequences[0])
protein = dna.translate(to_stop=True)

print(protein)
