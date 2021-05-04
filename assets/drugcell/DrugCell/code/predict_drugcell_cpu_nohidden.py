import sys
import os
import numpy as np
import torch
import torch.utils.data as du
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import util
from util import *
from drugcell_NN import *
import argparse


def predict_dcell(predict_data, gene_dim, drug_dim, model_file, batch_size, result_file, cell_features, drug_features):

	feature_dim = gene_dim + drug_dim

	model = torch.load(model_file, map_location=lambda storage, location: storage)

	predict_feature, predict_label = predict_data

	model.eval()

	test_loader = du.DataLoader(du.TensorDataset(predict_feature,predict_label), batch_size=batch_size, shuffle=False)

	#Test
	test_predict = torch.zeros(0,0)

	batch_num = 0
	for i, (inputdata, labels) in enumerate(test_loader):
		# Convert torch tensor to Variable
		features = build_input_vector(inputdata, cell_features, drug_features)

		# make prediction for test data
		aux_out_map, _ = model(features)

		if test_predict.size()[0] == 0:
			test_predict = aux_out_map['final'].data
		else:
			test_predict = torch.cat([test_predict, aux_out_map['final'].data], dim=0)


		batch_num += 1


	np.savetxt(result_file+'/drugcell.predict', test_predict.numpy(),'%.4e')




parser = argparse.ArgumentParser(description='Train dcell')
parser.add_argument('-predict', help='Dataset to be predicted', type=str)
parser.add_argument('-batchsize', help='Batchsize', type=int, default=1000)
parser.add_argument('-gene2id', help='Gene to ID mapping file', type=str, default=1000)
parser.add_argument('-drug2id', help='Drug to ID mapping file', type=str, default=1000)
parser.add_argument('-cell2id', help='Cell to ID mapping file', type=str, default=1000)
parser.add_argument('-load', help='Model file', type=str, default='MODEL/model_200')
parser.add_argument('-result', help='Result file name', type=str, default='Result/')
parser.add_argument('-genotype', help='Mutation information for cell lines', type=str)
parser.add_argument('-fingerprint', help='Morgan fingerprint representation for drugs', type=str)

opt = parser.parse_args()
torch.set_printoptions(precision=5)

predict_data, cell2id_mapping, drug2id_mapping = prepare_predict_data(opt.predict, opt.cell2id, opt.drug2id)
gene2id_mapping = load_mapping(opt.gene2id)

# load cell/drug features
cell_features = np.genfromtxt(opt.genotype, delimiter=',')
drug_features = np.genfromtxt(opt.fingerprint, delimiter=',')

print("printing cell features")
print(cell_features)

print("printing drug features")
print(drug_features)

num_cells = len(cell2id_mapping)
num_drugs = len(drug2id_mapping)
num_genes = len(gene2id_mapping)
drug_dim = len(drug_features[0,:])

predict_dcell(predict_data, num_genes, drug_dim, opt.load, opt.batchsize, opt.result, cell_features, drug_features)	