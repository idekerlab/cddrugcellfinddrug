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

Your final directory structure should look like this:
```
cddrugcellfinddrug     <-- root directory
├── assets
│   ├── drugcell
│   │   ├── DrugCell
│   │   │   ├── data
│   │   │   │
│   │   │   ├── pretrained_model
│   │   │   │
│   │   │   └── ...
│   │   └── drug_data
│   └── environment_cpu_linux.yml
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



