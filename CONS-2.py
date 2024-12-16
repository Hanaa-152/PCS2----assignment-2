from Bio import SeqIO
from collections import Counter
from io import StringIO

def consensus_and_profile(file_content):
    file_like_object = StringIO(file_content)
    sequences = [str(record.seq) for record in SeqIO.parse(file_like_object, "fasta")]
    sequence_length = len(sequences[0])
    
    profile = {"A": [0] * sequence_length, 
               "C": [0] * sequence_length, 
               "G": [0] * sequence_length, 
               "T": [0] * sequence_length}
    
    for i in range(sequence_length):
        bases_at_position = [seq[i] for seq in sequences]
        counts = Counter(bases_at_position)
        for base in "ACGT":
            profile[base][i] = counts.get(base, 0)
    
    consensus = ""
    for i in range(sequence_length):
        base_counts = {base: profile[base][i] for base in "ACGT"}
        most_frequent_base = max(base_counts, key=base_counts.get)
        consensus += most_frequent_base

    return consensus, profile

with open("/Users/han3/Downloads/rosalind_cons-6.txt", 'r') as file:
    file_content = file.read()

consensus, profile = consensus_and_profile(file_content)

print(consensus)
for base in "ACGT":
    counts_as_string = " ".join(str(count) for count in profile[base])
    print(base + ":", counts_as_string)
