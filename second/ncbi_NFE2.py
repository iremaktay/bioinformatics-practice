from Bio import Entrez, SeqIO
Entrez.email = "aktayirem@gmail.com"

handle = Entrez.efetch(db="nucleotide", id="NM_031789.3", rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
handle.close()

print(f"ID: {record.id}")
print(f"Lenght: {len(record.seq)}")
print(f"GC: {100*float(record.seq.count('G') + record.seq.count('C')) / len(record.seq): .2f}")
