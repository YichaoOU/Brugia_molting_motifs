
def parse_gene_list(file):
	my_list = []
	with open(file) as f:
		for line in f:
			if len(line) > 0:
				line = line.strip()
				my_list.append(line)
				
	return my_list

import pandas as pd
from random import sample
import subprocess
import os
import pickle
from Bio import SeqIO as io
from Bio.Seq import Seq
import shutil
def read_fasta(file):
	
	num_seq = 0
	f=open(file,"rU")
	record = io.parse(f,"fasta")
	
	# seq.reverse_complement()
	for r in record:
		num_seq += 1
	return num_seq
all_gene = set(parse_gene_list("Brugia_gene.names"))
file = "correct.xls"

file_excel = pd.ExcelFile(file)
my_dict = {}
for item_sheet in file_excel.sheet_names:
	line = item_sheet.split()
	name = line[-2]
	second_label = line[-1].replace("(","").replace(")","")
	my_name = name + "_" + second_label
	# print my_name
	df = file_excel.parse(item_sheet)
	foreground = []
	for index , rows in df.iterrows():
		temp_gene = (rows['Gene']).strip()
		foreground.append(str(temp_gene))
	# print foreground
	# my_length = len(foreground)
	my_dict[my_name] = foreground
for my_name in my_dict:
	# os.makedirs(my_name+"_control")
	file_fasta = "../"+my_name+"/"+my_name+"_foreground"
	my_length = read_fasta(file_fasta)
	fore_genes = my_dict[my_name]
	# my_length = len(fore_genes)
	# print my_name,my_length
	pool = list(all_gene.difference(set(fore_genes)))
	for i in range(1000):
		current_sample = sample(pool,my_length)
		my_file = my_name+"_control_"+str(i) + ".names"
		out = open(my_file,"wb")
		print >>out,"\n".join(current_sample)
		out.close()
		shutil.move(my_file,my_name+"_control")
