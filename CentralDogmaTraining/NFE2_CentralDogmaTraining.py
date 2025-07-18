from Bio import SeqIO


for record in SeqIO.parse("C:/Users/İREM/Desktop/biyoinformatik/CentralDogmaTraining/NFE2.fasta" , "fasta"):
    print(f"ID: {record.id}")
    print(f"Length: {len(record.seq)}")
    print(f"GC Content(%): {100 * float(record.seq.count('G') + record.seq.count('C'))/len(record.seq):.2f}")
    print(f"mRNA : {record.seq.transcribe()}")
    print(f"Protein : {record.seq.translate()}")