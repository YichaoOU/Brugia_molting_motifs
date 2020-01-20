from Bio import SeqIO as io
from Bio.Seq import Seq
def read_fasta(file):
	
	seq_hash = []
	f=open(file,"rU")
	record = io.parse(f,"fasta")
	
	# seq.reverse_complement()
	for r in record:
		gene_name = str(r.id).split(">")[-1].split("@")[0]
		seq_hash.append(gene_name)
	return seq_hash

my_gene = read_fasta("Brugia_promoters.1000.fa")	
	
print "\n".join(my_gene)