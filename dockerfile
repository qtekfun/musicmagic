FROM python:3.13-slim

WORKDIR /app

ADD https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp /app/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME /app/output

CMD ["python", "app.py"]