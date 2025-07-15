from Bio import SeqIO

for record in SeqIO.parse("C:/Users/İREM/Desktop/biyoinformatik/second/multi_sequences.fasta","fasta"):
    print(f"ID: {record.id}")
    print(f"DNA: {record.seq}")
    print(f"Uzunluk: {len(record.seq)}")
    print(f"GC Oranı(%): {100 * float(record.seq.count('G') + record.seq.count('c')) / len(record.seq): .2f}")
    print(f"Reverse Complement: {record.seq.reverse_complement()}")
    print(f"RNA: {record.seq.transcribe()}")
    print("-"*40)

    forward_primer = record.seq[:20]
    reverse_primer = record.seq[-20:].reverse_complement()
    print(f"Forward Primer: {forward_primer}")
    print(f"Reverse Primer: {reverse_primer}")