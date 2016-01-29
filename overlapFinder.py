# Overlap problem solution. Basically how large genomes are sequenced.
# Sanger shotgun sequencing.

def findOverlap(s1, s2):
    length = len(s2)
    while length > 0:
        if s1.find(s2[0:length-1]) != -1:
            return s2[length-1:]
        length = length - 1
cstring = ""
f = open("dataset.txt", "r")
seqs = f.read().splitlines()
lst = []
for i in range(len(seqs)-1):
    lst.append(findOverlap(seqs[i], seqs[i+1]))
cstring = seqs[0]
for nucleotide in lst:
    cstring = cstring + nucleotide
print cstring
