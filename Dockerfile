FROM python:3.10

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./gonzobot.py"]
