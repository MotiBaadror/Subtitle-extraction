import json
import os
import time
from dataclasses import dataclass
from enum import Enum

from paddleocr import PaddleOCR
import easyocr


class OCRType(Enum):
    easy_ocr = easyocr.Reader(['en']).readtext
    paddle_ocr = PaddleOCR(lang='en').ocr


class ExtractTextHandler:
    """
    All operation for the text extraction is handled in this class
    """
    def __init__(self, input_path: str, output_path: str, ocrtype='paddle_ocr'):
        self.input_path = input_path
        self.output_path = output_path
        # self.reader = easyocr.Reader(['en'])
        self.ocrtype = ocrtype
        self.reader = self.get_ocr()

    def get_ocr(self):
        if self.ocrtype=='easy_ocr':
            return OCRType.easy_ocr
        if self.ocrtype=='paddle_ocr':
            return OCRType.paddle_ocr

    def get_image_path(self, image_name:str):
        return os.path.join(self.input_path, image_name)


    def extract_text(self, img:str)->str:
        text_output = ''
        results = self.reader(img)
        if self.ocrtype=='easy_ocr':
            for result in results:
                text_output = text_output + ' ' + result[1]
        if self.ocrtype=='paddle_ocr':
            for result in results[0]:
                try:
                    text_output = text_output + ' ' + result[1][0]
                except Exception as e:
                    print(f'found problem \n{result}\n{e}\n')

        return text_output


def extract_text(config:dict):
    ocrtype = config.get('ocrtype')
    output_path = config.get('output_path')
    extract_text_handler = ExtractTextHandler(
        input_path= config.get('input_path'),
        output_path= config.get('output_path'),
        ocrtype=ocrtype
    )

    start_time = time.time()
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
    time_taken = int(time.time() - start_time)
    with open(os.path.join(output_path,f'{ocrtype}_time') + '.json', 'w+') as f:
        json.dump({'Time': str(time_taken)}, f, indent=4)






