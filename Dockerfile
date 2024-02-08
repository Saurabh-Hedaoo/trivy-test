FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN ["bash", "-c", "pip install -r requirements.txt"]

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
