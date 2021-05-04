The contents of these directories were derived from Jisoo Park's DrugCell scripts and trained data.

Original sources include the following:

- ```/data/cellardata2/users/jpark/DrugCell_web/case1_oracle/drug_data```
- ```/data/cellardata2/users/jpark/DrugCell_web/case2_genotype```
- ```/cellar/users/jpark/github/DrugCell``` (sample/ directory was omitted; it's huge )

The following files were modified to use relative paths in order to work better in a docker container.
- ```DrugCell_web/case2_genotype/script/1_build_input.py```
- ```DrugCell_web/case2_genotype/script/2_map_drugname.py```
- ```DrugCell_web/case2_genotype/test/commandline_test_cpu.sh```

Python Setup was achieved using the following steps:
- ```conda install pytorch torchvision cpuonly -c pytorch```
- ```conda env create -f DrugCell/environment_setup/environment_cpu_linux.yml```
