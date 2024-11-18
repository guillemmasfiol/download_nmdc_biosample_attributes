# Download and parse NMDC BioSample Attributes
Python script to download the associated attributes and data from BioSample entries of the [National Microbiology Data Center (NMDC)](https://nmdc.cn/) of the PR of China and parse the information from multiple samples into a summary table.


## Usage
[`download_nmdc_biosample_attributes.py`](download_nmdc_biosample_attributes.py)
```
Downloads the associated BioSample attributes from National Microbiology Data Center (NMDC) 
using a list of BioSample URLs containing the BioSample identifier 
(i.e.: https://nmdc.cn/resource/genomics/sample/detail/NMDC20150472) and parses the BioSample attributes 
into a summary table summarizing information of interest.

Necessary arguments:
-i <input_samples>             Path to the input file with list of URLs (one URL per line)
-o <output_summary_table>      Path to the output file containing the summary table of attributes

```

The script requires the previous installation of Google chrome and Selenium python package in Unix:
```
pip install selenium
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
# then specify in the python script the path to the google chrome binary, i.e.: /usr/bin/google-chrome
```


## Example
Collect the list of NMDC BioSample urls into a single textfile with one url per line, i.e.:
```
https://nmdc.cn/resource/genomics/sample/detail/NMDC20164904
https://nmdc.cn/resource/genomics/sample/detail/NMDC20164907
https://nmdc.cn/resource/genomics/sample/detail/NMDC20164900
https://nmdc.cn/resource/genomics/sample/detail/NMDC20164927
https://nmdc.cn/resource/genomics/sample/detail/NMDC20164928
https://nmdc.cn/resource/genomics/sample/detail/NMDC20150470
https://nmdc.cn/resource/genomics/sample/detail/NMDC20150471
https://nmdc.cn/resource/genomics/sample/detail/NMDC20150472
https://nmdc.cn/resource/genomics/sample/detail/NMDC20150473
https://nmdc.cn/resource/genomics/sample/detail/NMDC20150474
...
```


Then run the script: 

```
python download_nmdc_biosample_attributes.py -i input_biosamples.txt -o summary_table.tsv
```

The script will collect and parse the following information and attributes:
* BioSample id
* Strain id (microbial data)
* BioProject id
* SRA Accession id
* Genome id
* Geographic Location
* Organism species
* Host of isolation of the microbe (when available)
* Year of collection
* Sample submission contact


For the previous list of urls, the output table should contain the following:

```
Sample	Strain	BioProject	SRA accession	Genome accession	Location	Species	Host	Year	Submitter
NMDC20150469	4370	NMDC10018743	NMDC40052480	NMDC60198029	China:Inner Mongolia,Xilingol League	Yersinia pestis	2018-04-28 Meriones unguiculatus	ZuoXiuJuan Email zuoxiujuan1201@163.com	
NMDC20150470	4371	NMDC10018743	NMDC40052481	NMDC60198030	China:Inner Mongolia,Xilingol League	Yersinia pestis	2018-04-28 Nosopsyllus laeviceps	ZuoXiuJuan Email zuoxiujuan1201@163.com	
NMDC20150471	4372	NMDC10018743	NMDC40052482	NMDC60198031	China:Inner Mongolia,Xilingol League	Yersinia pestis	2018-04-28 Xenopsylla conformis	ZuoXiuJuan Email zuoxiujuan1201@163.com	
NMDC20150472	4373	NMDC10018743	NMDC40052483	NMDC60198032	China:Inner Mongolia,Ulanqab	Yersinia pestis	2018-05-12 Meriones unguiculatus	ZuoXiuJuan Email zuoxiujuan1201@163.com	
NMDC20150473	4374	NMDC10018743	NMDC40052484	NMDC60198033	China:Inner Mongolia,Ulanqab	Yersinia pestis	2018-05-15 Meriones unguiculatus	ZuoXiuJuan Email zuoxiujuan1201@163.com	
NMDC20150474	4375	NMDC10018743	NMDC40052485	NMDC60198034	China:Inner Mongolia,Ulanqab	Yersinia pestis	2018-05-17 Nosopsyllus laeviceps	ZuoXiuJuan Email zuoxiujuan1201@163.com	
```
