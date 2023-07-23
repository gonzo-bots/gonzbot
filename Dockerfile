FROM python:3.10

RUN echo 'pecker'
EXPOSE 80
RUN echo 'head'
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./gonzobot.py"]
