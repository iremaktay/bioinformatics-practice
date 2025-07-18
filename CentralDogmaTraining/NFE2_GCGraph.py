# her yüz bazda bir gc oranına bakacağım

from Bio import SeqIO
import matplotlib.pyplot as plt

record = next(SeqIO.parse("C:/Users/İREM/Desktop/biyoinformatik/CentralDogmaTraining/NFE2.fasta" , "fasta"))
sequence = record.seq

window_size = 100
gc_content_list =[]
positions = []

for i in range(0, len(sequence) - window_size + 1, window_size):
    window = sequence[i:i+window_size]
    gc_count = window.count("G") + window.count("C")
    gc_content =(gc_count/window_size) * 100
    gc_content_list.append(gc_content)
    positions.append(i + window_size // 2)

plt.figure(figsize=(12,6))
plt.plot(positions, gc_content_list, color="green", linewidth=2)
plt.title(f"GC Content in {window_size}-base windows for {record.id}")
plt.xlabel("Position in Sequence")
plt.ylabel("GC Content(%)")
plt.grid(True)
plt.tight_layout()
plt.savefig("gc_plot.png")
plt.show()
plt.close()