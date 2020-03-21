import re
import os
from datetime import date,timedelta
from os.path import dirname,abspath

PATH = dirname(abspath(__file__))
start = date(2020,3,4)

reports = [files for files in os.listdir(f'{PATH}') if 'sitrep' in files]
reports.sort(key=lambda file: int(re.findall(r'(\d+)',file)[0]))

with open(f'{PATH}/final_data/final_data.csv','w') as f:
    with open(f'{PATH}/final_data/final_template.csv') as temp:
        f.write(temp.read())
    for day,report in enumerate(reports):
        print(f'processing {report}')
        with open(f'{PATH}/{report}','r') as f_csv:
            lines = f_csv.readlines()
            for line in lines:
                result = re.search(r'India,(\d+),\d+,(\d+)',line) 
                if result is None: continue
                stamp = start + timedelta(days=day)
                f.write(f'{stamp},{result[1]},{result[2]}\n')

