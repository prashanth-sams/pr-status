FROM python:3.6

MAINTAINER Saurabh Taneja

RUN apt-get update

RUN apt-get install -y python3-pip

COPY  application_code /application_code

RUN pip install -r /application_code/requirements.txt

EXPOSE 5000

CMD ["/application_code/github_call.py"]
