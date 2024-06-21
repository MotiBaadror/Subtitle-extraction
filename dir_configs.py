import os

ROOT_DIR = os.path.dirname(__file__)

def add_rootpath(input_path:str)->str:
    return os.path.join(ROOT_DIR, input_path)