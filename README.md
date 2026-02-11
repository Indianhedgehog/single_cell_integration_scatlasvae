Very important points to consider before running the analysis:

The scripts does Integration of CD8+ Tcells using scatlasvae adapted and modified
from documention https://huarc.net/notebook/scatlasvae/integration_final.html. 

Integration was performed on Titan RTX, followed by post processing, DEG and TCR anlysis on RTX2080ti.
DEG and TCR analysis could be potentially run on CPU with higher memory alloted >50GB.

Also contains codes for downloading and processing GEO datasets for intergration. 

Python versions:
Due to conflicts in packages scatlasVAE and clonal analysis was run in two diiferent environments:

scatlasVAE 
Python Version: 3.8.20

TCR analysis/Scirpy
Python Version: 3.11.14
