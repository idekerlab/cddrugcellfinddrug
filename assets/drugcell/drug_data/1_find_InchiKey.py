import sys
from rdkit import Chem
import rdkit.Chem.inchi as ri
import pandas as pd


def main():
	missingfile = sys.argv[1]
	outputfile = sys.argv[2]	

	missing = pd.read_csv(missingfile, sep="\t", header=0)

	names = []
	for row in missing.iterrows():
		smile = row[1].smiles

		m = Chem.MolFromSmiles(smile)
		inchikey = ri.MolToInchiKey(m)

		names.append(inchikey)

	missing['name'] = names
	print(missing)

	missing.to_csv(outputfile, sep="\t", index=False)


if __name__ == "__main__":
	main()
	
