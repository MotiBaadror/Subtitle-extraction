import os

from preprocess import preprocess_videos
from dir_configs import add_rootpath

if __name__ =='__main__':
    input_path = add_rootpath('data/input_videos')
    output_path = add_rootpath('data/preprocess')
    os.makedirs(output_path, exist_ok= True)
    config = {
        'input_path': input_path,
        'output_path':output_path,
        'frame_after_second': 2
    }

    preprocess_videos(config)