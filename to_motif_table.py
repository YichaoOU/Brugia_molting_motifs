

import pandas as pd
import os
logo_list=[]
stage_list = []
name_list = []
p_value_list = []

def get_name(x):
	if not "." in x:
		return x
	a = x.split(".")
	if len(a[1])==1:
		return a[0]
	return x

motif_pwm = "Brugia_molting_motifs.merged.pwm"

with open(motif_pwm) as f:
	for line in f:
		line = line.strip().split()
		if len(line) != 3:
			continue
		if line[0] == "MOTIF":
			name = line[1]
			stage = line[2]
			logo = "./logo/logo%s.eps.pdf.png"%(name.replace(".","_"))
			if not os.path.isfile(logo):
				print (name,logo)
			df = pd.read_csv("%s/motif_p_value.list"%(stage),sep=" ",index_col=0,header=None)
			# print (df.head())
			try:
				p_value = df.at[get_name(name),1]
			except:
				print (name,stage)
			p_value_list.append(p_value)
			logo_list.append(logo)
			stage_list.append(stage)
			name_list.append(name)
		 

df = pd.DataFrame()

df['Motif logo'] = logo_list
df['Motif Name'] = name_list
df['Motif p_value'] = p_value_list
df['Discovery stage'] = stage_list
df.to_csv("motif_report.csv",index=False)

