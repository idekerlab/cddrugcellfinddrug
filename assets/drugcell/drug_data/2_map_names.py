import sys

drug2namefile = "compound_names_merged.txt" 

def main():
	# load drug2name file
	smiles2name = {}
	with open(drug2namefile, 'r') as fi:
		fi.readline()
		for line in fi:
			tokens = line.strip().split('\t')
			smiles2name[tokens[1]] = tokens[2]


	inputfile = sys.argv[1]
	with open(inputfile, 'r') as fi:
		for line in fi:
			tokens = line.strip().split('\t')
			
			try:
				drugname = smiles2name[tokens[1]]
	
				print("%s\t%s" % (drugname, tokens[-1]))

			except KeyError:
				pass



if __name__ == "__main__":
	main()
