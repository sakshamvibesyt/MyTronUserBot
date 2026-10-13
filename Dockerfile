FROM python:3.9-slim-bullseye

WORKDIR /workspace/

COPY . /workspace/

RUN apt-get update && 
apt-get install -y --no-install-recommends ffmpeg && 
apt-get clean && 
rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip && 
pip install -r requirements.txt

CMD ["python", "-u", "-m", "main"]
