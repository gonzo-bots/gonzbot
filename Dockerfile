FROM python:3.10

EXPOSE 80
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./gonzobot.py"]
