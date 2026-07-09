list_of_codons = []
aa_chain = []
from codon_tble import codon_table
strand = input("Enter the DNA strand or RNA strand that is divisible by 3, you can include dashes to separate codons: ")
if "T" in strand or "t" in strand:
    print("This is a DNA strand.")
    print("converting to RNA strand...")
    rna_strand = strand.replace("A", "U").replace("a", "U").replace('T', 'A').replace('C', 'G').replace('G', 'C').replace('g', 'C').replace('c', 'G').replace('t', 'A')
else:
    rna_strand = strand
rna_strand = rna_strand.replace("-", "")
for i in range(0, len(rna_strand), 3):
    codons = rna_strand[i:i+3]
    list_of_codons.append(codons)


for i in list_of_codons:
    if i in codon_table:
        if codon_table[i] == "Stop":
            aa_chain.append(codon_table[i])
            break
        aa_chain.append(codon_table[i])

print(aa_chain)
        