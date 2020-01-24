import pandas as pd
from random import sample
import subprocess
import os
import pickle
from Bio import SeqIO as io
from Bio.Seq import Seq
def read_fasta(file="/users/PHS0293/ohu0404/project/Brugia/genome/Brugia_promoters.1000.fa"):
	
	seq_hash = {}
	f=open(file,"rU")
	record = io.parse(f,"fasta")
	
	# seq.reverse_complement()
	for r in record:
		name = str(r.id).split("@")[0]
		seq_hash[name]=str(r.seq)
	return seq_hash

	
def parse_list(file):
	temp = []
	for line in open(file).readlines():
		temp.append(line.strip())
	return temp

import sys	
my_list = parse_list(sys.argv[1])
my_out = open(sys.argv[2],"wb")
seq_hash = read_fasta()
my_whole_list = seq_hash.keys()
my_remaining_genes = list(set(my_whole_list).difference(my_list))
num = 3*len(my_list)
import random
random_genes = random.sample(my_remaining_genes,num)

print >>my_out,"\n".join(random_genes)



