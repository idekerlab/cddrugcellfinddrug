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

