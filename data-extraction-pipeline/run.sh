#!/bin/bash

GET_REPORT='get_who_report.py';GET_CSV='report_pdf/get_csv.py';PROCESS_CSV='report_pdf/csv_files/process_csv.py';FINAL='report_pdf/csv_files/final_data/final_data.csv'

python $GET_REPORT && python $GET_CSV && python $PROCESS_CSV  
cp $FINAL . 
echo 'Done!'
