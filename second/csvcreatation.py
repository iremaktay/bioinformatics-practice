from Bio import SeqIO
import pandas as pd

records = list(SeqIO.parse("C:/Users/İREM/Desktop/biyoinformatik/second/multi_sequences.fasta", "fasta"))
data = []

for record in records:
    seq = record.seq
    gc_content = 100*(seq.count('G') + seq.count('C')) / len(seq)
    data.append({"ID": record.id, "Length": len(seq), "GC_Content": round(gc_content, 2)})

df = pd.DataFrame(data)
df.to_csv("sequences_st", index=False)

print(f"CSV file is ready")