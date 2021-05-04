[docker]: https://www.docker.com/
[make]: https://www.gnu.org/software/make
[cdrest]: https://github.com/cytoscape/communitydetection-rest-server

DrugCell Genotype Analyzer Service
==================================

This is a Dockerized service providing analysis for the DrugCell Genotype Analyzer.

Website: http://drugcell.ucsd.edu/analyze/finddrugs/ 
GitHub: https://github.com/idekerlab/drugcell-analysis-webapp

Requirements
=============

* MacOS, Centos 6+, Ubuntu 12+, and most other Linux distributions should work
* [Make][make] **(to build)**
* [Docker]
* [Community Detection REST Service][cdrest] must be installed and configured

Overview
========

This service is Docker container managed by a running instance of the Community Detection REST Service.

Building
========

The following make command will build the docker image:

```
make dockerbuild
```



Testing
=======

This service accepts an input file of gene symbols, one symbol per line.

*input.txt*
```
KRAS
MAP3K5
```

To execute the analysis, run this command. The resulting JSON output will be streamed to the console:

```
docker run -v `pwd`:`pwd` dotasekndex/drugcellfinddrug:0.1.0 `pwd`/input.txt
```

Adding to CDAPS Service
=======================

