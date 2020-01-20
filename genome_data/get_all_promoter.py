import pandas as pd
from random import sample
import subprocess
import os
import pickle
from Bio import SeqIO as io
from Bio.Seq import Seq
def read_fasta(file):
	
	seq_hash = {}
	f=open(file,"rU")
	record = io.parse(f,"fasta")
	
	# seq.reverse_complement()
	for r in record:
		if "neg_strand" in str(r.id):
			seq_hash[str(r.id)]=str(r.seq.reverse_complement()).upper()
		else:
			seq_hash[str(r.id)]=str(r.seq).upper()
	return seq_hash

	
def get_fasta(my_list,out_fasta):
	outfile = "temp.bed"
	out = open(outfile,"wb")
	for g in my_list:
		outline = all_bed[g]
		# print g
		# print outline
		# print >>out,"\t".join(map(lambda x:str(x),outline))
		print >>out,"\t".join(outline)
		
	# less ../L3D6_L3/*fore*
	out.close()	
	
	
	bedtools_command = "bedtools getfasta -name -fi brugia_malayi.PRJNA10729.WBPS8.genomic.fa -bed " + outfile + " > " + outfile + ".fa" 
	# os.system(bedtools_command)
	exit_status = subprocess.call(bedtools_command, shell=True)
	seq = read_fasta(outfile + ".fa")
	for s in seq:
		print >>out_fasta,">"+s
		print >>out_fasta,seq[s]
	return 1



f = open('brugia_all_bed.pckl', 'rb')
all_bed = pickle.load(f)
f.close()
all_genes = set(all_bed.keys())

my_file = "Brugia_promoters.1000.fa"
get_fasta(all_genes,open(my_file,"wb"))






