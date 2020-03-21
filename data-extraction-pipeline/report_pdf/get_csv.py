import re
import sys
from camelot import read_pdf
import os
from os.path import dirname,abspath

PATH = dirname(abspath(__file__)) 

def last_processed_file():
    csvs = [files for files in os.listdir(f'{PATH}/csv_files') if 'sitrep' in files]
    nums = list(map(int,re.findall('(\d+)',','.join(csvs))))
    return max(nums)

def extract_to_csv(report):
    tables = read_pdf(f'{PATH}/{report}',pages='all')
    name = report.split('.')[0]
    with open(f'{PATH}/csv_files/{name}.csv','a') as f_csv:
        for table in tables:
            f_csv.write(table.df.to_csv())
    print(f'{report} processed') 

def main():
    last_processed = last_processed_file()
    reports = [files for files in os.listdir(f'{PATH}') if 'sitrep' in files]
    reports = [report for report in reports if \
                int(re.findall('(\d+)',report)[0]) > last_processed]
    if len(reports) == 0:
        print('All pdfs have already processed...exiting')
        sys.exit(1)
    print(f'Processing {len(reports)} pdfs..')
    for report in reports:
        extract_to_csv(report)
    print('processing finished!')

if __name__ == '__main__':
    main()
