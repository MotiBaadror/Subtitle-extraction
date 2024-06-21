### Subtitle Extractor 

1. Make python environment  
 `python -m venv ocr_env `   
2. activate env
3. Install requirements `pip3 install -r requirements.txt`
4. Make a data folder and keep all videos there
5. Make sure to run tests to avoid any bug and error, which is there in the `./tests` folder 
6. To preprocess run `local/run_preprocess.py`    
7. To extract subtitle run `local/run_extract_text.py`




### Docker image setting 
1. Keep all the data in the `data\input_videos`
2. Build docker image using `docker build -t subtitle_extractor -f ./docker/Dockerfile .`
3. Run docker image `docker run --rm -it -t subtitle_extractor`
4. Copy results from docker to local directory `docker cp {container_id}/app/data/output_texts/ my_result_folder`


Read more thought about the solutions [here](https:myname.com)

   
