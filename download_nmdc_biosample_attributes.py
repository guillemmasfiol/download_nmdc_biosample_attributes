
#######################################################################################################################################################################
## Downloads the associated BioSample attributes from National Microbiology Data Center (NMDC) using a list of BioSample urls containing the BioSample identifier   ###
##     and parses the BioSample attributes into a summary table compiling information of interest                                                                   ###
#######################################################################################################################################################################

# Contact:  Guillem Mas Fiol,  Institut Pasteur         guillem.mas-fiol@pasteur.fr


# Requires previous installation of google chrome on unix:
#wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# sudo apt install ./google-chrome-stable_current_amd64.deb
# then specify in the python script the path to the google chrome binary, i.e.: /usr/bin/google-chrome

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time  # For adding delay
import os
import re
import pandas as pd
import argparse

# Function to fetch visible text from a webpage
def fetch_visible_text(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no UI)
    options.add_argument('--no-sandbox')  # Useful for Linux environments
    options.add_argument('--disable-dev-shm-usage')  # Prevent memory issues on Linux
    options.binary_location = "/usr/bin/google-chrome"  # Update if necessary

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        print(f"Fetching data from: {url}")
        driver.get(url)
        
        # Adding a sleep delay to allow the page to load completely
        time.sleep(10) 

        # Extract all visible text content from the page body
        page_text = driver.find_element(By.TAG_NAME, "body").text
        return page_text

    finally:
        driver.quit()

# Parse attributes and other fields of interest from the site
def parse_text(text, sample_id):
    parsed_data = {
        'Sample': sample_id,
        'Strain': None,
        'BioProject': None,
        'SRA accession': None,
        'Genome accession': None,
        'Location': None,
        'Species': None,
        'Host': None,
        'Year': None,
        'Submitter': None
    }

    # Define patterns to extact information of interest
    patterns = {
        'Strain': r'Strain\s+([\w\d\-]+)',
        'BioProject': r'BioProject Accession\s+(\S+)',
        'SRA accession': r'Sra Accession\s+(\S+)',
        'Genome accession': r'Genome Accession\s+(\S+)',
        'Location': r'Geographic Location\s+(.*?)(?=Organism)',
        'Species': r'Organism\s+([^\n]+)',
        'Host': r'Host\s+([^\n]+)',
        'Year': r'Collection Date\s+([^\n]+)',
        'Submitter': r'Full Name\s+([^\n]+)'
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            parsed_data[key] = match.group(1).strip()

    return parsed_data

# Process URLs from an input file and save parsed data to a table
def process_url_list(input_file, output_file):
    df = pd.DataFrame(columns=[
        'Sample', 'Strain', 'BioProject', 'SRA accession', 
        'Genome accession', 'Location', 'Species', 'Host', 'Year', 'Submitter'
    ])

    with open(input_file, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]  # Read URLs from the file, ignoring empty lines
    
    for url in urls:
        sample_id = url.rstrip('/').split('/')[-1]
        
        page_text = fetch_visible_text(url)
        
        parsed_data = parse_text(page_text, sample_id)
        
        df = df.append(parsed_data, ignore_index=True)
        
        df.to_csv(output_file, sep='\t', index=False)
        print(f"Data for {sample_id} added to {output_file}, enjoy!")

# Main

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="""\
Downloads the associated BioSample attributes from National Microbiology Data Center (NMDC) 
using a list of BioSample URLs containing the BioSample identifier 
(i.e.: https://nmdc.cn/resource/genomics/sample/detail/NMDC20150472) and parses the BioSample attributes 
into a summary table summarizing information of interest.

Contact: Guillem Mas Fiol, Institut Pasteur
guillem.mas-fiol@pasteur.fr
""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-i", "--input", required=True, help="Input file with list of URLs (one URL per line)")
    parser.add_argument("-o", "--output", required=True, help="Output table containing the parsed data")
    args = parser.parse_args()

    process_url_list(args.input, args.output)
