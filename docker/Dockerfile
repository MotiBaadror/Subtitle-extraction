FROM python:3.10

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y


COPY ../requirements.txt .

RUN pip3 install -r requirements.txt

WORKDIR /app


COPY /data/ ./data
COPY /src/ .
COPY /local/ .
COPY dir_configs.py ./dir_configs.py

CMD ["python3", "run_preprocess.py"]
CMD ["python3","run_extract_text.py"]



