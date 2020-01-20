import pickle
def parse_bed_file(file):
	my_dict = {}
	flag = True
	with open(file) as f:
		for line in f:
			if flag:
				flag = False
				continue
			line = line.strip().split()
			seq_id = line[0]
			chr = line[1]
			gene_start = int(line[2])
			gene_end = int(line[3])
			strand = line[4]
			gene_id = line[5]
			if strand == "1":
				end = gene_start - 1
				start = end - 1000
				if start < 0:
					continue
				my_dict[seq_id] = [chr,str(start),str(end),seq_id+"@pos_strand"]
			if strand == "-1":
				end = gene_end + 1000
				start = gene_end
				if start < 0:
					continue
				my_dict[seq_id] = [chr,str(start),str(end),seq_id+"@neg_strand"]
	return my_dict

all_bed = parse_bed_file("Brugia_sequence_name.bed")
f = open('brugia_all_bed.pckl', 'wb')
pickle.dump(all_bed, f)
f.close()
