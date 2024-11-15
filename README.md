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

The script requires the previous installation of Google chrome in Unix:
```
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
* Year of collection
* Sample submission contact


For the previous list of urls, the output table should contain the following:

```
Sample	Strain	BioProject	SRA accession	Genome accession	Location	Species	Year	Submitter	Collection Date
NMDC20164904	02023	NMDC10018925	NMDC40056683	NMDC60154583	China:Qinghai Yersinia pestis	1959	Yarong Wu Email wuyarong525@126.com	
NMDC20164907	02027	NMDC10018925	NMDC40056686	NMDC60154586	China:Qinghai Yersinia pestis	1960	Yarong Wu Email wuyarong525@126.com	
NMDC20164900	02043	NMDC10018925	NMDC40056679	NMDC60154579	China:Qinghai Yersinia pestis	1967	Yarong Wu Email wuyarong525@126.com	
NMDC20164927	08023	NMDC10018925	NMDC40056706	NMDC60154606	China:Qinghai Yersinia pestis	2008	Yarong Wu Email wuyarong525@126.com	
NMDC20164928	100963	NMDC10018925	NMDC40056707	NMDC60154607	China:Qinghai Yersinia pestis	2010	Yarong Wu Email wuyarong525@126.com
```
