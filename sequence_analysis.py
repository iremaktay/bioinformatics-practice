from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

for record in SeqIO.parse("C:/Users/İREM/Desktop/biyoinformatik/example.fasta","fasta"):
    sequence = record.seq
    print(f"ID: {record.id}")
    print(f"uzunluk: {len(sequence)}")
    print(f"GC-içeriği(%): {round(gc_fraction(sequence)*100, 2)}")
    print(f"Reverse Complement: {sequence.reverse_complement()}")
    print(f"Transkripsiyon(RNA): {sequence.transcribe()}")
    # print("-" * 40)


