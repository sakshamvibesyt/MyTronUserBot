FROM python:3.11-slim-bookworm

WORKDIR /workspace/

COPY . /workspace/

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg libpq-dev gcc python3-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "-u", "-m", "main"]
