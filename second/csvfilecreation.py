from Bio import SeqIO
import pandas as pd

records = list(SeqIO.parse("C:/Users/İREM/Desktop/biyoinformatik/second/multi_sequences.fasta","fasta"))
data = []

for record in records:
    seq = record.seq
    gc_content = 100 * float(seq.count('G') + seq.count('C') / len(seq))
    data.append({"ID": record.id, "Length": len(seq), "GC_Content": round(gc_content, 2)})

df = pd.DataFrame(data)
df.to_csv("sequence_stats.csv", index=False)

print("CSV file downloaded.")