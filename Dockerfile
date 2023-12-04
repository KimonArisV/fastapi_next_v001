FROM python:3.9.10
WORKDIR /usr/src
COPY requirements.txt .
#RUN apt-get update && apt-get install -y libpq-dev build-essential
RUN pip3 install --upgrade pip
#RUN pip3 install wheel setuptools pip --upgrade
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
