FROM python:3.7.7-slim
RUN apt-get update -y
RUN apt-get install git -y
RUN apt-get install python3-pip -y
RUN git clone https://github.com/DiegoLorenzo7/practica-creativa2.git
WORKDIR .
RUN pip3 install -r  practica-creativa2/bookinfo/src/productpage/requirements.txt 
ENV GROUP_NUMBER 37
EXPOSE 9080
COPY apliDocker.py .

CMD ["python3","apliDocker.py"]
