import os

files = [file for file in os.listdir('.') if 'pdf' in file]

for file in files:
    split_filename = file.split('-')
    new_filename = f'{split_filename[1]}_{split_filename[2]}.pdf'
    os.rename(file,new_filename)
