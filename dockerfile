from python:3
workdir /app
RUN pip install flask
RUN pip install boto3
RUN pip install requests
RUN pip install elastic-apm[flask]
RUN pip install psutil
COPY . /app
CMD ["python", "app.py"]