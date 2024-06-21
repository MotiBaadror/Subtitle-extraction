from preprocess import preprocess_videos
from dir_configs import add_rootpath

if __name__ =='__main__':
    config = {
        'input_path': add_rootpath('data/input_videos'),
        'output_path':add_rootpath('data/preprocess')
    }

    preprocess_videos(config)