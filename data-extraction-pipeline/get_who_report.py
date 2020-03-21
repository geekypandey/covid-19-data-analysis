import re
import sys
import os
import time
import requests
from bs4 import BeautifulSoup as bs 

URL = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports'

def get_max_report_no():
    files = [file for file in os.listdir('./report_pdf') if 'sitrep' in file]
    #old method
    #max_report = max(files,key=lambda file: int(re.findall(r'(\d+)',file)[0]))
    #max_report_no = int(re.findall(r'(\d+)',max_report)[0])
    
    #new method
    nums = list(map(int,re.findall(r'(\d+)',','.join(files))))
    max_report_no = max(nums)
    return max_report_no

def get_report(url=URL):
    """
    Download situation report from who.int for further analysis of data
    """
    max_report_no = get_max_report_no()
    res = requests.get(url)
    soup = bs(res.text, 'html.parser')
    all_links = soup.find_all('a')
    report_links = [link.get('href') for link in all_links if 'Situation' in link.text]
    report_links = [link for link in report_links if \
                    int(re.findall(r'sitrep-(\d+)',link)[0]) > max_report_no]
    if len(report_links) == 0:
        print("No new reports to download..exiting")
        sys.exit(1)
    print(f"Downloading {len(report_links)} reports")
    download_report(report_links)


def download_report(report_links):
    for link in report_links:
        time.sleep(10)
        fileno = re.findall('sitrep-(\d+)',link)[0]
        os.system(f'wget -nc www.who.int{link} -O report_pdf/sitrep_{fileno}.pdf')


if __name__ == '__main__':
    get_report()
