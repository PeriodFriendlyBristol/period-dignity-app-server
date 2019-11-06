FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt &&\
    apt-get update &&\
    apt-get install binutils libproj-dev gdal-bin -y
COPY . /code/
RUN pip install -r requirements.txt
CMD bash /code/run.sh
