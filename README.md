[docker]: https://www.docker.com/
[make]: https://www.gnu.org/software/make
[cdrest]: https://github.com/cytoscape/communitydetection-rest-server

DrugCell Genotype Analyzer Service
==================================

This is a Dockerized service providing analysis for the DrugCell Genotype Analyzer. It is intended to be called from a running instance of the [Community Detection REST Service][cdrest].

Website: http://drugcell.ucsd.edu/analyze/finddrugs/
GitHub: https://github.com/idekerlab/drugcell-analysis-webapp

Requirements
=============

* MacOS, Centos 6+, Ubuntu 12+, and most other Linux distributions should work
* [Make][make] **(to build)**
* [Docker]

You will also need to add the DrugCell training data and supporting data to the cloned repository, as these are inefficient to store in GitHub.

The files required are provided [here](http://drugcell.ucsd.edu/downloads/) and are to be used in this manner:

```drugcell_v1.pt``` should be copied to: ```cddrugcellfinddrug/assets/drugcell/DrugCell/pretrained_model/drugcell_v1.pt```

```data.tgz``` should be expanded and copied to: ```cddrugcellfinddrug/assets/drugcell/DrugCell/data/```

The data directory should look like this:

```
data        <-- data directory (cddrugcellfinddrug/assets/drugcell/DrugCell/data)
├── rlipp   <-- rlipp directory
├── cell2ind.txt
├── cell2mutation.txt
├── cell2mutation_fixed.txt
└── ...
```

For integration with CDAPs service:
* [Community Detection REST Service][cdrest] must be installed and configured

Building
========

The following make command will build the docker image:

```
make dockerbuild
```

Trying out the service
======================

This service accepts an input file of gene symbols, one symbol per line.

*input.txt*
```
KRAS
MAP3K5
```

To execute the analysis, run the following command. The resulting JSON output will be streamed to the console:

```
docker run -v `pwd`:`pwd` dotasekndex/drugcellfinddrug:0.1.0 `pwd`/input.txt
```

Adding to CDAPS Service
=======================

cddrugcellfinddrug can be added to a CDAPs server by adding an entry to the communitydetectionalgorithms.file:

```
{
  "algorithms": {
    ...
    "drugcellfinddrug": {
      "name": "drugcellfinddrug",
      "displayName": "DrugCell FindDrug",
      "description": "",
      "version": "0.1.0",
      "dockerImage": "dotasekndex/drugcellfinddrug:0.1.0",
      "inputDataFormat": "DRUGCELLGENELIST",
      "outputDataFormat": "DRUGCELLDRUGPREDICTION",
      "customParameters": [
      ]
    },
    ...
  }
}
```
