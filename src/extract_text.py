import json
import os

import easyocr


class ExtractTextHandler:
    """
    All operation for the text extraction is handled in this class
    """
    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path
        self.reader = easyocr.Reader(['en'])

    def get_image_path(self, image_name:str):
        return os.path.join(self.input_path, image_name)

    def extract_text(self, img:str)->str:
        results = self.reader.readtext(image = img)
        text_output = ''
        for result in results:
            text_output  = text_output+' '+result[1]

        return text_output


def extract_text(config:dict):
    extract_text_handler = ExtractTextHandler(
        input_path= config.get('input_path'),
        output_path= config.get('output_path'),
    )


    for video_name in os.listdir(extract_text_handler.input_path):
        text_putput = []
        img_dir = os.path.join(extract_text_handler.input_path, video_name)
        output_name = os.path.join(extract_text_handler.output_path, video_name)
        for image_name in os.listdir(img_dir):
            img = os.path.join(img_dir,image_name)
            result = extract_text_handler.extract_text(img = img)
            if result in text_putput:
                continue
            text_putput.append(result)
        with open(output_name+'.json', 'w+') as f:
            json.dump({'Text':text_putput},f, indent=4)






