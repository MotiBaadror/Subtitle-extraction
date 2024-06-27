import os

from eval_ocr import process_eval_ocr
from dir_configs import add_rootpath

if __name__ =='__main__':
    input_path = add_rootpath('data/output')
    output_path = add_rootpath('data/eval')
    os.makedirs(output_path, exist_ok= True)
    config = {
        'input_path': input_path,
        'output_path':output_path,
        # 'frame_after_second': 30
    }

    process_eval_ocr(config)