FROM python:3.11-slim-bookworm

WORKDIR /workspace/

COPY . /workspace/

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg git libpq-dev gcc python3-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

RUN sed -i 's/MIN_CHANNEL_ID = -1002147483647/MIN_CHANNEL_ID = -1007852516352/' /usr/local/lib/python3.11/site-packages/pyrogram/utils.py && sed -i 's/MIN_CHAT_ID = -2147483647/MIN_CHAT_ID = -999999999999/' /usr/local/lib/python3.11/site-packages/pyrogram/utils.py

CMD ["python", "-u", "-m", "main"]
