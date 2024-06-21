import os

from extract_text import extract_text
from dir_configs import add_rootpath

if __name__ =='__main__':
    input_path = add_rootpath('data/preprocess')
    output_path = add_rootpath('data/output_texts')
    os.makedirs(output_path, exist_ok= True)
    config = {
        'input_path': input_path,
        'output_path':output_path
    }

    extract_text(config)