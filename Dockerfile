FROM python:3.8.2-buster
RUN find . -name "*.pyc" -exec rm -f {} \;
RUN apt-get update && apt-get install -y build-essential software-properties-common g++ make libpq-dev python3-dev  gcc 
ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt

ADD . /code
EXPOSE 5000

CMD ["uwsgi", "--ini", "uwsgi.ini"]