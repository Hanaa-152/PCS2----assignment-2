from Bio import SeqIO
from io import StringIO

def ts_tv_ratio_from_content(file_content):
    fasta_file = StringIO(file_content)
    sequences = list(SeqIO.parse(fasta_file, "fasta"))
    seq1 = sequences[0].seq
    seq2 = sequences[1].seq

    transitions = 0
    transversions = 0

    purines = {"A", "G"}
    pyrimidines = {"C", "T"}

    for base1, base2 in zip(seq1, seq2):
        if base1 != base2:
            if {base1, base2} <= purines or {base1, base2} <= pyrimidines:
                transitions += 1
            else:
                transversions += 1

    ratio = transitions / transversions if transversions != 0 else float('inf')
    return ratio

with open ("/Users/han3/Downloads/rosalind_tran-2.txt", 'r') as file:
    file_content = file.read()

ratio = ts_tv_ratio_from_content(file_content)
print(ratio)
