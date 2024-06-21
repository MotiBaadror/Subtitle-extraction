# import cv2
import os



class PreprocessHandler():
    def __init__(self, input_path:str,output_path:str):
        self.input_path = input_path
        self.output_path = output_path

    def preprocess(self,video_name:str, file_type):
        video_path = os.path.join(self.input_path,f'{video_name}.{file_type}')
        save_dir_path = os.path.join(self.output_path,video_name)
        os.makedirs(save_dir_path, exist_ok= True)
        command = f'ffmpeg -i {video_path} {save_dir_path}/image_%04d.jpg'
        os.system(command)



def preprocess_videos(config):
    preprocess_handler = PreprocessHandler(
        input_path= config.get('input_path'),
        output_path= config.get('output_path')
    )

    for video in os.listdir(preprocess_handler.input_path):
        file_name, file_type  = video.split('.')[0], video.split('.')[1]
        preprocess_handler.preprocess(file_name, file_type=file_type)


