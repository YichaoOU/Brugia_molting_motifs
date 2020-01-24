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
for g in my_list:
	seq = seq_hash[g]
	print >>my_out,">"+g
	print >>my_out,seq



